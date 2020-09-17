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