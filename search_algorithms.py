from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_counter = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"Total number of states: {state_counter}")
            return next_state[0]
        else :
            successors = next_state[0].successors(action_list)
            state_counter += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    
    

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=None) :
    search_queue = deque()
    closed_list = {}
    state_counter = 0
    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0:
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        path = next_state[0]
        count = -1 #made this -1 so that limit can be set to the optimal number of actions performed
        while path is not None : # get full path with all actions, limit the depth(actions performed)
            path = path.prev
            count += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"Total number of states: {state_counter}")
            return next_state[0]
        elif limit == None or count < limit:
            successors = next_state[0].successors(action_list)
            state_counter += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    print(f"Total number of states visited: {state_counter}")
    return next_state[0]

## add iterative deepening search here
def iterative_deepening_search(startState, action_list, goal_test, use_closed_list=True):
    depth = 0
    total_states = 0
    done = False
    while True :
        limit = depth
        search_queue = deque()
        closed_list = {}
        state_counter = 0
        search_queue.append((startState,""))
        if use_closed_list :
            closed_list[startState] = True
        while len(search_queue) > 0:
            ## this is a (state, "action") tuple
            next_state = search_queue.pop()
            path = next_state[0]
            count = -1 #made this -1 so that limit can be set to the optimal number of actions performed
            while path is not None : # get full path with all actions, limit the depth(actions performed)
                path = path.prev
                count += 1
            if goal_test(next_state[0]):
                ptr = next_state[0]
                while ptr is not None :
                    ptr = ptr.prev
                    print(ptr)
                print(f"Total number of states: {total_states + state_counter}")
                done = True
                return next_state
            elif limit == None or count < limit:
                successors = next_state[0].successors(action_list)
                state_counter += len(successors)
                if use_closed_list :
                    successors = [item for item in successors
                                        if item[0] not in closed_list]
                    for s in successors :
                        closed_list[s[0]] = True
                search_queue.extend(successors)
        depth += 1
        total_states += state_counter
        