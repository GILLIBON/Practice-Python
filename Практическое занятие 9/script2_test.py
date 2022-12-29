from script2 import pass_check

def test_pass_less_than_6():
    assert pass_check('abc12') == False

def test_pass_not_contains_num():
    assert pass_check('abcdef') == False

def test_pass_not_containt_lett():
    assert pass_check('123456') == False

def test_pass_not_containt_password():
    assert pass_check('123paSSwoRd23Alpha') == False