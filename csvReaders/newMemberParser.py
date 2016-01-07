def parseFile(className, fname):
    strToRet = ".box.brother \n" + "  %" + "h3 " + className + " Class\n" + "  %" + "ul\n"
    namesNBro = []
    with open(fname) as f:
        for line in f:
            namesNBro.append(line)
    namesNBro.sort()
    for name in namesNBro:
        strToRet = strToRet + "    %" + "li " +name
    print(strToRet)

parseFile("Iota", "iota.csv")