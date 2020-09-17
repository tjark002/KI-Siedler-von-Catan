def algorithm2(candidates, programs, queue=[], cat_change=[]):      
    ...            
        ...        
        if not (c.i < len(c.preference_list) and p == c.preference_list[c.i]) or p.capacity == 0: 
            reject(queue, c)
            continue
            
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
    ...   
    return candidates, programs