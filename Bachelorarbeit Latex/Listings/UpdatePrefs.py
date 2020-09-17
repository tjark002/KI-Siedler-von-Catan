def update_preferences(self):
    ...
    program_names = []
    for p in self.preference_list:
        program_names.append(p.name)
    program_names = list(dict.fromkeys(program_names))
    ...

    amount = len(program_names)
    program_names = program_names[:amount]
    #rand.shuffle(program_names)
    preferences = []
    for n in program_names:
        for q in eligible_programs:
            if n == q.name:
                preferences.append(q)
                    
    self.preference_list = preferences