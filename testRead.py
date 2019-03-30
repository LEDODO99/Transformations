from SRflatShade import *
from Obj import *
r=image()
r.glCreateWindow(920,920)
r.glClear()
r.glViewPort(459,459,920,920)
o=objeto()
o.readObj("Chibirobo.obj")
r.flatShadeObj(o.vertices,o.faces)
r.glFinish()
