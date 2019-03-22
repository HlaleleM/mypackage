from recursion import myFunction

def test_sum_array():
    """
    make sure top_n works correctly
    """
    assert myFunction.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert myFunction.sum_array([10, 1, 12, 9, 2]) == 34 , 'incorrect'
    assert myFunction.sum_array([1, 2, 3, 4, 5]) == 15, 'incorrect'

def test_fibonacci():
    assert myFunction.fibonacci(0) == 0, 'incorrect'
    assert myFunction.fibonacci(1) == 1, 'incorrect'
    assert myFunction.fibonacci(4) == 3, 'incorrect'

def test_factorial() :
    assert.myFunction.factorial(0) ==1, 'incorrect'
    assert.myFunction.factorial(2) ==2, 'incorrect'
    assert.myFunction.factorial(3) ==6, 'incorrect'

def test_reverse():
    assert.myFunction.reverse('EDSA') == 'ASDE', 'incorrect'
    assert.myFunction.reverse('hlalele') == 'elelalh', 'incorrect'
    assert.myFunction.reverse('power') == 'rewop', 'incorrect'

from sorting import myFunction
def test_bubble_sort():
    assert.myFunction.bubble_sort(['E','D','S','A']) == ['A','D','E','S'],'incorrect'
    assert.myFunction.bubble_sort([4,-1,0,20,0]) == [-1,0,0,4,20],'incorrect'
    assert.myFunction.bubble_sort([3,7,2,3,1]) == [1,2,3,3,7],'incorrect'

def test_merge_sort():
    assert.myFunction.merge_sort(['E','D','S','A']) == ['A','D','E','S'],'incorrect'
    assert.myFunction.merge_sort([4,-1,0,20,0]) == [-1,0,0,4,20],'incorrect'
    assert.myFunction.merge_sort([3,7,2,3,1]) == [1,2,3,3,7],'incorrect'

def test_quick_sort():
    assert.myFunction.quick_sort(['E','D','S','A']) == ['A','D','E','S'],'incorrect'
    assert.myFunction.quick_sort([4,-1,0,20,0]) == [-1,0,0,4,20],'incorrect'
    assert.myFunction.quick_sort([3,7,2,3,1]) == [1,2,3,3,7],'incorrect'
