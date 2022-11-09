def carabosse(s):
    state = True
    lc = 0
    if (len(s)) == 0:
        return 'Erreur 0'
    for o in range (len(s)):
        if s[0] == '*':
            continue
        elif o == (len(s)):
            if s[o] == 'x':
                return 'Erreur 1'
            
        else:
            break
    else:
        last_carac = s[-1]
        x = -1
        while state:
            if last_carac != '*':
                state = False
            else:
                x = x-1
                last_carac = s[x]
        for i in range (len(s)):
            c = ""
            if s[i] != "*":
                c += s[i]
            else:
                c += last_carac
        return c
print(carabosse("Bonj*ouro"))