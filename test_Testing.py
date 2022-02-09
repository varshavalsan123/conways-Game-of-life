import life 

F = False
T = True

def test_life_grid_no_input():
    res = [[F, F, F,F],[ F, F,F, F],[ F,F, F, F],[F, F, F,F]]
    assert  res == life.view_matrix([])
    
def test_life_grid_input():
    res = [[F, T, F,T],[ F, T,F, F],[ F,F, F, F],[F, F, F,F]]
    assert res == life.view_matrix([1,3,5]) 

def test_life_grid_repeat_input():
    res = [[F, T, F,T],[ F, T,F, F],[ F,F, F, F],[F, F, F,F]]
    assert res == life.view_matrix([1,3,5,1])


def test_position_of_T_multiple(): 
    res = [[0,0],[0,2],[2,1]]
    assert res == life.position( [[ T, F,T, F],[ F,F, F, F],[ F, T, F, F],[F, F, F,F]])


def test_neighbour_nil():
    neighbours, neighbour_F = life.neighbour_check( [[ T, F,T, F],[ F,F, F, F],
                                        [ F, T, F, F],
                                        [F, F, F,F]], [0,0])
    assert neighbours == 0
    assert  neighbour_F == [[0,1],[1,0],[1,1]]

def test_neighbours_three():
   neighbours, F_nb = life.neighbour_check( [[ T, F,T, F],[ F,T, F, F],
                                        [ F, T, F, F],
                                        [F, F, F,F]], [1,1])
   assert neighbours == 3
   assert  F_nb == [[0,1],[1,0],[1,2],[2,0],[2,2]]

def test_no_change_in_gen():
    res = [[ T, T, F, F],[ T,T, F, F],[ F, F, F, F],[F, F, F,F]]
    assert res == life.change_generation( [[ T, T, F, F],[ T,T, F, F],[ F, F, F, F],[F, F, F,F]])
   
def test_change_in_gen():
    assert life.change_generation( [[ F, F, F, F],
                               [ T,T, T, F],
                               [ F, F, F, F],
                               [F, F, F,F]]) == [[  F, T, F, F],
                               [ F,T, F, F],
                               [ F, T, F, F],
                               [F, F, F,F]]

def test_view_no_T():
    res = [[ F, F, F, F],[ F, F, F, F],[ F, F, F, F],[ F, F, F, F]]
    assert res == life.view_matrix([[ F, F, F, F]*4]*4)
