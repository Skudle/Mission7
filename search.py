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
    try:
        with open(filename, 'r') as f:
            for s in f:
                line.append(s.replace("\n", ""))
            return line
    except FileNotFoundError:
        return "Fichier inexistant"



def create_index ( filename ):
    """create index for words and put them in the dictionary
    Args: a string
    returns: a dictionary
    """
    dico ={
    }
    list = readfile(filename)
    if list == "Fichier inexistant":
        return "Fichier inexistant"
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

def get_lines ( words, index ):
    list2 = []
    list3 = []
    for o in words:
        try:
            list2.append(index[o])
        except KeyError:
            list2 = []
            return list2
        except TypeError:
            return "Le fichier n'existe pas"
            
    same = all(element == list2[0] for element in list2)
    if same:
        return list2[0]

    else:
        result = set(list2[0])
        for s in list2[1:]:
            result.intersection_update(s)
        list3.append((list(result)))
        flat_list = [ item for elem in list3 for item in elem]
        return flat_list

print(get_lines(['used'], create_index('PythonSecretCode.txt')))
