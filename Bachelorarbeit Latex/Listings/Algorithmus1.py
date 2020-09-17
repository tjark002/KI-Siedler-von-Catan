def algorithm1(candidates, programs):
    queue = []

    for p in programs:
        p.wait_list = []
        
    for c in candidates:
        if len(c.preference_list) > 0:
            queue.append(c)
        
    while queue:
        c = queue[0] #Waehle den ersten Kandidaten in der Liste
        del queue[0] #Und entferne ihn
        p = c.preference_list[c.i]
        
        #Prueft ob ein Kandidat geeignet ist (hier: Programm ist an Stelle i auf der Praeferenzenliste zu finden (Redundant))
        if not p == c.preference_list[c.i]: 
            reject(c)
            continue #Wenn er nicht geeignet ist, wird der nächste Kandidat bearbeitet
        
        #Wenn er geeignet ist, wird er einsortiert
        if len(p.wait_list) == p.capacity:
            lastc = p.wait_list[-1] #Das letzte Element der der Warteliste zwischenspeichern
            
            #Wenn der neue Kandidat besser als der auf dem letzten Platz ist, ersetzt er ihn
            if p.merit_list.index(lastc) > p.merit_list.index(c): 
                p.wait_list[-1] = c
                reject(queue, lastc)
                p.sort_waitlist() #Sorgt dafuer, dass die Warteliste sortiert bleibt
            else:
                reject(queue, c)
                
        else:
            p.wait_list.append(c)
            p.sort_waitlist() #Sorgt dafuer, dass die Warteliste sortiert bleibt
    
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