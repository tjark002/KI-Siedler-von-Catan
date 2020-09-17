#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rand


# ## Utility

# In[2]:


class Program:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = []
        self.min_cutoff = 0
        
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


# In[2]:


def generate_preferences(programs):
    amount = rand.randint(2,4)
    rand.shuffle(programs)
    programs = programs[:amount]
    return programs
    
def generate_merit(candidates):
    rand.shuffle(candidates)
    cs = candidates.copy()
    return cs

def print_candidates(candidates):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for c in candidates:
        print("********************************** " + c.name + ": " + str(c.p))
        for p in c.preference_list:
            print(p.name)

def print_programs(programs):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for p in programs:
        print("********************************** " + p.name + " " + str(p.capacity) + ": ")
        for c in p.merit_list:
            print(c.name) 


# ## Algorithm 1

# In[4]:


def generate_preferences(programs):
    amount = rand.randint(2,4)
    rand.shuffle(programs)
    programs = programs[:amount]
    return programs
    
def generate_merit(candidates):
    rand.shuffle(candidates)
    cs = candidates.copy()
    return cs

class Program:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = []
        self.min_cutoff = 0
        
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
        
def algorithm1(candidates, programs):
    queue = []

    for p in programs:
        #print("Programm")
        p.wait_list = []
        
    for c in candidates:
        #print("Kandidat")
        if len(c.preference_list) > 0:
            queue.append(c)
        
    while queue:
        c = queue[0] #Wähle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        p = c.preference_list[c.i]
        
        #Prüft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Präferenzenliste zu finden)
        if not p == c.preference_list[c.i]: 
            reject(c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
        
        #Wenn er geeignet ist, wird er einsortiert
        #print(len(p.wait_list), p.capacity)
        if len(p.wait_list) == p.capacity:
            lastc = p.wait_list[-1] #Das letzte Element der der Warteliste zwischenspeichern
            #print(p.name, ": ", lastc.name)
            
            #Wenn der neue Kandidat besser als der auf dem letzten Platz ist, ersetzt er ihn
            #print(lastc.name + ": ", p.merit_list.index(lastc))
            #print(c.name + ": ", p.merit_list.index(c))
            if p.merit_list.index(lastc) > p.merit_list.index(c): 
                p.wait_list[-1] = c
                reject(queue, lastc)
                p.sort_waitlist() #Sorgt dafür, dass die Warteliste sortiert bleibt
            else:
                reject(queue, c)
                
        else:
            p.wait_list.append(c)
            p.sort_waitlist() #Sorgt dafür, dass die Warteliste sortiert bleibt
    
    for c in candidates:
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
            if p in c.preference_list:
                c.allocate(p)
        else:
            c.p = 0
    
    return candidates, programs

def reject(queue, c):
    c.i = c.i + 1
    if c.i < len(c.preference_list):
        p = c.preference_list[c.i]
        if p in c.preference_list:
            queue.append(c)
    
    return queue


# In[5]:


candidates, programs = algorithm1(candidates, programs)


# ## Algorithm 2

# In[436]:


def generate_preferences(programs):
    amount = rand.randint(2,4)
    rand.shuffle(programs)
    programs = programs[:amount]
    return programs
    
def generate_merit(candidates):
    rand.shuffle(candidates)
    cs = candidates.copy()
    return cs

class Program:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = []
        self.min_cutoff = 0
        
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
        
def algorithm2(candidates, programs, queue=[], cat_change=[]):
          
    for c in candidates:
        if len(c.preference_list) > 0:
            queue.append(c)
            
    while queue:
        c = queue[0] #Wähle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
        
        #Prüft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Präferenzenliste zu finden)
        if not (c.i < len(c.preference_list) and p == c.preference_list[c.i]) or p.capacity == 0: 
            reject(queue, c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
            
        if len(p.wait_list) > 0:
            y = p.wait_list[-1] #y ist das letzte Element der Warteliste von P
            #Sortierter Schnitt von wait_list und cat_change
            temp = []
            for x in p.wait_list:
                if x in cat_change:
                    temp.append(c)
            if len(temp) > 0:
                w = temp[-1]
            else: 
                w = 0
        else: 
            w = 0
            y = 0
        
        p.wait_list.append(c)
        p.sort_waitlist()     
            
        if len(p.wait_list) <= p.capacity:
            continue
        
        if w == 0 and y != 0:
            if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff:
                if c in cat_change:
                    queue = penalty_remove_and_reject(queue, c, p)
            else:
                r = p.sort([c, y])[-1]
                queue = remove_and_reject(queue, r, p)
        elif w != 0 and y != 0:
            if y != w:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p)
                else:
                    r = p.sort([c, y, w])[-1]
                    queue = remove_and_reject(queue, r, p)
            else:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p)
                else:
                    r = p.sort([c, y])[-1]
                    queue = remove_and_reject(queue, r, p)
    
    for c in candidates:
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
            if p in c.preference_list:
                c.allocate(p)
        else:
            c.p = 0
    
    return candidates, programs


def reject(queue, c):
    c.i = c.i + 1
    if c.i < len(c.preference_list):
        p = c.preference_list[c.i]
        if p in c.preference_list:
            queue.append(c)
    return queue

def remove_and_reject(queue, w, p):
    #print(len(p.wait_list))
    del p.wait_list[p.wait_list.index(w)]
    #print(len(p.wait_list))
    queue = reject(queue, w)
    return queue

def penalty_remove_and_reject(queue, w, p):
    #print(len(p.wait_list))
    del p.wait_list[p.wait_list.index(w)]
    #print(len(p.wait_list))
    queue = reject(queue, w)
    return queue


# In[205]:


def algorithm21(candidates, programs, queue=[], cat_change=[]):
          
    if len(queue) == 0:
        for c in candidates:
            if len(c.preference_list) > 0:
                queue.append(c)
            
    while queue:
        c = queue[0] #Wähle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
        
        #Prüft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Präferenzenliste zu finden)
        if not (c.i < len(c.preference_list) and p == c.preference_list[c.i]) or p.capacity == 0: 
            reject(queue, c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
            
        if len(p.wait_list) > 0:
            y = p.wait_list[-1] #y ist das letzte Element der Warteliste von P
            #Sortierter Schnitt von wait_list und cat_change
            temp = []
            for x in p.wait_list:
                if x in cat_change:
                    temp.append(c)
            if len(temp) > 0:
                w = temp[-1]
            else: 
                w = 0
        else: 
            w = 0
            y = 0
        
        p.wait_list.append(c)
        p.sort_waitlist()     
            
        if len(p.wait_list) <= p.capacity:
            continue
        
        if w == 0 and y != 0:
            if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff:
                if c in cat_change:
                    queue = penalty_remove_and_reject(queue, c, p)
            else:
                r = p.sort([c, y])[-1]
                queue = remove_and_reject(queue, r, p)
        elif w != 0 and y != 0:
            if y != w:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p)
                else:
                    r = p.sort([c, y, w])[-1]
                    queue = remove_and_reject(queue, r, p)
            else:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p)
                else:
                    r = p.sort([c, y])[-1]
                    queue = remove_and_reject(queue, r, p)
    
    for c in candidates:
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
            if p in c.preference_list:
                c.allocate(p)
        else:
            c.p = 0
    
    return candidates, programs

def reject(queue, c):
    c.i = c.i + 1
    if c.i < len(c.preference_list):
        p = c.preference_list[c.i]
        if p in c.preference_list:
            queue.append(c)
    return queue

def remove_and_reject(queue, w, p):
    #print(len(p.wait_list))
    del p.wait_list[p.wait_list.index(w)]
    #print(len(p.wait_list))
    queue = reject(queue, w)
    return queue

def penalty_remove_and_reject(queue, w, p):
    #print(len(p.wait_list))
    del p.wait_list[p.wait_list.index(w)]
    #print(len(p.wait_list))
    queue = reject(queue, w)
    return queue


# In[206]:


candidates, programs = algorithm21(candidates, programs)


# ## Algorithm 3

# In[185]:


class Program:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = dict()
        self.min_cutoff = 0
        
    def initialize(self, candidates):
        rand.shuffle(candidates)
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
    
    
class Candidate:
    
    def __init__(self, name, preference_list):
        self.name = name
        self.preference_list = preference_list
        self.i = 0
        self.p = "Leer"
    
    def allocate(self, p):
        self.p = p.name
        
def print_candidates(candidates):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for c in candidates:
        print("********************************** " + c.name + ": " + str(c.p))
        for p in c.preference_list:
            print(p.name)

def print_programs(programs):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for p in programs:
        print("********************************** " + p.name + " " + str(p.capacity) + ": ")
        for c in p.merit_list:
            print(c.name + ": " + str(p.merit_list[c])) 


# In[490]:


def algorithm3(candidates, programs, queue=[], cat_change=[]):
    
    if len(queue) == 0:
        for c in candidates:
            if len(c.preference_list) > 0:
                queue.append(c)
            
    while queue:
        c = queue[0] #Wähle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
        
        #Prüft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Präferenzenliste zu finden)
        if not (c.i < len(c.preference_list) and p == c.preference_list[c.i]) or p.capacity == 0: 
            reject(queue, c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
            
        if len(p.wait_list) > 0:
            y = p.wait_list[-1] #y ist das letzte Element der Warteliste von P
            #Sortierter Schnitt von wait_list und cat_change
            temp = []
            for x in p.wait_list:
                if x in cat_change:
                    temp.append(c)
            if len(temp) > 0:
                w = temp[-1]
            else: 
                w = 0
        else: 
            w = 0
            y = 0
        
        p.wait_list.append(c)
        p.sort_waitlist()     
            
        if len(p.wait_list) <= p.capacity:
            continue
        
        if w == 0 and y != 0:
            if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff:
                if c in cat_change:
                    queue = penalty_remove_and_reject(queue, c, p, cat_change)
            else:
                r = p.sort([c, y])[-1]
                queue = remove_and_reject(queue, r, p, cat_change)
        elif w != 0 and y != 0:
            if y != w:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p, cat_change)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p, cat_change)
                else:
                    r = p.sort([c, y, w])[-1]
                    queue = remove_and_reject(queue, r, p, cat_change)
            else:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p, cat_change)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p, cat_change)
                else:
                    r = p.sort([c, y])[-1]
                    queue = remove_and_reject(queue, r, p, cat_change)
    
    for c in candidates:
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
            if p in c.preference_list:
                c.allocate(p)
        else:
            c.p = 0
    
    return candidates, programs



def reject(queue, c):
    c.i = c.i + 1
    if c.i < len(c.preference_list):
        p = c.preference_list[c.i]
        if p in c.preference_list:
            queue.append(c)
    return queue

def remove_and_reject(queue, w, p, cat_change):
    g = len(p.wait_list)
    rank_w = p.get_rank_of_candidate(w)
    
    #Alle Personen der Liste mit Rank von Kanididat w
    l_candidates = p.get_candidates_with_rank(rank_w)
    l = len(l_candidates)
    
    #Alle Personen, die den Rank von Kandidat w haben und einen Kategoriewechsel vorgenommen haben.
    l1_candidates = []
    for x in l_candidates:
        if x in cat_change:
            l1_candidates.append(c)
    l1 = len(l1_candidates)
    if (g-l) >= p.capacity:
        for x in l_candidates:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
    elif (g-l1) >= p.capacity:
        for x in l1_candidates:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
            
    return queue

def penalty_remove_and_reject(queue, w, p, cat_change):
    l_candidates = p.get_candidates_with_rank(rank_w)
    l = len(l_candidates)
    l1_candidates = []
    for x in l_candidates:
        if x in cat_change:
            l1_candidates.append(c)
    l1 = len(l1_candidates)
    
    print("g-l1: ", g-l1)
    if (g-l1) >= p.capacity: 
        for x in l1_capacity:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
            
    return queue


# ## Generate test data

# In[200]:


programs = []
candidates = []

program_names = ["IMIT", "Informatik", "Wirtschaftsinformatik", "BWL"]
candidate_names = ["Hans", "Peter", "Susan", "Michael", "Christian" , "Kathrin", "Jana", "Lisa", "Mike", "Tarek", "Tjorven"]

for n in program_names:
    programs.append(Program(n, rand.randint(1, 3)))
    
for n in candidate_names:
    candidates.append(Candidate(n, generate_preferences(programs)))

for p in programs:
    p.initialize(candidates)


# In[201]:


candidates, programs = algorithm3(candidates, programs)


# ## Algorithm 4

# In[421]:


def generate_preferences(programs):
    amount = rand.randint(2,4)
    rand.shuffle(programs)
    programs = programs[:amount]
    return programs

def print_candidates(candidates):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for c in candidates:
        print("********************************** " + c.name + ": " + str(c.p))
        for p in c.preference_list:
            print(p.name)

def print_programs(programs):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for p in programs:
        print("********************************** " + p.name + " " + str(p.capacity) + ": ")
        for c in p.merit_list:
            print(c.name) 

class Program:
    
    def __init__(self, name, capacity, allowsfor):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = dict()
        self.min_cutoff = 0
        self.allowsforeign = allowsfor
        
    def initialize(self, candidates):
        rand.shuffle(candidates)
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
        self.name = name
        self.preference_list = preference_list
        self.i = 0
        self.p = "Leer"
        self.isindian = isind
    
    def allocate(self, p):
        self.p = p.name
        
def print_candidates(candidates):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for c in candidates:
        print("********************************** " + c.name + ": ", c.p, "Inder: ", c.isindian)
        for p in c.preference_list:
            print(p.name)

def print_programs(programs):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for p in programs:
        print("********************************** " + p.name + " " + str(p.capacity) + ": ")
        for c in p.merit_list:
            print(c.name + ": " + str(p.merit_list[c])) 


# In[3]:


def algorithm4(candidates, programs, queue=[], cat_change=[]):
    
    if len(queue) == 0:
        for c in candidates:
            if c.isindian:
                if len(c.preference_list) > 0:
                    queue.append(c)
            
    while queue:
        c = queue[0] #Wähle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
        
        #Prüft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Präferenzenliste zu finden)
        if not (c.i < len(c.preference_list) and p == c.preference_list[c.i]) or p.capacity == 0: 
            reject(queue, c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
            
        if len(p.wait_list) > 0:
            y = p.wait_list[-1] #y ist das letzte Element der Warteliste von P
            #Sortierter Schnitt von wait_list und cat_change
            temp = []
            for x in p.wait_list:
                if x in cat_change:
                    temp.append(c)
            if len(temp) > 0:
                w = temp[-1]
            else: 
                w = 0
        else: 
            w = 0
            y = 0
        
        p.wait_list.append(c)
        p.sort_waitlist()     
            
        if len(p.wait_list) <= p.capacity:
            continue
        
        if w == 0 and y != 0:
            if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff:
                if c in cat_change:
                    queue = penalty_remove_and_reject(queue, c, p, cat_change)
            else:
                r = p.sort([c, y])[-1]
                queue = remove_and_reject(queue, r, p, cat_change)
        elif w != 0 and y != 0:
            if y != w:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(y) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p, cat_change)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p, cat_change)
                else:
                    r = p.sort([c, y, w])[-1]
                    queue = remove_and_reject(queue, r, p, cat_change)
            else:
                if p.wait_list.index(c) <= p.min_cutoff and p.wait_list.index(w) <= p.min_cutoff:
                    if c in cat_change:
                        r = p.sort([c, w])[-1]
                        queue = penalty_remove_and_reject(queue, r, p, cat_change)
                    else:
                        queue = penalty_remove_and_reject(queue, w, p, cat_change)
                else:
                    r = p.sort([c, y])[-1]
                    queue = remove_and_reject(queue, r, p, cat_change)
                    
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
                        
    
    for c in candidates:
        if c.i < len(c.preference_list):
            p = c.preference_list[c.i]
            if p in c.preference_list:
                c.allocate(p)
        else:
            c.p = 0
    
    return candidates, programs



def reject(queue, c):
    c.i = c.i + 1
    if c.i < len(c.preference_list):
        p = c.preference_list[c.i]
        if p in c.preference_list:
            queue.append(c)
    return queue

def remove_and_reject(queue, w, p, cat_change):
    g = len(p.wait_list)
    rank_w = p.get_rank_of_candidate(w)
    
    #Alle Personen der Liste mit Rank von Kanididat w
    l_candidates = p.get_candidates_with_rank(rank_w)
    l = len(l_candidates)
    
    #Alle Personen, die den Rank von Kandidat w haben und einen Kategoriewechsel vorgenommen haben.
    l1_candidates = []
    for x in l_candidates:
        if x in cat_change:
            l1_candidates.append(c)
    l1 = len(l1_candidates)
    if (g-l) >= p.capacity:
        for x in l_candidates:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
    elif (g-l1) >= p.capacity:
        for x in l1_candidates:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
            
    return queue

def penalty_remove_and_reject(queue, w, p, cat_change):
    l_candidates = p.get_candidates_with_rank(rank_w)
    l = len(l_candidates)
    l1_candidates = []
    for x in l_candidates:
        if x in cat_change:
            l1_candidates.append(c)
    l1 = len(l1_candidates)
    
    print("g-l1: ", g-l1)
    if (g-l1) >= p.capacity: 
        for x in l1_capacity:
            del p.wait_list[p.wait_list.index(x)]
            queue = reject(queue, x)
            
    return queue


# ## Generate test data

# In[4]:


programs = []
candidates = []

program_names = ["IMIT", "Informatik", "Wirtschaftsinformatik", "BWL"]
candidate_names = ["Hans", "Peter", "Susan", "Michael", "Christian" , "Kathrin", "Jana", "Lisa", "Mike", "Tarek", "Tjorven"]

for n in program_names:
    programs.append(Program(n, rand.randint(1, 1), False))
    
for n in candidate_names:
    candidates.append(Candidate(n, generate_preferences(programs), bool(rand.getrandbits(1))))

for p in programs:
    p.initialize(candidates)


# In[530]:


candidates, programs = algorithm4(candidates, programs)


# In[ ]:


print_programs(programs)


# In[ ]:


print_candidates(candidates)


# # Algorithm 5

# In[301]:




class Program:
    
    def __init__(self, name, capacity, allowsfor, tag):
        self.name = name
        self.capacity = capacity
        self.wait_list = []
        self.merit_list = dict()
        self.min_cutoff = 0
        self.allowsforeign = allowsfor
        self.tag = tag
        
    def initialize(self, candidates):
        temp = dict()
        for x in candidates:
            temp[x] = rand.randint(1,10000)
        self.merit_list = temp.copy()
        
    def generate_submerit(self, merit_list):
        self.merit_list = dict()
        for key, value in merit_list.items():
            if self.tag in key.tag: # Wahr, wenn der Kandidat den Tag hat oder den Tag + den PW-Zusatz hat
                self.merit_list[key] = value
                
        
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
    
    def __init__(self, name, preference_list, isind, tag, isfemale):
        self.name = name
        self.tag = tag
        self.preference_list = preference_list
        self.i = 0
        self.p = "Leer"
        self.isindian = isind
        self.acceptance = 0
        self.isfemale = isfemale
    
    def allocate(self, p):
        self.p = p.name
        
    def update_preferences(self):
        eligible_programs = []
        program_names = []
        for p in self.preference_list:
            program_names.append(p.name)
        program_names = list(dict.fromkeys(program_names))
        print(program_names)
        
        if self.tag == "OPEN-PwD" or self.tag == "OBC-NCL-PwD"  or self.tag == "SC-PwD" or self.tag == "ST-PwD": 
            for p in programs:
                if p.tag == self.tag or p.tag == "OPEN-PwD" or p.tag == "OPEN":
                    eligible_programs.append(p)
        else:
            for p in programs:
                if p.tag == self.tag or p.tag == "OPEN":
                    eligible_programs.append(p)

        amount = len(program_names)
        program_names = program_names[:amount]
        preferences = []
        for n in program_names:
            for q in eligible_programs:
                if n == q.name:
                    preferences.append(q)
                    
        self.preference_list = preferences


# ## Generate test data

# In[359]:


def print_candidates(candidates):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for c in candidates:
        print("********************************** " + c.name + ": ", c.p, "Inder: " + str(c.isindian) + " " + str(c.tag) + " Weiblich: " + str(c.isfemale))
        for p in c.preference_list:
            print(p.name + " " + p.tag)

def print_programs(programs):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for p in programs:
        print("********************************** " + p.name + " " + str(p.capacity) + ": ")
        for c in p.merit_list:
            print(c.name + ": " + str(p.merit_list[c])) 
            

def generate_virtual_programs(program_names, virtual_names):
    programs = []

    capacity = rand.randint(400,450)
    
    female_only = int(capacity * 0.2)
    capacity = capacity - female_only
    
    ob = int(capacity*0.27)
    sc = int(capacity*0.15)
    st = int(capacity*0.075)
    op = capacity-ob-sc-st
    oppw = int(op*0.03)
    op = op-oppw
    obpw = int(ob*0.03)
    ob = ob-obpw
    scpw = int(sc*0.03)
    sc = sc-scpw
    stpw = int(st*0.03)
    st = st-stpw
    
    virtual_sizes = dict()
    virtual_sizes[0] = female_only
    virtual_sizes[1] = op
    virtual_sizes[2] = ob
    virtual_sizes[3] = sc
    virtual_sizes[4] = st
    virtual_sizes[5] = oppw
    virtual_sizes[6] = obpw
    virtual_sizes[7] = scpw
    virtual_sizes[8] = stpw
    
    for n in program_names:
        for i in range(len(virtual_names)):
            programs.append(Program(n, virtual_sizes[i], True, virtual_names[i]))

    return programs

def generate_preferences(program_names, programs, tag, virtual_names, isfemale):
    eligible_programs = []
    if isfemale:
        if tag == "OPEN-PwD" or tag == "OBC-NCL-PwD"  or tag == "SC-PwD" or tag == "ST-PwD": 
            for p in programs:
                if p.tag == tag or p.tag == "OPEN-PwD" or p.tag == "OPEN" or p.tag == "FEM":
                    eligible_programs.append(p)
        else:
            for p in programs:
                if p.tag == tag or p.tag == "OPEN" or p.tag == "FEM":
                    eligible_programs.append(p)
    else: 
        if tag == "OPEN-PwD" or tag == "OBC-NCL-PwD"  or tag == "SC-PwD" or tag == "ST-PwD": 
            for p in programs:
                if p.tag == tag or p.tag == "OPEN-PwD" or p.tag == "OPEN":
                    eligible_programs.append(p)
        else:
            for p in programs:
                if p.tag == tag or p.tag == "OPEN":
                    eligible_programs.append(p)
                
    amount = rand.randint(2,len(program_names))
    rand.shuffle(program_names)
    program_names = program_names[:amount]
    preferences = []
    for n in program_names:
        for q in eligible_programs:
            if n == q.name:
                preferences.append(q)
    return preferences

def prepare_next_round(candidates, programs):
    #Bestimme den Status des Akzeptanz durch den Kandidaten
    #0: Kandidat hat keinen Platz, 1: Reject, 2: Freeze, 3: Float
    for c in candidates:
        if len(c.preference_list) > 0:
            if c.preference_list[0].name == c.p:
                c.acceptance = 2 # Freeze
            elif c.p == "Leer":
                c.acceptance = 0 # hat noch keinen Platz
            else: 
                c.acceptance = 3 # Float
            
    reject = rand.sample(candidates, int(len(candidates)*0.10))
    for p in programs:
        p.wait_list = list(set(p.wait_list) - set(reject))
    for c in candidates:
        if c in reject:
            c.acceptance = 1
            c.p = "Leer" 
            c.preference_list = []
        elif c.acceptance == 2: #Freeze
            choice = []
            for p in c.preference_list:
                if p.name == c.p:
                    choice.append(c.preference_list[c.preference_list.index(p)])
            c.preference_list = choice
    
    
    #min_cutoff berechnen
    for p in programs:
        if len(p.wait_list) > 0:
                p.min_cutoff = p.get_rank_of_candidate(p.wait_list[-1])
        
        
    #Dereservation der freien Plätze
    for p in programs:
        if p.tag == "OBC-NCL":
            if len(p.wait_list) < p.capacity:
                for q in programs:
                    if q.name == p.name and q.tag == "OPEN":
                        free_space = p.capacity - len(p.wait_list)
                        q.capacity = q.capacity + free_space
                        p.capacity = len(p.wait_list)
                for q in programs:
                    if q.tag == "OBC-NCL-PwD":
                        if len(q.wait_list) < q.capacity:
                             for r in programs:
                                if r.name == q.name and r.tag == "OPEN":
                                    free_space = q.capacity - len(q.wait_list)
                                    r.capacity = r.capacity + free_space
                                    q.capacity = len(p.wait_list)
            else:
                for q in programs:
                    if q.tag == "OBC-NCL-PwD":
                        if len(q.wait_list) < q.capacity:
                             for r in programs:
                                if r.name == q.name and r.tag == "OBC-NCL":
                                    free_space = q.capacity - len(q.wait_list)
                                    r.capacity = r.capacity + free_space
                                    q.capacity = len(p.wait_list)
                                    
        elif p.tag == "SC-PwD":
            if len(p.wait_list) < p.capacity:
                for q in programs:
                    if q.name == p.name and q.tag == "SC":
                        free_space = p.capacity - len(p.wait_list)
                        q.capacity = q.capacity + free_space
                        p.capacity = len(p.wait_list)
                        
        elif p.tag == "ST-PwD":
            if len(p.wait_list) < p.capacity:
                for q in programs:
                    if q.name == p.name and q.tag == "ST": 
                        free_space = p.capacity - len(p.wait_list)
                        q.capacity = q.capacity + free_space
                        p.capacity = len(p.wait_list)
                        
                        
    #Aendere die Kategorie einiger Kandidaten zufällig, sagen wir von 3%
    cat_change = rand.sample(candidates, int(len(candidates)*0.03))
    for c in cat_change:
        c.tag = virtual_names[rand.randint(0,7)+1]
        c.update_preferences()
            
    return candidates, programs, cat_change


# In[348]:


programs = []
candidates = []

virtual_names = dict()
virtual_names[0] = "FEM"
virtual_names[1] = "OPEN"
virtual_names[2] = "OBC-NCL"
virtual_names[3] = "SC"
virtual_names[4] = "ST"
virtual_names[5] = "OPEN-PwD"
virtual_names[6] = "OBC-NCL-PwD"
virtual_names[7] = "SC-PwD"
virtual_names[8] = "ST-PwD"


program_names = ["IMIT", "Informatik", "Wirtschaftsinformatik", "BWL"]
programs = generate_virtual_programs(program_names, virtual_names)
    
candidate_names = ["Hans", "Peter", "Susan", "Michael", "Christian" , "Kathrin", "Jana", "Lisa", "Mike", "Tarek", "Tjorven"]
candidate_names = []
for i in range(2000):
    name = str(i)
    candidate_names.append(name)
    
for n in candidate_names:
    tag = virtual_names[rand.randint(0,7) + 1]
    isfemale = rand.randint(1, 100) < 30
    candidates.append(Candidate(n, generate_preferences(program_names, programs, tag, virtual_names, isfemale), True, tag, isfemale))

for n in program_names:
    openp = programs[0]
    for p in programs:
        if p.tag == "OPEN" and p.name == n:
            p.initialize(candidates)
            openp = p
    for p in programs:
        if p.tag != "OPEN" and p.name == n:
            p.merit_list = openp.merit_list


# In[349]:


candidates, programs = algorithm4(candidates, programs)


# In[350]:


print_programs(programs)


# In[351]:


print_candidates(candidates)


# In[352]:


candidates, programs, cat_change = prepare_next_round(candidates, programs)
print(len(candidates))


# In[353]:


candidates, programs = algorithm4(candidates, programs)


# In[354]:


for c in cat_change:
    print(c.name, c.tag)


# In[355]:


print_candidates(candidates)


# In[356]:


print(candidates[61].name)
c = candidates[61]
for p in c.preference_list:
    print(p.name, p.tag)
print(c.acceptance)


# In[357]:


candidates, programs, cat_change = prepare_next_round(candidates, programs)
candidates, programs = algorithm4(candidates, programs)
for c in cat_change:
    print(c.name, c.tag)
print(len(candidates))


# In[358]:


candidates, programs, cat_change = prepare_next_round(candidates, programs)
candidates, programs = algorithm4(candidates, programs)
for c in cat_change:
    print(c.name, c.tag)
print(len(candidates))


# In[ ]:





# In[ ]:



