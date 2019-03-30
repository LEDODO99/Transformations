##Luis Estuardo Delgado 17187
##Tarea SR1
import struct
from collections import namedtuple
def char(c):
    return struct.pack("=c", c.encode('ascii'))
def word(c):
    return struct.pack("=h",c)
def dword(c):
    return struct.pack("=l",c)
def color(r,g,b):
    return bytes([b,g,r])
V2 = namedtuple('Vertex2', ['x', 'y'])
V3 = namedtuple('Vertex3', ['x', 'y', 'z'])
class image(object):
    def __init__(self):
        self.Ccolor=color(0,0,0)
        self.Vcolor=color(255,255,255)
        self.framebuffer=[]
        self.VPvx=0
        self.VPvy=0
        self.VPlf=0
        self.VPrf=0
        self.VPuf=0
        self.VPdf=0
        self.width=0
        self.height=0
        self.color_point=color(255,255,255)
    def glCreateWindow(self, width,height):
        self.width=width
        self.height=height

    def glViewPort(self,x,y,width,height):
        if((width%2)==0):
            self.VPlf=(int)(x-((width/2)-1))
            self.VPrf=(int)(x+(width/2))
        else:
            self.VPlf=(int)(x-((width/2)))
            self.VPrf=(int)(x+(width/2))
        if((height%2)==0):
            self.VPdf=(int)(y-((height/2)-1))
            self.VPuf=(int)(y+(height/2))
        else:
            self.VPdf=(int)(y-(height/2))
            self.VPuf=(int)(y+(height/2))
        
        if(self.VPlf<0):
            return 0
        elif(self.VPrf>self.width-1):
            return 0
        elif(self.VPuf>self.height-1):
            return 0
        elif(self.VPdf<0):
            return 0
        else:
            self.VPvx=x
            self.VPvy=y
            return 1
    def glClear(self):
        self.framebuffer=[
            [
                self.Ccolor
                for x in range(self.width)
                ]
            for y in range (self.height)
            ]
        self.zbuffer=[
            [-float('inf')for x in range(self.width)]
            for y in range(self.height)
            ]
    def glClearColor(self,r,g,b):
        self.Ccolor=color(round(r*255),round(g*255),round(b*255))
    def point(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        else:
            self.framebuffer[y][x] = self.Vcolor
    def glVertex(self,x,y):
        equis=0
        ye=0
        if(x<0):
            equis=(int)((x*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x>0):
            equis=(int)((x*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis=self.VPvx
        if(y<0):
            ye=(int)((y*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y>0):
            ye=(int)((y*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye=self.VPvy
        self.framebuffer[ye][equis]=self.Vcolor
    def glColor(self,r,g,b):
        a=round(r*255)
        if a>255:
            a=255
        elif a<0:
            a=0
        c=round(g*255)
        if c>255:
            c=255
        elif c<0:
            c=0
        e=round(b*255)
        if b>255:
            b=255
        elif b<0:
            b=0
        self.Vcolor=color(a,c,e)
    def glFinish(self):
        f = open("out.bmp", 'wb')
	#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(54+(self.width*self.height)*3))
        f.write(dword(0))
        f.write(dword(54))
	#image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()
    def glFinishNamed(self,filename):
        f = open(filename, 'wb')
	#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(54+(self.width*self.height)*3))
        f.write(dword(0))
        f.write(dword(54))
	#image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()
   
    def glLine(self,x0,y0,x1,y1):
        if(x0<0):
            equis1=(int)((x0*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x0>0):
            equis1=(int)((x0*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis1=self.VPvx
        if(y0<0):
            ye1=(int)((y0*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y0>0):
            ye1=(int)((y0*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye1=self.VPvy
        if(x1<0):
            equis2=(int)((x1*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x1>0):
            equis2=(int)((x1*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis2=self.VPvx
        if(y1<0):
            ye2=(int)((y1*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y1>0):
            ye2=(int)((y1*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye2=self.VPvy

        dy=abs(ye2-ye1)
        dx=abs(equis2-equis1)
        steep = dy>dx
        if steep:
            equis1,ye1=ye1,equis1
            equis2,ye2=ye2,equis2
            dy=abs(ye2-ye1)
            dx=abs(equis2-equis1)
        if equis1>equis2:
            equis1,equis2=equis2,equis1
            ye1,ye2=ye2,ye1
        offset = 0
        threshhold=dx
        y=ye1
        equis2+=1
        for x in range(equis1,equis2,+1):
            if steep:
                self.framebuffer[x][y]=self.Vcolor
            else:
                self.framebuffer[y][x]=self.Vcolor
            offset +=dy
            if offset>=threshhold:
                if ye1<ye2:
                    y+=1
                else:
                    y-=1
                threshhold+=dx
    def fill(self):
        for x in range(self.width):
            pintar=False
            canChange=True
            for y in range(self.height):
                if(self.framebuffer[y][x]==self.Ccolor):
                    canChange=True
                    if pintar:
                        self.framebuffer[y][x]=self.Vcolor
                else:
                    if canChange:
                        pintar = not pintar
                        if(self.framebuffer[y+1][x+1]==self.Ccolor):
                            canChange=False

    def lineObj(self,vertices,caras):
        for a in caras:
            xs=[]
            ys=[]
            p=0
            for o in a:
                xs.append(vertices[o[0]-1][0])
                ys.append(vertices[o[0]-1][1])
                p+=1
            for o in range(0,p,+1):
                if o==0:
                    r=p-1
                else:
                    r=o-1
                self.glLine(xs[r],ys[r],xs[o],ys[o])
    
    def flatShadeObj(self,vertices,caras):
        luz=V3(0,0,1)
        for cara in caras:
            x1=int(self.VPrf*((vertices[cara[0][0]-1][0]+1)/2))
            y1=int(self.VPrf*((vertices[cara[0][0]-1][1]+1)/2))
            z1=int(self.VPrf*((vertices[cara[0][0]-1][2]+1)/2))
            x2=int(self.VPrf*((vertices[cara[1][0]-1][0]+1)/2))
            y2=int(self.VPrf*((vertices[cara[1][0]-1][1]+1)/2))
            z2=int(self.VPrf*((vertices[cara[1][0]-1][2]+1)/2))
            x3=int(self.VPrf*((vertices[cara[2][0]-1][0]+1)/2))
            y3=int(self.VPrf*((vertices[cara[2][0]-1][1]+1)/2))
            z3=int(self.VPrf*((vertices[cara[2][0]-1][2]+1)/2))

            v1 = V3(x1,y1,z1)
            v2 = V3(x2,y2,z2)
            v3 = V3(x3,y3,z3)

            normal = self.normalVec(self.prodCruz(self.restaVec(v2,v1),self.restaVec(v3,v1)))
            intens = self.prodPunto(normal,luz)
            if intens<0:
                pass
            else:
                self.glColor(intens,intens,intens)
                self.triangle(v1,v2,v3)
    
    def bbox(self,A, B, C):
        xs = sorted([A.x, B.x, C.x])
        ys = sorted([A.y, B.y, C.y])
        return V2(xs[0], ys[0]), V2(xs[2], ys[2])
    
    def barycentric(self,A, B, C, P):
        cx, cy, cz = self.prodCruz(
            V3(B.x - A.x, C.x - A.x, A.x - P.x),
            V3(B.y - A.y, C.y - A.y, A.y - P.y)
        )

        if cz == 0:
            return -1, -1, -1
        
        # Coordenadas baricentricas
        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return w, v, u
    
    def triangle(self,A, B, C):
        bbox_min, bbox_max = self.bbox(A, B, C)

        for x in range(bbox_min.x, bbox_max.x + 1):
            for y in range(bbox_min.y, bbox_max.y + 1):
                w, v, u = self.barycentric(A, B, C, V2(x, y))

                # Si estan fuera del triangulo, no pintar
                if w < 0 or v < 0 or u < 0:
                    pass
                else:
                    z = A.z * w + B.z * v + C.z * u
                    # Si z es mayor que el z buffer, pintar y cambiar valor zbuffer
                    if z > self.zbuffer[x][y]:
                        self.point(x, y)
                        self.zbuffer[x][y] = z
    
    def prodPunto(self,v0,v1):
        return (v0.x*v1.x)+(v0.y*v1.y)+(v0.z*v1.z)
    def sumaVec(self,v0,v1):
        return V3(v0.x+v1.x,v.y+v1.y,v0.z+v1.z)
    def restaVec(self,v0,v1):
        return V3(v0.x-v1.x,v0.y-v1.y,v0.z-v1.z)
    def mul(self,v0,k):
        return V3(v0.x*k,v0.y*k,v0.z*k)
    def prodCruz(self,v0,v1):
        return V3(
            v0.y * v1.z - v0.z * v1.y,
            v0.z * v1.x - v0.x * v1.z,
            v0.x * v1.y - v0.y * v1.x
        )
    def magVec(self,v0):
        return (v0.x**2 + v0.y**2 + v0.z**2)**0.5
    def normalVec(self,v0):
        l = self.magVec(v0)
        if not l:
            return V3(0, 0, 0)
        return V3(v0.x/l, v0.y/l, v0.z/l)
    
        
    
    
