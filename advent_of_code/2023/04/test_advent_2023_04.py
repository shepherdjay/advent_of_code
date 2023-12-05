from advent_2023_04 import update_for_matches

def test_update_for_matches():
    current_list = [1, 2, 3 ,4, 5]
    idx = 1
    matches = 2

    update_for_matches(idx, matches, current_list)
    assert current_list == [1, 2, 3, 3, 4, 4, 5]