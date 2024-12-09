import y2024day09 as advent


def test_filesystem():
    input = '123'

    assert advent.construct_filesystem(input) == ['0','.','.','1','1','1']

def test_solve_example():
    input = '2333133121414131402'
    assert advent.solve_puzzle(input) == 1928