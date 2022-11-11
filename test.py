import search

def test_get_words():
    assert search.get_words ( "Turmoil has engulfed the Galactic Republic." ) == ['turmoil', 'has', 'engulfed', 'the', 'galactic', 'republic']
    print('Test 1 passed')
def test_readfile():
    assert search.readfile ('test.txt') == ['While the Congress of the Republic endlessly debates\n', 'this alarming chain of events, the Supreme Chancellor has\n', 'secretly dispatched two Jedi Knights.']
    print('Test 2 passed')
def test_create_index():
    assert search.create_index ('test.txt') == {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [0], 'debates': [0], 'this': [1], 'alarming': [1], 'chain': [1], 'events': [1], 'supreme': [1], 'chancellor': [1], 'has': [1], 'secretly': [2], 'dispatched': [2], 'two': [2], 'jedi': [2], 'knights': [2]}
    print('Test 3 passed')
def test_get_lines():
    assert search.get_lines(['while'], {"while": [0], "the": [0,1], "congress": [0], "of": [0,1], "republic": [0] , "jedi": [2],}) == [0]
    print('Test 4 passed')
test_get_words ()
test_readfile()
test_create_index()
test_get_lines()