from calculate_grades import calculate_stat

def test_calculate_stat():
    grade_list = [12,23,25,33,45]
    assert calculate_stat(grade_list) == (27.6, 10.983624174196784)

def test_calculate_stat_empty_list():
    grade_list = []
    assert calculate_stat(grade_list) == (0, 0)

def test_calculate_stat_full_of_zeros():
    grade_list = [0, 0, 0, 0]
    assert calculate_stat(grade_list) == (0, 0)