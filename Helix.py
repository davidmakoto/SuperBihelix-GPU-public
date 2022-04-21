class Helix:
    """
    Represents a helix with 4 degrees of freedom: phi, theta, eta, hydrophobic center (hpc), x and y coordinate as well as eta_res and eta_res_num (verify). Each degree of freedom is a list for numberous angles to test following the format of angles.txt input file.
    """
    # def __init__(self):
    #     self.hel_num = None # todo: adjust other implementations outside of this class 
    #     self.phi_angles = []      # tuple replaces phi1 and phi2 arrays
    #     self.eta_angles = []
    #     self.theta_angles = []
    #     self.hpcs = [] # todo: make sure to adjust other implementations outside of class
    #     self.angles_of_interest = []

    #     self.x = None
    #     self.y = None
    #     self.eta_res = None
    #     self.eta_res_num = None # todo verify this is the right name

    # # initalizer for super.template format (includes x, y, EtaRes)
    # # todo: how will numbers be read, as int or str?
    # def __init__(self, 
    #              hel_num_input: int,
    #              x_input: float,
    #              y_input: float,
    #              hpc_input,
    #              theta_angles_input,

    #              phi_angles_input, # left without type checking to accept both lists and an float, sorted out below
    #              eta_angles_input,
    #             #  angles_of_interest_input,
                 
    #              eta_res_abbrev_input: str,
    #             #  eta_res_num_input: float
    #              eta_res_num_input = None #: float
    #              ):
    #     if eta_res_num_input is None:
    #         print("eta res id input is None")
    #     if type(eta_res_num_input) == str:
    #         print("eta res id input is str")
            
        
    #     self.hel_num = hel_num_input
        
    #     # phi angle handling
    #     self.phi_angles = []
    #     if type(phi_angles_input) == float: # change this to also maybe expect a string and type cast it
    #         self.phi_angles.append(phi_angles_input)
    #     elif type(phi_angles_input) == list:
    #         self.phi_angles = phi_angles_input
    #     else:
    #         print("Wrong type passed into phi angles, expected type float or list and recieved " + str(type(phi_angles_input)))
        
    #     # eta angle handling
    #     self.eta_angles = []
    #     if type(eta_angles_input) == float:
    #         self.eta_angles.append(eta_angles_input)
    #     elif type(eta_angles_input) == list:
    #         self.eta_angles = eta_angles_input
    #     else:
    #         print("Wrong type passed into eta angles, expected type float or list and recieved " + str(type(eta_angles_input)))

    #     # theta angle handling
    #     self.theta_angles = []
    #     if type(theta_angles_input) == float:
    #         self.theta_angles.append(theta_angles_input)
    #     elif type(theta_angles_input) == list:
    #         self.theta_angles = theta_angles_input
    #     else:
    #         print("Wrong type passed into theta angles, expected type float or list and recieved " + str(type(theta_angles_input)))
    #     ##################################################

    #     # hpc handling
    #     self.hpcs = []
    #     if type(hpc_input) == float:
    #         self.hpcs.append(hpc_input)
    #     if type(hpc_input) == int:
    #         self.hpcs.append(float(hpc_input))
    #     if type(hpc_input) == str:
    #         print(hpc_input)
    #         self.hpcs.append(float(hpc_input))
    #     elif type(hpc_input) == list:
    #         self.hpcs = hpc_input
    #     else:
    #         print("Wrong type passed into hpc, expected type float or list and recieved " + str(type(hpc_input)))
        
    #     self.angles_of_interest = []

    #     self.x = x_input
    #     self.y = y_input
    #     self.eta_res_abbrev = eta_res_abbrev_input
    #     self.eta_res_num = eta_res_num_input





    # def add_angle_generic(self, 
    #                       angle_type: str, 
    #                       angles: tuple): # todo: would list be better for appending?
    #         # if helices_of_interest.PyTuple_Check(tm_num):    # checking if helix # is relevent, otherwise skip                                                                 
    #     if angle_type == 'eta':                      # start reading in angle name & angles
    #         for angle in angles:
    #             self.eta_angles.append(angle)       # add angle to helix object's list variable, eta_angles. j from .cpp vers is implemented as helix_obj.x_angles.len()
    #     if angle_type == 'phi':
    #         for angle in angles:
    #             self.phi_angles.append(angle)
    #     if angle_type == 'theta':
    #         for angle in angles:
    #             self.theta_angles.append(angle)
    #     GPCR.add_helix(self)
    
    # # todo: (have it incremennt some counter? or unnnnecessary?) def add_angle(self,...)

###################################################################################################

    def __init__(self, 
                 hel_num_input = None,
                 x_input = None,
                 y_input = None,
                 hpc_input = None,
                 theta_angles_input = None,
                 phi_angles_input = None, 
                 eta_angles_input = None,
                #  angles_of_interest_input,
                 eta_res_abbrev_input = None,
                 eta_res_num_input = None
                 ):            
    #  helix number input handling
        if hel_num_input is None: self.hel_num = None # case of empty constructor
        else:
            try:                                      # try to cast input to int and assign to GPCR var
                self.hel_num = int(hel_num_input)
            except ValueError:
                print("Unable to convert helix number input: \"" + hel_num_input + "\" to float")
    #  x input handling

        if x_input is None: self.x = None  # case of empty constructor
        else:                              # case of passing in single float for x val
            try: 
                self.x = float(x_input)
            except ValueError:
                print("Unable to convert x input: \"" + x_input + "\" to integer")

    #  y input handling

        if y_input is None: self.y = None  # case of empty constructor
        else:                              # case of passing in single float for x val
            try: 
                self.y = float(y_input)
            except ValueError:
                print("Unable to convert y input: \"" + y_input + "\" to float")

    #  hpc input handling
        self.hpcs = []
        if hpc_input is None:          pass                  # case of empty constructor
        elif type(hpc_input) == list:  self.hpcs = hpc_input # case of passing in list, set equal to obj var
        else:                                                # case of passing in single float for x val
            try: 
                self.hpcs.append(float(hpc_input))
            except ValueError:
                print("Unable to convert hpc input: \"" + hpc_input + "\" to float")

    # theta angle handling
        self.theta_angles = []
        if theta_angles_input is None:         pass                                   # if no input      -> leave list empty                                         
        elif type(theta_angles_input) == list: self.theta_angles = theta_angles_input # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
        else:
            try:                                                                     # if not None or list, try to convert to float and append todo: do I need 2 statements instead of 1 here to trigger error correctly?
                self.theta_angles.append(float(theta_angles_input))
            except ValueError:
                print("Unable to convert theta angle input: \"" + theta_angles_input + "\" to float")


    # phi angle handling
        self.phi_angles = []
        if phi_angles_input is None:         pass                                     # if no input      -> leave list empty                                 
        elif type(phi_angles_input) == list: self.phi_angles = phi_angles_input       # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
        else:
            try: 
                self.phi_angles.append(float(phi_angles_input))
            except ValueError:
                print("Unable to convert phi angle input: \"" + phi_angles_input + "\" to float")

    # eta angle handling
        self.eta_angles = []
        if eta_angles_input is None:         pass                                     # if no input      -> leave list empty                                 
        elif type(eta_angles_input) == list: self.eta_angles = eta_angles_input       # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
        # todo: can I make line above cast to float?
        else:
            try: 
                self.eta_angles.append(float(eta_angles_input)) # todo: why is this string?
            except ValueError:
                print("Unable to convert eta angle input: \"" + eta_angles_input + "\" to float")        

    #  eta res abbreviation input handling
        if eta_res_abbrev_input is None: self.eta_res_abbrev = None
        else:
            try: 
                self.eta_res_abbrev = str(eta_res_abbrev_input)
            except ValueError:
                print("Unable to convert eta residue abbrevation input: \"" + eta_res_abbrev_input + "\" to string")

    #  eta res id input handling
        if eta_res_num_input is None: self.eta_res_num = None
        else:
            try: 
                self.eta_res_num = int(eta_res_num_input)
            except ValueError:
                print("Unable to convert eta residue number input: \"" + eta_res_num_input + "\" to int")


        self.angles_of_interest = []
