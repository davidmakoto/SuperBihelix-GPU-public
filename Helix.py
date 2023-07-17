class Helix:
    """
    Represents a helix with 4 degrees of freedom: phi, theta, eta, hydrophobic center (hpc), x and y coordinate as well as eta_res and eta_res_num (verify). Each degree of freedom is a list for numberous angles to test following the format of angles.txt input file.
    """

    def __init__(self,
                 hel_num_input=None,
                 x_input=None,
                 y_input=None,
                 hpc_input=None,
                 theta_angles_input=None,
                 phi_angles_input=None,
                 eta_angles_input=None,
                 eta_res_abbrev_input=None,
                 eta_res_num_input=None
                 ):
        #  helix number input handling
        if hel_num_input is None:
            self.hel_num = None  # case of empty constructor
        else:
            try:                                      # try to cast input to int and assign to GPCR var
                self.hel_num = int(hel_num_input)
            except ValueError:
                print("Unable to convert helix number input: \"" +
                      hel_num_input + "\" to float")
    #  x input handling
        if x_input is None:
            self.x = None  # case of empty constructor
        else:                              # case of passing in single float for x val
            try:
                self.x = float(x_input)
            except ValueError:
                print("Unable to convert x input: \"" +
                      x_input + "\" to integer")

    #  y input handling
        if y_input is None:
            self.y = None  # case of empty constructor
        else:                              # case of passing in single float for x val
            try:
                self.y = float(y_input)
            except ValueError:
                print("Unable to convert y input: \"" + y_input + "\" to float")

    #  hpc input handling
        self.hpcs = []
        if hpc_input is None:
            pass                  # case of empty constructor
        elif type(hpc_input) == list:
            self.hpcs = hpc_input  # case of passing in list, set equal to obj var
        else:                                                # case of passing in single float for x val
            try:
                self.hpcs.append(float(hpc_input))
            except ValueError:
                print("Unable to convert hpc input: \"" +
                      hpc_input + "\" to float")

    # theta angle handling
        self.theta_angles = []
        if theta_angles_input is None:
            pass                                   # if no input      -> leave list empty
        elif type(theta_angles_input) == list:
            # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
            self.theta_angles = theta_angles_input
        else:
            # if not None or list, try to convert to float and append todo: do I need 2 statements instead of 1 here to trigger error correctly?
            try:
                self.theta_angles.append(float(theta_angles_input))
            except ValueError:
                print("Unable to convert theta angle input: \"" +
                      theta_angles_input + "\" to float")

    # phi angle handling
        self.phi_angles = []
        if phi_angles_input is None:
            pass                                     # if no input      -> leave list empty
        elif type(phi_angles_input) == list:
            # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
            self.phi_angles = phi_angles_input
        else:
            try:
                self.phi_angles.append(float(phi_angles_input))
            except ValueError:
                print("Unable to convert phi angle input: \"" +
                      phi_angles_input + "\" to float")

    # eta angle handling
        self.eta_angles = []
        if eta_angles_input is None:
            pass                                     # if no input      -> leave list empty
        elif type(eta_angles_input) == list:
            # if input is list -> set new list equal (todo: do I need a copy constructor to not get reference here?)
            self.eta_angles = eta_angles_input
        # todo: can I make line above cast to float?
        else:
            try:
                # todo: why is this string?
                self.eta_angles.append(float(eta_angles_input))
            except ValueError:
                print("Unable to convert eta angle input: \"" +
                      eta_angles_input + "\" to float")

    #  eta res abbreviation input handling
        if eta_res_abbrev_input is None:
            self.eta_res_abbrev = None
        else:
            try:
                self.eta_res_abbrev = str(eta_res_abbrev_input)
            except ValueError:
                print("Unable to convert eta residue abbrevation input: \"" +
                      eta_res_abbrev_input + "\" to string")

    #  eta res id input handling
        if eta_res_num_input is None:
            self.eta_res_num = None
        else:
            try:
                self.eta_res_num = int(eta_res_num_input)
            except ValueError:
                print("Unable to convert eta residue number input: \"" +
                      eta_res_num_input + "\" to int")

        self.angles_of_interest = []
