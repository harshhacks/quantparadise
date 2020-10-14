from VR import Mod6 as md

# class TestClass:


def test_first():
    assert md.zero_coupon(1, 2, 3, 4, 5, model="abcd") == -1

        
def test_second():
    assert md.swapRates([1], 2, 3) == -1

        
def test_third():
    assert md.liborRates([1], 2, 3) == -1
    

def test_fourth():
    assert md.objFunc1([1, 2, 3, -8], 5, 6, 2 , model="abcd") == -2

    
def test_fifth():
    assert md.objFunc1([-1, 2, 3, 4], 2, 3, 4, model="ac") == -1
        
