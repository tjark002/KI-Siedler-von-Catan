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