import search

def test_get_words():
    assert search.get_words ( "Turmoil has engulfed the Galactic Republic." ) == ['turmoil', 'has', 'engulfed', 'the', 'galactic', 'republic']
def test_readfile():
    assert search.readfile ('text_example_1.txt') == ['While the Congress of the Republic endlessly debates', 'this alarming chain of events, the Supreme Chancellor has', 'secretly dispatched two Jedi Knights.']
def test_create_index():
    assert search.create_index ('PythonSecretCode.txt') == "Fichier inexistant"
    assert search.create_index ('text_example_1.txt') == {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [0], 'debates': [0], 'this': [1], 'alarming': [1], 'chain': [1], 'events': [1], 'supreme': [1], 'chancellor': [1], 'has': [1], 'secretly': [2], 'dispatched': [2], 'two': [2], 'jedi': [2], 'knights': [2]}
def test_get_lines():
    assert search.get_lines(['while'], {"while": [0], "the": [0,1], "congress": [0], "of": [0,1], "republic": [0] , "jedi": [2],}) == [0]
    assert search.get_lines(['used', 'bullseye'], search.create_index('episodeIV_dialogue.txt')) == [808]
    assert search.get_lines(['Python'], search.create_index('episodeIV_dialogue.txt')) == []
    assert search.get_lines(['used'], search.create_index('PythonSecretCode.txt')) == "Le fichier n'existe pas"
    
    print('Passed')
test_get_words ()
test_readfile()
test_create_index()
test_get_lines()