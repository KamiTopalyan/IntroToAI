from Tree import Grid
# tuple formatimiz uclu --> x,y ve duvar olup olmadigi
Grid = Grid()

def read(Grid,linelen):
    y=0
    x=0
    f = open("test1.lay", "r")#dosyada verilen maze stringlerini okuyoruz !!!TEK MAZE OLMALI!!!
    string = f.read()#string olarak saveliyoruz
    print(string)#test amacli print

    for m in range(len(string)):#x axis
        if m%linelen==0 and m>0:
            y+=1
            x=0
        if(string[m] == '%'):#duvar mi degil mi
            Grid.append(x,y,True)#x ve y koodrinatlari, true ise duvar demek ve node kesilecek
        elif(string[m] == ' '):
            Grid.append(x,y, False)
        x+=1
    print(Grid)
read(Grid, 3)
