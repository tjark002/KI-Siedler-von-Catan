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