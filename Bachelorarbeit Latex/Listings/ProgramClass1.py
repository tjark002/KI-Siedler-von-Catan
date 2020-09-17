class Program:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = []
        
    def initialize(self, candidates):
        rand.shuffle(candidates)
        self.merit_list = candidates.copy()
        
    def sort_waitlist(self): #Warteliste sortieren
        temp = []
        for c in self.merit_list:
            if c in self.wait_list:
                temp.append(c)
        self.wait_list = temp
        
    def sort(self, candidates): #Beliebige Kandidaten sortieren
        temp = []
        for c in self.merit_list:
            if c in candidates:
                temp.append(c)
        return temp
    
class Candidate:
    
    def __init__(self, name, preference_list):
        self.name = name
        self.preference_list = preference_list
        self.i = 0
        self.p = "Leer"
    
    def allocate(self, p):
        self.p = p.name
        
def generate_preferences(programs):
    amount = rand.randint(2,4)
    rand.shuffle(programs)
    programs = programs[:amount]
    return programs