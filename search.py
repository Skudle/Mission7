def get_words ( line ):
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
    line = []
    with open(filename, 'r') as f:
        for i in f.readlines():
            line.append(i)
        return line

def create_index ( filename ):
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