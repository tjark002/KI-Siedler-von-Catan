for n in program_names:
    openp = programs[0]
    for p in programs:
        if p.tag == "OPEN" and p.name == n:
            p.initialize(candidates)
            openp = p
    for p in programs:
        if p.tag != "OPEN" and p.name == n:
            p.merit_list = openp.merit_list