import script1

def test_r_is_zero():
    assert script1.area_of_circle(0) == 'Радиус должен быть больше нуля.'

def test_r_is_below_zero():
    assert script1.area_of_circle(-1) == 'Радиус должен быть больше нуля.'

def test_r_is_str():
    assert script1.area_of_circle('1') == 'Радиус должен быть числом.'

def test_r_is_float():
    assert script1.area_of_circle(0.1) == 0.031415926535897934