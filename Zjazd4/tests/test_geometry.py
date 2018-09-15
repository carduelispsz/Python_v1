from mathematica.geometry import figures

def test_squarearea():
    square = figures.square_area(5)
    assert square == 25

def test_trianglearea():
    tri = figures.triangle_area(2,3)
    assert tri == 3