# -*- coding: cp1252 -*-
import math 
import cv2
import numpy as np
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time
import base64
from PIL import Image
import StringIO
pnconfig = PNConfiguration()
 
pnconfig.publish_key = 'pub-c-6e938ef8-f0e6-4215-a092-824794c101e3'
pnconfig.subscribe_key = 'sub-c-53cabfec-3dd7-11e7-82b8-0619f8945a4f'
 
pubnub = PubNub(pnconfig) 


def publish_callback(result, status):
    pass
    

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels('canal1').execute()
my_listener.wait_for_connect()
print('Conectado')
x=0
suma=0
cal=1000
def segmentos(img2):
            res=0
            A=img2[6:26,17:62]
            B=img2[17:60,52:68]
            C=img2[77:115,50:66]
            D=img2[115:131,5:48]
            E=img2[73:118,2:16]
            F=img2[30:65,1:39]
            G=img2[58:83,20:53]
            a=np.linalg.norm(A,1)
            print (a,'A')
            b=np.linalg.norm(B,1)
            print (b,'B')
            c=np.linalg.norm(C,1)
            print (c,'C')
            d=np.linalg.norm(D,1)
            print (d,'d')
            e=np.linalg.norm(E,1)
            print (e,'E')
            f=np.linalg.norm(F,1)
            print (f,'F')
            g=np.linalg.norm(G,1)
            print (g,'G')
            
            if(a >cal and b >cal and c>cal and d>cal and e>cal and f>cal and g<cal):
                res='0'
            if(a <cal and b >cal and c>cal and d<cal and e<cal and f<cal and g<cal):
                res='1'
            if(a >cal and b >cal and c<cal and d>cal and e>cal and f<cal and g>cal):
                res='2'
            if(a >cal and b >cal and c>cal and d>cal and e<cal and f<cal and g>cal):
                res='3'
            if(a <cal and b >cal and c>cal and d<cal and e<cal and f>cal and g>cal):
                res='4'    
            if(a >cal and b <cal and c>cal and d>cal and e<cal and f>cal and g>cal):
                res='5'    
            if(a >cal and b <cal and c>cal and d>cal and e>cal and f>cal and g>cal):
                res='6'    
            if(a >cal and b >cal and c>cal and d<cal and e<cal and f<cal and g<cal):
                res='7'    
            if(a >cal and b >cal and c>cal and d>cal and e>cal and f>cal and g>cal):
                res='8'    
            if(a >cal and b >cal and c>cal and d>cal and e< cal and f>cal and g>cal):
                res='9'    
            return res,A,B,C,D,E,F,G


def main():
       
       switch=True
       ic=0
       aux=''
       aux2=0
       xcar=54
       ycar=50
       add=0
       token=True
       cap1=cv2.VideoCapture(1)
       tramas=1000
       calmedida=5000
       while(True):
            starting_point = time.time()
            _,im=cap1.read()
            auxi=im
            batery=im[57:75,204:230]
            batery=cv2.cvtColor(batery,cv2.COLOR_BGR2GRAY)
            cv2.imwrite("MA.jpg",auxi)
            i=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
           
            i=cv2.medianBlur(i,3)          
            kernel = np.ones((3,3),np.float32)/9
            i = cv2.blur(i,(5,5))
            ii=i
            #i=cv2.imread("M2.jpg",0);
            if(switch):
                template = cv2.imread("punto.jpg",0)
            else:
                template = cv2.imread("punto.jpg",0)
            w, h = template.shape[::-1]
            methods = ['cv2.TM_CCORR_NORMED']
            for meth in methods:
                method = eval(meth)
            res = cv2.matchTemplate(i,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            puntox=i[215:232,405:419]
            puntoy=i[218:234,313:327]
            a=np.linalg.norm(puntox,1)
            b=np.linalg.norm(puntoy,1)
            
            print 'puntos',a,b
            print 'Punto:',(top_left[0],top_left[1],bottom_right[0],bottom_right[1])
            if(top_left[0]>400 and top_left[0]<430 and bottom_right[1]<240):
                puntoa=''
                puntob='.'
                print 'b'
            elif(top_left[0]>=300 and top_left[0]<400 and bottom_right[1]<240):
                puntoa='.'
                puntob=''
                print 'a'
            else:
                puntoa=''
                puntob=''
                
            p=i
            template = cv2.imread("recorte2.jpg",0)
            w, h = template.shape[::-1]
            methods = ['cv2.TM_CCORR_NORMED']
            for meth in methods:
                method = eval(meth)
            res = cv2.matchTemplate(i,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            
            ##print ('A',top_left,'B',bottom_right)
            img=i[47:237,192:518]
            imgaux=auxi[90:225,125:515]
            z=img
            cv2.rectangle(auxi,top_left, bottom_right, 255, 1)
            img11=img[35:61,16:85]#PH
            img21=img[33:59,92:162]#MS
            img31=img[32:58,169:238]#PPM
            img41=img[31:56,244:316]#C°
##            img4=img[4:30,4:85]#C*
##          i= cv2.equalizeHist(i)  
            aux1=img
            a=np.linalg.norm(img11,2)
            b=np.linalg.norm(img21,2)
            c=np.linalg.norm(img31,2)
            d=np.linalg.norm(img41,2)
            print 'Tipo de dato: ',a,b,c,d
            value=''
            if(min(a,b,c,d)==a and a<calmedida):
                value='PH'

                switch=True
            elif(min(a,b,c,d)==b and b<calmedida):

                value='mS/cm'
                
                switch=True
            elif(min(a,b,c,d)==c and c<(calmedida+1500)):
                
                value='PPM'
                switch=True
            elif(min(a,b,c,d)==d and c<calmedida):
           
                value='Celsius'
                switch=False
##            print value
            img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,23,1)
            img=cv2.bitwise_not(img)
            kernel = np.ones((3,3))
            img = cv2.erode(img,kernel,iterations = 4)
          
            try:   
                    img0=img[xcar:(xcar+141),(ycar-36):(ycar-19)]
                    img1=img[xcar:(xcar+141),ycar:(ycar+70)]
                    img2=img[xcar:(xcar+141),(ycar+100):(ycar+170)]
                    img3=img[xcar:(xcar+141),(ycar+187):(ycar+257)]
                    print ('Numero 1 inicial',np.linalg.norm(img0,1))
                    if(np.linalg.norm(img0,1)>1500):
                                    numero0=1
                    else:
                        numero0=0

                    
                    
                    
                    
                    
                    
                    numero,a,b,c,d,e,f,g=segmentos(img1)
                    
                    numero3,a,b,c,d,e,f,g=segmentos(img3)
                    numero2,a,b,c,d,e,f,g=segmentos(img2)


                    
                    numero=float(str(numero0)+str(numero)+puntoa+str(numero2)+puntob+str(numero3))
                    print 'Numero de salida:',numero
                    estado=int(np.linalg.norm(batery,2))
                    
                    if estado >=1000:
                        flag='A'
                    if estado <1000 and estado >800:
                        flag='F'
                    if estado<800 and estado >500:
                        flag='S'
                    if estado < 500:
                        flag='Fa'
##                    print flag
                    if(numero!=aux2):
                        cv2.imwrite("MS2.jpg",img)
                        im = Image.open('MS2.jpg')
                        output = StringIO.StringIO()
                        im.save(output, "JPEG", quality=89)
                        encoded_string1 = base64.b64encode(output.getvalue())
                        cv2.imwrite("Muestra1.jpg",z)
                        im = Image.open('Muestra1.jpg')
                        output = StringIO.StringIO()
                        im.save(output, "JPEG", quality=89)
                        encoded_string = base64.b64encode(output.getvalue())                        
                        pubnub.publish().channel('canal1').message({'bat':flag,'text':value,'value':numero,'src':encoded_string,'src1':encoded_string1}).async(publish_callback)
                        ##time.sleep(0.5)
                        aux2=numero
##                        
##                        
##                        
##                
##
##                    
##                    
##                    
####                    cv2.imshow('Hola',batery)
####                    cv2.imshow('Hola1',auxi)
####                    cv2.imshow('Hola2',img31)
##                    cv2.imshow('A',auxi)
####                    cv2.imshow('A',img11)
####                    cv2.imshow('B',img21)
####                    cv2.imshow('C',img31)
####                    cv2.imshow('D',img41)
####                    cv2.imshow('E',e)
####                    cv2.imshow('F',f)
####                    cv2.imshow('G',g)
##                    
##                    
##
##                    
##                    
##            
            except(ValueError):
                        print ValueError
            elapsed_time = time.time () - starting_point

            ##print (elapsed_time)
            cv2.imshow('Hola1',z)
##            cv2.imshow('Hola2',img1)
##            cv2.imshow('Hola3',img2)
##            cv2.imshow('Hola4',img3)
            cv2.imshow('a',a)
            cv2.imshow('b',b)
            cv2.imshow('c',c)
            cv2.imshow('d',d)
            cv2.imshow('e',e)
            cv2.imshow('f',puntoy)
            cv2.imshow('g',puntox)
            if (cv2.waitKey(1) & 0xFF==ord('q')):
##                                cv2.imwrite("rebbot2.jpg",puntox)
                                cap1.release()
                                cv2.destroyAllWindows()
                                break 


if __name__ == "__main__":
    
    
    main()
    pubnub.unsubscribe().channels("canal1").execute()
    

