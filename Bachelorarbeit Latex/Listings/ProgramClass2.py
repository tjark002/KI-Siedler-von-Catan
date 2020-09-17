class Program:
  
    def __init__(self, name, capacity):
        ...
        self.min_cutoff = 0

def remove_and_reject(queue, w, p):
    del p.wait_list[p.wait_list.index(w)]
    queue = reject(queue, w)
    return queue

def penalty_remove_and_reject(queue, w, p):
    del p.wait_list[p.wait_list.index(w)]
    queue = reject(queue, w)
    return queue