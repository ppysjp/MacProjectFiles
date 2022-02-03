# https://realpython.com/python-testing/
 
def test_sum():
    assert sum([1 , 2, 3]) == 6, "Should be six"

def test_sum_tuple():
    assert sum((1 , 2, 3)) == 6, "Should be six"


if __name__ =="__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed!")
