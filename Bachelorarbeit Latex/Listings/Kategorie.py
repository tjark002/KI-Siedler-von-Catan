    #Aendere die Kategorie einiger Kandidaten zufällig, sagen wir von 3%
    cat_change = rand.sample(candidates, int(len(candidates)*0.03))
    for c in cat_change:
        c.tag = virtual_names[rand.randint(0,7)+1]
        c.update_preferences()
            
    return candidates, programs, cat_change