import shape_math

def test_squaring_number():
    assert shape_math.square(5) == 25
    assert shape_math.square(-3) == 9
    assert shape_math.square(10) == 100

# calculate the area of a triangle
def test_area_of_triangle():
    assert shape_math.area_of_triangle(10, 5) == 25  # (base * height) / 2
    assert shape_math.area_of_triangle(8, 6) == 24
    assert shape_math.area_of_triangle(7, 3) == 10.5

# calculate the area of a trapezoid
def test_area_of_trapezoid():
    assert shape_math.area_of_trapezoid(10, 6, 4) == 32  # ((base1 + base2) / 2) * height
    assert shape_math.area_of_trapezoid(8, 4, 3) == 18
    assert shape_math.area_of_trapezoid(7, 5, 2) == 12

# calculate the surface area of a cylinder
def test_surface_area_of_cylinder():
    assert round(shape_math.surface_area_of_cylinder(7, 10), 2) == 747.7  # Rounded to 2 decimal places
    assert round(shape_math.surface_area_of_cylinder(5, 12), 2) == 534.07  
    assert round(shape_math.surface_area_of_cylinder(3, 8), 2) == 207.35  

# calculate the surface area of a sphere
def test_surface_area_of_sphere():
    assert round(shape_math.surface_area_of_sphere(7), 2) == 615.75  # Rounded to 2 decimal places
    assert round(shape_math.surface_area_of_sphere(5), 2) == 314.16  
    assert round(shape_math.surface_area_of_sphere(3), 2) == 113.10  

# calculate the volume of a cube
def test_volume_of_cube():
    assert shape_math.volume_of_cube(3) == 27  # side^3
    assert shape_math.volume_of_cube(4) == 64
    assert shape_math.volume_of_cube(5) == 125

# calculate the volume of a cone
def test_volume_of_cone():
    assert round(shape_math.volume_of_cone(3, 9), 2) == 84.82  # Rounded to 2 decimal places
    assert round(shape_math.volume_of_cone(5, 12), 2) == 314.16  
    assert round(shape_math.volume_of_cone(7, 10), 2) == 513.13  

# calculate the volume of a sphere
def test_volume_of_sphere():
    assert round(shape_math.volume_of_sphere(3), 2) == 113.10  # Rounded to 2 decimal places
    assert round(shape_math.volume_of_sphere(5), 2) == 523.6  
    assert round(shape_math.volume_of_sphere(7), 2) == 1436.76  
