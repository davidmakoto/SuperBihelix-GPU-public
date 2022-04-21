import Helix as Helix

class GPCR:
    def __init__(self):
        self.helices = []

    def __init__(self, helices):
        self.helices = []   # tuple or list? 
        if helices is None:
            return
        elif helices.len() > 0:
            for helix in helices:
                self.helices.append(helix)  # change this later so that it creates a list
        
    def add_helix(self, helix: Helix):
        self.helices.append(helix)
    
    
    def check_for_duplicate_helices(self, hel_num: int):
        ''' Input a helix to see if there's a duplicate, if there is return helix obj, else return None '''
        for hel in self.helices:
            if hel_num == hel.hel_num:
                return hel  # returns helix
        return None
