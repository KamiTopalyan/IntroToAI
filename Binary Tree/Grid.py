class Grid:
    GridVar = []
    startPos = 0
    targetPos = 0
    
    class GridSlot:
        def __init__(self, x, y, iswall, value):
            self.pos = (x,y)
            self.iswall = iswall
            self.value = value
        
    def append(self, x, y, iswall, value):
        self.GridVar[x].append(self.GridSlot(x,y,iswall, value))
            
    def read(self, path: str) -> None:
        f = open(path, "r", encoding='utf-8')
        string = f.read()
        rows = string.splitlines()
        for r in range(len(rows)):
            self.GridVar.append([])
            for c in range(len(rows[r])):
                if(rows[r][c] == '%'):
                    self.append(r,c,True, "%")
                elif(rows[r][c] == ' '):
                    self.append(r,c,False, " ")
                elif(rows[r][c] == 'p'):
                    self.append(r,c,False, "p")
                    self.startPos = (r,c)
                    print(self.startPos)
                elif(rows[r][c] == 'F'):
                    self.append(r,c,False, "F")
                    self.targetPos = (r,c)
                    print("set Target to ", (r,c))
                else:
                    self.append(r,c,True, rows[r][c])
        print(self)
        
    def isWall(self, x, y):
        return self.GridVar[x][y].iswall
    
    def getGrid(self):
        return self.GridVar
    
    def isTarget(self, x, y):
        return self.targetPos == (y,x)
    
    def getFinalGrid(self, pos: tuple, visited: list[tuple]):
        string = ""
        for x in range(len(self.GridVar)):
            for y in range(len(self.GridVar[x])):
                string += '\033[1;31mX\033[0m' if (x,y) in visited else self.GridVar[x][y].value
            string += "\n"
        return string