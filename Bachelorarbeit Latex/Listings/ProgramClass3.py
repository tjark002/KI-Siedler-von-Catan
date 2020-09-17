class Program:
    
    def __init__(self, name, capacity):
        ...
        self.merit_list = dict()
        ...
        
    def initialize(self, candidates):
        temp = dict()
        for x in candidates:
            temp[x] = rand.randint(1,5)
        self.merit_list = temp.copy()
        
    def sort_waitlist(self): #Warteliste sortieren
        temp = []
        for key, value in sorted(self.merit_list.items(), key=lambda item: item[1]):
            if key in self.wait_list:
                temp.append(key)
        self.wait_list = temp
        
    def sort(self, candidates): #Beliebige Kandidaten sortieren
        temp = []
        for key, value in sorted(self.merit_list.items(), key=lambda item: item[1]):
            if key in candidates:
                temp.append(key)
        return temp
    
    def get_rank_of_candidate(self, candidate):
        return self.merit_list[candidate]
        
    def get_candidates_with_rank(self, rank):
        candidates = list()
        items = self.merit_list.items()
        for item in items:
            if item[1] == rank and item[0] in self.wait_list:
                candidates.append(item[0])
        return candidates