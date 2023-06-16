with open('my_file.txt','r') as file:
    #print(file.readlines())
    c = 0
    for a in file:
        for b in a:
            #print(b)
            if b == '1':
                c += 1
    print(c)
