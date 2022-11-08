def convert(args):
    if args.isnumeric():
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
                if i == len(data)-2:
                    treatment += convert(data[i]) + str(counter)
                    treatment += ' '
            elif (len(data)-1) - (i+1) == 1:
                convert(len(data) - 1)
                treatment += x + str(counter)
                return treatment
            else:
                treatment += convert(data[i]) + str(counter)
                treatment += ' '
                counter = 1
            
                
                
    return treatment


print(treatment('ppayyyyy'))

        