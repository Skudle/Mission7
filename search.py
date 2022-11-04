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
        f.close()
        return line

def create_index ( filename ):
  dico = {
  }
  list = []
  with open(filename, 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        list.append(line)
    
    for l in range (len(list)):
        for lil in list[l]:
            if lil not in dico:
                dico[lil] = [l]
            else:
                if dico[lil] == [l]:
                    pass
                else:
                    dico[lil].append(l)
        
    return dico



      