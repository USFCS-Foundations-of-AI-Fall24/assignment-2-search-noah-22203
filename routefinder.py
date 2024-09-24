from queue import PriorityQueue
import math
from Graph import *

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    state_counter = 0
    m_graph = start_state.mars_graph

    if use_closed_list:
        closed_list[start_state] = True

    while not search_queue.empty():
        next_state = search_queue.get()   # I got all of this from the other search methods
        if goal_test(next_state):
            print("Goal found")
            print(next_state)
            ptr = next_state.prev_state  
            while ptr is not None:
                print(ptr)
                ptr = ptr.prev_state
            print(f"Total number of states: {state_counter}")
            return next_state  
        else:
            new_node = Node(next_state.location)
            edges = next_state.mars_graph.get_edges(new_node) #gets edges
            
            if edges is None:  #this may not be necessary anymore but it fixed a bug I was having earlier so I left it in.
                edges = []  
            successors = []
            
            for edge in edges: 
                new_state = map_state(location=edge.dest, mars_graph=m_graph, prev_state=next_state)

                new_state.g = next_state.g + edge.val #increment cost so far
                new_state.h = heuristic_fn(new_state) #recalculate cost to goal
                new_state.f = new_state.g + new_state.h #total cost

                successors.append(new_state)

            state_counter += len(successors) #increment states
           
            if use_closed_list:
                successors = [item for item in successors if item not in closed_list]
                for s in successors:
                    closed_list[s] = True
            for s in successors: #because priority queue does not have "extend"
                search_queue.put(s)

    print(f"Total number of states visited: {state_counter}")
    return next_state


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    loc = state.location.split(",")
    x = int(loc[0])
    y = int(loc[1])
    return math.sqrt((x-1) ** 2 + (y-1) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    m_graph = Graph() 
    with open(filename, 'r') as file:
       
        for line in file:  # I used some chatGPT here to make my solution much more compact and look nicer(less repetative)
            nodes, neighbor_str = line.strip().split(":")
            neighbors = neighbor_str.split()
            node = Node(nodes)
            edges = [Edge(node, neighbor, 1) for neighbor in neighbors]
            m_graph.add_node(node)
            
            for edge in edges:
                m_graph.add_edge(edge)
    
    return m_graph


if __name__=="__main__" :
    file = '/home/nssteaderman/assignment-2-search-noah-22203/Graph.txt'
    
    graph = read_mars_graph(file)  
    test_state= map_state()
    test_state.location = "3,6"
    test_state.mars_graph = graph
    
    
    a_star(test_state, sld, map_state.is_goal)
    a_star(test_state, h1, map_state.is_goal)
