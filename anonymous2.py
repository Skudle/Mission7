def convert(args):
    if str(args).isnumeric():
            return 'number*'
    elif args[0].lower() in 'aueioy':
        if args[0].isupper():
            return 'vowel-up*'
        else:
            return 'vowel-low*'
    else:   
        if args[0].islower():
            return 'consonant-low*'
        else:
            return 'consonant-up*'
def treatment(data):
    counter = 1
    treatment = ""
    if len(data) == 1:
        x = convert(data)
        treatment += x + str(counter)
        return treatment
        
    else:
        for i in range (len(data)-1):
            if convert(data[i]) == convert(data[i+1]):
                counter+=1
                #Probleme: sort de la boucle avant d'additioner dans treatment quand i atteint la valeur max
                
            else:
                treatment += convert(data[i]) + str(counter)
                treatment += ' '
                counter = 1
                if i == (len(data)-2):
                    x = convert(data[-1])
                    treatment += x + str(counter)
                    
            
                
                
    return treatment


print(treatment('78huy'))

        