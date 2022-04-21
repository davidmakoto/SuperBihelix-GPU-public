import Helper as helpers
import Helix as Helix
import GPCR as GPCRClass
import pandas as pd
import numpy as np

# import CUDA_kernels as CUDA_kernels
import pycuda.driver as drv
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule
from time import time

# driver code:
#   1) Creates GPCR object
#   2) Initialites interacting helices (hard coded for now)
#   3) Parses protein input information
#   4) Formats protein helix pair input
#   5) GPU_setup organizes information for PyCUDA framework and sends jobs to gpu 

def main():
    # handle_com_line_args()
    GPCR = GPCRClass.GPCR(None)  # creating empty GPCR obj to attach conformation information to
    helices_of_interest = (1, 2)

    # Inputs
    read_starting_struct('CPU_Code/super.template', GPCR)
    read_angles('CPU_Code/angles.txt', 
                  helices_of_interest, 
                  GPCR)
                  # todo: should this be a second GPCR?
                  # todo: figure out how to store all gpcr info in another gpcr based on helices of interest and starting structure

    hel_pair_df = create_helix_pair_df(GPCR)  
    GPU_setup(hel_pair_df) # handles all of the device interaction code
         

# real function definition cannot be published
def create_helix_pair_df (GPCR: GPCRClass): pass  

def read_angles(file_name: str, 
                helices_of_interest: tuple, 
                GPCR: GPCRClass):
    """
    Takes in file name, helices user is interested in, and a GPCR obj.
    Reads helix information from file name provided and attaches helix
    information to GPCR object. Will only return helices of interest.
    If no file found or empty file, 'None' will be returned.
    """

    with open(file_name, 'r') as reader:
        for line in reader.readlines():  # reading through each line, keeping 
            line_words = line.split()                       # formatting lines
            line_map = map(str.strip, line_words)
            line_list = list(line_map)                      # map to use indices for words
            hel_num = int(line_list[0][2])                  # 3rd position of string with form 'TM7'

            angle_type = line_list[1]                       # 2nd arg of list
            angles_list = line_list[2:]                     # cut out used args to isolate angle arguments
            
            #* don't store helix input info if not interested in specific helix (defined in main function)
            if hel_num in helices_of_interest:              
                
                #* checks for duplicates based on helix number read and existing helices in GPCR obj - returns helix object
                duplicate_helix = GPCR.check_for_duplicate_helices(hel_num)  
                if duplicate_helix is None:                 # case of no duplicates in GPCR found 
                    helix = Helix.Helix()                   # new Helix obj - added to GPCR at end
                    helix.hel_num = hel_num                 # setting helix obj values
                else:
                    helix = duplicate_helix                 # use existing helix that matches TM hel number
                            
                #* start reading in angle name & angles
                if angle_type == 'eta':                  
                    for angle in angles_list:
                        helix.eta_angles.append(float(angle))      # add angle to helix object's list variable, eta_angles. j from .cpp vers is implemented as len( helix_obj.x_angles )
                if angle_type == 'phi':
                    for angle in angles_list:
                        helix.phi_angles.append(float(angle))
                if angle_type == 'theta':
                    for angle in angles_list:
                        helix.theta_angles.append(float(angle))
                if angle_type == 'hpc':
                    for hpc in angles_list:
                            helix.hpcs.append(float(hpc))

                if duplicate_helix is None: # if no duplicate found, add new helix to GPCR obj, else if duplicate found, helix is already attached to GPCR
                    GPCR.add_helix(helix)


def read_starting_struct(file_name: str, 
                         GPCR: GPCRClass):

    # TODO: where does the GPCR come from? created here & returned or passed in as param?

    with open(file_name, 'r') as reader:
        for line in reader.readlines():  # reading through each line, keeping 
            line_words = line.split()                       # formatting lines
            line_map = map(str.strip, line_words)
            line_list = list(line_map)                      # map to use indices for words
            
            if line_list[1] == "TM": return  # exit condition - end of file
            
            hel_num = int(line_list[1][0]) # 2nd word 1st letter (grabing # from )
            line_list = line_list[2:] # isolate 3rd word and on (x, y,...), and cast to string for next line
            x, y, hpc, theta, phi, eta, res_abbrev, res_num = line_list # make sure this is string type
            helix = Helix.Helix(int(hel_num),
                                float(x),
                                float(y),
                                float(hpc),
                                float(theta),
                                float(phi),
                                float(eta),
                                str(res_abbrev),
                                int(res_num)) # position of res in full sequence
            GPCR.add_helix(helix)


def GPU_setup(hel_pair_df: pd.DataFrame):

    number_of_tasks = 12 * 12 * 12 * 2#=1728 = 3456
    # number_of_tasks = hel_pair_df.size #TODO: make this unsigned int, causing issues
    fact = 15


    gpuResultArray = host_to_gpu(fact, number_of_tasks, hel_pair_df)           # rest of GPU setup
    cpuResultArray = helpers.cpuFactorial(fact, number_of_tasks)  # same calculations on CPU for time and accuracy analysis

    # debugging, if using random input, comment section below
    print("Does our kernel work correctly? : {}".format(np.allclose(gpuResultArray, cpuResultArray)))  # compares gpu and cpu arrays and returns true/false
    helpers.checkNumberOfTargetValues(gpuResultArray, fact)  # function to check number of occurances of math.factorial(fact), within gpuResultArray

def host_to_gpu(kernel_input, num_tasks, hel_pair_df: pd.DataFrame):
    BLOCK_SIZE = (1, 1, 1)  # each thread block contains only one thread
    GRID_SIZE = (num_tasks, 1, 1)  # 1d grid, the size of arr is same as num of tasks
    multiple_kernel_function_gpu = CUDA_kernels.ker.get_function("parent_kernel_function")  # getting references to device kernels to be called from host - Kernels stored in CUDAKernels.py
    helix_pair_energy_gpu = CUDA_kernels.ker.get_function("helix_pair_energy")

    # creating arr to use to allocate space on gpu - arguments of np function are (size, array input, type)
    # the hel_pair_df is used as input and df_col_to_np_arr is used to cast pd.df column to np.array
    phi1_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "phi1"), np.float32)
    theta1_input_arr = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "theta1"), np.float32)
    eta1_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "eta1"), np.float32)
    hpc1_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "hpc1"), np.float32)

    phi2_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "phi2"), np.float32)
    theta2_input_arr = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "theta2"), np.float32)
    eta2_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "eta2"), np.float32)
    hpc2_input_arr   = np.full(len(hel_pair_df), df_col_to_np_arr(hel_pair_df, "hpc2"), np.float32)
    # print("--- phi1_input_arr --- ", phi1_input_arr)  # for debugging

    # allocating memory on the gpu of size (input arr)
    input_phi1_array_gpu   = gpuarray.to_gpu(phi1_input_arr)
    input_theta1_array_gpu = gpuarray.to_gpu(theta1_input_arr)
    input_eta1_array_gpu   = gpuarray.to_gpu(eta1_input_arr)
    input_hpc1_array_gpu   = gpuarray.to_gpu(hpc1_input_arr)

    input_phi2_array_gpu   = gpuarray.to_gpu(phi2_input_arr)
    input_theta2_array_gpu = gpuarray.to_gpu(theta2_input_arr)
    input_eta2_array_gpu   = gpuarray.to_gpu(eta2_input_arr)
    input_hpc2_array_gpu   = gpuarray.to_gpu(hpc2_input_arr)

    # allocating memory on gpu for the output, the same size as "phi1_input_arr" 
    out_gpu = gpuarray.empty_like(input_phi1_array_gpu)

    # calling kernel
    helix_pair_energy_gpu(
        input_phi1_array_gpu,  # input arrs
        input_theta1_array_gpu,
        input_eta1_array_gpu,
        input_hpc1_array_gpu,
        input_phi2_array_gpu,
        input_theta2_array_gpu,
        input_eta2_array_gpu,
        input_hpc2_array_gpu,
        out_gpu,                # output array
        block=BLOCK_SIZE, grid=GRID_SIZE  # specifying number of processes to run,
    )

    print("output from the gpus is: ", out_gpu)

    # uncomment if running RANDOM input values
    # input_array = np.random.randint(15, size=num_tasks)  # creates 1d arr of size (num_tasks) with random values between 0-14
    # print("----------------------------------------------------------------------------------------")
    # print("printing random array of ints from 0-14, input_array", input_array)
    # print("----------------------------------------------------------------------------------------")

#* OLD CODE BELOW, ONLY FOR REFERENCE
    #   options: arr size, initialized value, type
    input_array = np.full(num_tasks, kernel_input, np.float32)  # creating 1d numpy  array "a" the size of "num_tasks" - typecast to single precision (max size for most gpus) # todo: make sure won't need double precision for bihelix
    input_array_gpu = gpuarray.to_gpu(input_array)  # allocating memory on gpu, the same size as "a"

    outputArrayGPU = gpuarray.empty_like(input_array_gpu)  # allocating memory on gpu for the output, the same size as "a" (all 3 vectors same size)

    t1 = time()
    multiple_kernel_function_gpu(
        input_array_gpu,  # input arr
        outputArrayGPU,  # output arr, same size as input arr
        block=BLOCK_SIZE, grid=GRID_SIZE  # specifying number of processes to run,
    )  # and orientation (defined at top of function)
    print("Output from the multi function kernel\n", outputArrayGPU)
    print('Total time for GPU function:  %fs' % (time() - t1))
    return outputArrayGPU.get()  # returns output from gpu function for debugging purposes (shown in main function)

def df_col_to_np_arr(df: pd.DataFrame, col_name):
    return df.loc[:,col_name].values


if __name__ == "__main__": 
    main()
