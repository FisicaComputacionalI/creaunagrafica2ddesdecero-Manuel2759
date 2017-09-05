import numpy as np
import pylab as pl
x=[1, 2, 3, 4]
y=[7.7, 7.8, 8.5, 8.75]
pl.plot(x, y)
pl.xlabel('Semestre[x]')
pl.ylabel('Promedio[y]')
pl.savefig('tar.png')
