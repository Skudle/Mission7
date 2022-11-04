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

print(get_words("The bana.na i;s :  yellow,"))


def readfile ( filename ):
    line = []
    with open(filename, 'r') as f:
        for i in f.readlines():
            line.append(i)
        f.close()
        return line

print(readfile('test.txt'))

#def create_index ( filename ):


      