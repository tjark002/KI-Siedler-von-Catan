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