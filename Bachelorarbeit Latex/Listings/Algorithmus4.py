class Program:
    
    def __init__(self, name, capacity, allowsfor):
        ...
        self.allowsforeign = allowsfor
        
    ...
    def count_indians(self):
        k = 0
        for x in self.wait_list:
            if x.isindian == True:
                k = k + 1
        return k
    
    def last_indian_waitlist(self):
        last_indian = self.wait_list[0]
        for x in self.wait_list:
            if x.isindian == True:
                last_indian = x
        return last_indian
    
    
class Candidate:
    
    def __init__(self, name, preference_list, isind):
        ...
        self.isindian = isind


def algorithm4(candidates, programs, queue=[], cat_change=[]):
    
    if len(queue) == 0:
        for c in candidates:
            if c.isindian:
                if len(c.preference_list) > 0:
                    queue.append(c)      
    ...             
    for c in candidates:
        if c.isindian == False:
            while c.i < len(c.preference_list):
                p = c.preference_list[c.i]
                if p.allowsforeign == True:
                    k = p.count_indians()
                    if k <= p.capacity:
                        p.wait_list.append(c)
                        p.sort_waitlist()  
                        break
                    else:
                        y = p.last_indian_waitlist()
                        if p.merit_list[c] <= p.merit_list[y]:
                            p.wait_list.append[c]
                            break
                c.i = c.i + 1
    
    return candidates, programs