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
    g = len(p.wait_list)
    rank_w = p.get_rank_of_candidate(w)
    
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