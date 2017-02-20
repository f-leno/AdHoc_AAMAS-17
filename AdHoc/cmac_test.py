from cmac import CMAC
import numpy as np
import numpy.random as npr

c = CMAC(5,0.1,0.1)

data = [0.5, 0.7, 0.1, 0, 1, 0.543]
#for i in range(1):
#    t = npr.rand(10) * 4 - 2
#    print(type(t))
#    print("t[%d]: %s" % (i,str(t)))
#    pts = c.quantize(t)
#    print("pts[%d]: %s" % (i,str(pts)))
    #pts = c.quantize_alt(t)
    #print("pts[%d]: %s" % (i,str(pts)))
    #pts = c.quantize_fast(t)
    #print("pts[%d]: %s" % (i,str(pts)))
#    data.append([t,pts])

print data

print c.quantize(data)

#labels = [d[1][0] for d in data]

#print len(set(labels))
