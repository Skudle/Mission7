def get_words ( line ):
    """Transforms a phrase into a list without special symbols
    
    Args: a string
    
    returns: a list of strings"""
    
    word_list = []
    for w in line.split():
      word=''
      for c in w:
        if c.isalpha():
          word = word+c.lower()
      if len(word)>0:
        word_list.append(word)
    return word_list


def readfile ( filename ):
    """opens a file and read it line by line
    Args: a string
    
    returns: a list of string"""
    
    line = []
    with open(filename, 'r') as f:
        for i in f.readlines():
            line.append(i)
        return line

def create_index ( filename ):
    """create index for words and put them in the dictionary
    Args: a string
    returns: a dictionary
    """
    dico ={
    }
    list = readfile(filename)
    for l in range (len(list)):
        lil = get_words(list[l])
        for i in range (len(lil)):
            if lil[i] not in dico:
                dico[lil[i]] = [l]
            else:
                if dico[lil[i]] == [l]:
                    pass
                else:
                    dico[lil[i]].append(l)
        
    return dico

print(create_index('test.txt'))