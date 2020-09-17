    #min_cutoff berechnen
    for p in programs:
        if len(p.wait_list) > 0:
                p.min_cutoff = p.get_rank_of_candidate(p.wait_list[-1])