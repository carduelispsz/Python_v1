from Zjazd4.mathematica.algebra import matrices

def test_adder():
    mat1 = [[1,1,1],[1,1,1]]
    mat2 = [[2,2,2],[2,2,2]]
    dodane = matrices.add_matrices(mat1, mat2)
    assert dodane == [[3, 3, 3], [3, 3, 3]]

def test_substr():
    mat1 = [[1,1,1],[1,1,1]]
    mat2 = [[2,2,2],[2,2,2]]
    odjete = matrices.substract_matrices(mat1, mat2)
    assert odjete == [[-1,-1,-1], [-1,-1,-1]]