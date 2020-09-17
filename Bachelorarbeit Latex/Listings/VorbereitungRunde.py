def prepare_next_round(candidates, programs):
    #Bestimme den Status der Akzeptanz durch den Kandidaten
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
                        
                        
    #Ändere die Kategorie einiger Kandidaten zufällig, sagen wir von 3%
    cat_change = rand.sample(candidates, int(len(candidates)*0.03))
    for c in cat_change:
        c.tag = virtual_names[rand.randint(0,7)+1]
        c.update_preferences()
            
    return candidates, programs, cat_change