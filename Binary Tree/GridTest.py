from Tree import Grid
import os

Grid = Grid(3,3)
print(os.path.abspath("testLays/test1.lay"))
Grid.ReadLay(os.path.abspath("testLays/test1.lay"))
