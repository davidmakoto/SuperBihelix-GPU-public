# GPU Enabled SuperBihelix
is a boilerplate app to run portions of the patented molecular dynamics simulation, SuperBihelix, in parallel on graphics processing units (GPU) using the PyCUDA/CUDA framework.


# Table of contents
* [Motivation](#motivation)
* [Introduction](#introduction)
* [Disclaimer](#disclaimer)
* [Dependancies](#dependancies)
* [Project Sturcture](#project-structure)
* [Running Instructions](#running-instructions)
* [Next Steps](#next-steps)
* [References](#references)

# Motivation
This project was created to speed up the current implementation of the pattented conformational analysis algorithm, SuperBihelix via parallization. The algorithm's exhaustive nature (> 13 trillion input structures) causes the algorithm to take days to weeks to run depending on the supercomputer. In addition, the SuperBihelix algorithm "cuts corners" in order to make the runtime bearable, by sampling a circular region 3 or 5 times instead of 360 or 720 times, hindering the true strength of the algorithm. Parallel processing is the most obvious solution to improve the run time of this legacy algorithm. 


# Introduction: 
### Structural bioinformatics
The SuperBihelix algorithm is a pattented sturctural bioinformatics algorithm used to determine the stability various conformations (possible orientations) of a GPCR aka seven transmembrane (7TM) proteins. It is useful for drug researchers investigating cell signaling pathways. The analysis is done by constructing a physics based model of the protein's structure, followed by a brute force stability calculation of every single possible orientation of the protein -- the most stable of which are outputted to the researcher.

Without molecular dynamics conformational sampling tools, researchers generally rely on crystallography or cryo-electron microscopy images to attain a conformational snapshot of a protein, for investigation. Unfortinately, these techniques produce a single conformational space, and can take weeks or months to produce one particular crystal structure. Trying to find a target protein's exact conformation using older techniques can be compared to trial and error based on educated guesses, that are only validated after a lengthy and possibly expensive process.

<!-- GPCR IMAGE -->
<p align="center">
  <img width=70% 
       src="https://user-images.githubusercontent.com/20344260/168345619-f4063ae9-0310-445e-957b-68390f924bdf.png">
</p>
<!-- caption -->
<p align = "center">
A. Typical seven-helix bundle. B. Nearest-neighbor helix pairs highlighted by double arrows; C. The 12 helix pairs shown explicitly. Source: [1]
</p>

  
 
The number of configurations analyzed is designed to reach 13 trillion for a 7TM protein, a very high number due to the three degrees of freedom taken into account for each of the 7TM protein's 7 helices (5 × 3 × 5) ^ 7 = 13.35 trillion. Right now, the algorithm is reliant on extreme computing power leading to runtimes of days or weeks, even with the algorithm intentionally cutting corners to decrease the problem size. 

To avoid cutting corners, the amount of inputs per DOF would be increased greatly, in turn, increasing the problem size exponentially. For example, each DOF currently takes 3 or 5 conformational samples per 360 degree rotational sample space, which would mean it takes a conformational sample each 120 or 72 degrees, respectively. Ideal analysis would sample more possibilities, such as every 10 degrees producing 36 sample angles for that DOF. However, this could increases the number of calculations from 1.335 e13 to (36 ^ 3) ^ 7 = 4.81 e32. This computational bottleneck prompted the idea of parallel processing through the general purpose graphics processing unit (GPGPU) paradigm. 

<!-- DEGREES OF FREEDOM IMAGE -->
<p align="center">
  <img width=70%
       src="https://user-images.githubusercontent.com/20344260/168344976-70ea1aa9-042f-4be3-b030-5713ed72eca6.png">
</p>
<!-- caption -->
<p align = "center">
Coordinates specifying the orientation of a TM helix in a membrane [1].
</p>


More can be read about the SuperBihelix algorithm in the [Bihelix paper](https://pubmed.ncbi.nlm.nih.gov/22173949/) or the [SuperBihelix paper](https://www.pnas.org/doi/pdf/10.1073/pnas.1321233111).

### PyCUDA GPGPU framework
The PyCUDA framework was used to interface with the Nvidia GPU. PyCUDA is a wrapper for NVIDIA's GPU framework, CUDA (C/C++), which falls under the paraell paradigm umbrella of languages. The PyCUDA framework simplifies the process of sending jobs to the GPU, memory allocation, etc. The general workflow behind PyCUDA is as follows:
* initalize GPU parameters (e.g. parameters related to sharing memory on the GPU architecture such as block/grid size)
* define CUDA C/C++ functions or kernels, which are run by the device 
* allocate input and output arrays to exchange information the GPU device
* and finally send jobs (kernel tasks) to the gpu.

To learn more understand more about parallel processing using gpus, check out the following resources:
* [PyCUDA Documentation](https://documen.tician.de/pycuda/)
* [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/)
* [Book: Hands-On GPU Programming with Python and CUDA: Explore high-performance parallel computing with CUDA](https://www.amazon.com/Hands-Programming-Python-CUDA-high-performance/dp/1788993918)


<!-- PyCUDA descriptive slide -->
<p align="center">
  <img width=90% 
       src="https://user-images.githubusercontent.com/20344260/168404356-f9a5aad4-957f-46d9-b4e3-803b2f5e78aa.png">
</p>
<!-- caption -->
<p align = "center">
Description pipeline of tasks from host to device and compatibility of NVCC compiler.
</p>


# Disclaimer
The code is not functional due to a pattent on the parent algorithm. This redacted repo is primarily here to showcase my work. For those interested in joining the project, please send me a message on getting more information.


# Project Structure
The general structure of the code is as follows:


#### main driver
superbihelix_GPU.py

#### GPCR and Helix classes
* GPCR.py 
* Helix.py

#### device code
* CUDA_kernels.py
<br> CUDA C/C++ code for PyCUDA

#### input files
* super.template
* angles_local.txt


#### GPU benchmark helpers
* Helper.py 
<br>
Functions related to comparing the time to complete tasks on the GPU and CPU and verifying identical answers of large arrays.


# Dependancies
* Python 3.7
* Numpy
* Pandas 
* NVIDIA GPU hardware
* PyCUDA (python framework built on NVIDIA's compute unified device architecture (CUDA) framework)




# Running Instructions
Navigate to the parent directory for the project and paste the following lines into a terminal
```bash
git clone https://github.com/dmw01/SuperBihelix-GPU-public.git;
cd SuperBihelix-GPU-public;
pip install pandas numpy pycuda; 
python3 SuperBihelix_GPU.py
```

# Next Steps
The next step in the project is to identify time consuming steps within specific parts of the algorithm and rewrite the code in PyCUDA or Python's Numba library. The most time consuming step is the side chain optimization via Side-Chain Rotamer Excitation Analysis Method (SCREAM). However, the implementation is ~2500 lines of non-CUDA compatible python. In addition, the initial calling of SuperBihelix must be refractored from iterative processing to parallel processing, in a way that all of the steps proceeding the SCREAM process is completed.
The current structure of SuperBihelix_GPU.py assumes that all of the algorithms within SuperBihelix can be parallelized using NVCC, as this was the assumption until the project ended. The skeleton behind the non public version of SuperBihelix GPU can serve as a starting template for what needs to be done with SCREAM. 



## References
<a id="1">[1]</a> 
Raviender Abrol, Jenelle K Bray, William A Goddard 3rd (2012). 
Bihelix: Towards de novo structure prediction of an ensemble of G-protein coupled receptor conformations
Proteins. 2012 Feb;80(2):505-18.
https://pubmed.ncbi.nlm.nih.gov/22173949/

<a id="1">[2]</a> 
Jenelle K Bray, Raviender Abrol, William A Goddard III, Bartosz Trzaskowski, and Caitlin E. Scott (2014). 
SuperBiHelix method for predicting the pleiotropic ensemble of G-protein-coupled receptor conformations
Proceedings of the National Academy of Sciences. 2014;E72-E78
https://www.pnas.org/doi/10.1073/pnas.1321233111
<br>



Work done under Dr. Raviender Abrol at California State University, Northridge.
