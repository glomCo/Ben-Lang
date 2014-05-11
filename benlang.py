var = {'a':0}
line = {'0':'benio'}
co = 0

def ben(func):
    try:
        func = func.split(' ')
        if func[0] == "var":
           # print func[1]
            matter = eval(str(func[2]))
            print matter
            var[func[1]] = matter
            #print var
        if func[0] == "bensays":
            print var[func[1]]
        if func[0] == "beneats":
            var[func[1]] = raw_input(func[2])
        if func[0] == "int":
            var[func[1]] = int(var[func[1]])
        if func[0] == "str":
            var[func[1]] = str(var[func[1]])
        if func[0] == "if":
            if func[1]:
               ben(line[func[2]])
        if func[0] == "goto":
            ben(line[func[1]])
        if func[0] == "file":
            
            
            if func[2] == "r":
                fo = open(func[1], func[2])
                a = fo.readline()
                var[func[3]] = a
                fo.close()
            elif func[2] == "w" or "a":
                fo = open(func[1], func[2])
                fo.write(var[func[3]])
                fo.close()
            fo.close()
        if func[0] == "dump":
            print var
            print line
            print co
        if func[0] == "until":
            while int(func[1]) != int(var[func[2]]):
                ben(line[func[3]])
    except:
            print "Error line " + str(co)



while 1==1:
    co = co + 1
    func = raw_input(str(co) + " >")
    line[str(co)] = func 
    ben(func)
