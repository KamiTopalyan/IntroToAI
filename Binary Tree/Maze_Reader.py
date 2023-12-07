from Tree import Grid
# tuple formatimiz uclu --> x,y ve duvar olup olmadigi
def read(Grid: Grid) -> None:
    f = open("Berkeley/layouts/bigMaze.lay", "r")#dosyada verilen maze stringlerini okuyoruz !!!TEK MAZE OLMALI!!!
    string = f.read()#string olarak saveliyoruz
    rows = string.splitlines()
    for r in range(len(rows)):
        Grid.generateRow(1)
        for c in range(len(rows[r])):
            if(rows[r][c] == '%'):
                Grid.append(r,c,True,r, "%")
            if(rows[r][c] == ' '):
                Grid.append(r,c,False,r, " ")
            if(rows[r][c] == 'P'):
                Grid.append(r,c,False,r, "P")
                Grid.setStartPos((r,c))
                print(Grid.startPos)
            if(rows[r][c] == 'F'):
                Grid.append(r,c,False,r, "F")
                Grid.setTargetPos((r,c))
                print("set Traget to ", (r,c))
    print(Grid)

