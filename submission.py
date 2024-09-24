from search_algorithms import *
from mars_planner import *
from adjacency import *
from routefinder import *


if __name__=="__main__" :
    s = RoverState()

    breadth_first_search(s, action_list, mission_complete)
    depth_first_search(s, action_list, mission_complete)
    depth_first_search(s, action_list, mission_complete, limit=9)
    depth_first_search(s, action_list, mission_complete, limit=5)
    iterative_deepening_search(s, action_list, mission_complete)

    file = '/home/nssteaderman/assignment-2-search-noah-22203/Graph.txt'
    graph = read_mars_graph(file)  
    test_state= map_state()
    test_state.location = "3,6"
    test_state.mars_graph = graph
    
    a_star(test_state, sld, map_state.is_goal)
    a_star(test_state, h1, map_state.is_goal)

    print("\nadjacency problem:\n")
    solve_adjacency()