import unittest
import pandas as pd
import SuperBiHelix_GPU as SuperBiHelix
import GPCR as GPCRClass
import Helix as Helix

class TestBiHelix(unittest.TestCase):
    def setUp(self):
        self.GPCR_angles_txt = GPCRClass.GPCR(None)
        SuperBiHelix.read_angles("CPU_Code/angles.txt", (5,7), self.GPCR_angles_txt)

        self.GPCR_super_template = GPCRClass.GPCR(None)
        SuperBiHelix.read_starting_struct("CPU_Code/super.template", self.GPCR_super_template)
        # have functions above be identical in arguments (second missing angles of interest)

        # self.hel_pair_conform_df = pd.DataFrame(columns=['phi_ang1', 'theta_ang1', 'eta_ang1', 'hpc1', # each entry is a list 
        #                                                  'phi_ang2', 'theta_ang2', 'eta_ang2', 'hpc2']) 


    def test_read_angles(self):        
        self.assertEqual(self.GPCR_angles_txt.helices[0].hel_num, 5)
        self.assertEqual(self.GPCR_angles_txt.helices[0].eta_angles[2], 0)
        self.assertEqual(self.GPCR_angles_txt.helices[1].eta_angles[2], 0)

    def test_read_super_template(self):        
        self.assertEqual(self.GPCR_super_template.helices[0].hel_num, 1)
        self.assertEqual(self.GPCR_super_template.helices[0].eta_angles[0], 193.97)

        #* needs slight fixing - type conversion to int
        # wtf does this mean TypeError: 'int' object is not subscriptable 
        # self.assertEqual(self.GPCR_super_template.helices[6].eta_res_num[0], 323)
        # print(str(type(self.GPCR_super_template.helices[6].eta_res_num[0])))


        # self.assertNotEqual(self.GPCR_super_template.helices[0].eta_res_abbrev, None)

        
        # self.assertEqual(self.GPCR_super_template.helices[1].eta_angles[2], 0)
    # def test_hel_pair_conform_df(self): # todo: move this section of code to GPCR class and make it a function so it is easily testable
        # print(self.hel_pair_conform_df)
        # self.assertAlmostEqual()

        



if __name__ == '__main__':
    unittest.main()