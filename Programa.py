# -*- coding: cp1252 -*-
import math 
import cv2
import numpy as np
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time

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
cal=1100

def segmentos(img2):
            res=0
            A=img2[3:20,17:60]
            B=img2[17:60,64:86]
            C=img2[77:121,54:73]
            D=img2[115:131,10:58]
            E=img2[78:118,5:18]
            F=img2[20:60,3:22]
            G=img2[58:73,13:50]
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
       xcar=32
       ycar=68
       add=0
       token=True
       cap1=cv2.VideoCapture(1)
       tramas=1000
       while(True):
            _,im=cap1.read()
            i=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            
            i=cv2.medianBlur(i,3)          
            kernel = np.ones((3,3),np.float32)/9
            i = cv2.blur(i,(5,5))
            ii=i
            #i=cv2.imread("M2.jpg",0);
            if(switch):
                template = cv2.imread("punto.jpg",0)
            else:
                template = cv2.imread("Luz2.jpg",0)
            w, h = template.shape[::-1]
            methods = ['cv2.TM_CCORR_NORMED']
            for meth in methods:
                method = eval(meth)
            res = cv2.matchTemplate(i,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            
            
            if(top_left[0]>400 and bottom_right[1]<250):
                puntoa=''
                puntob='.'
            elif(top_left[0]<400 and bottom_right[1]<250):
                puntoa='.'
                puntob=''
            else:
                puntoa=''
                puntob=''
                
            p=i
            #cv2.rectangle(p,top_left, bottom_right, 255, 1)
            img=i[54:232,172:533]
            
            img1=img[4:30,4:85]#PH
            img2=img[4:30,98:173]#MS
            img3=img[12:38,175:253]#PPM
##            img4=img[4:30,4:85]#C*
##          i= cv2.equalizeHist(i)  
            aux1=img
            a=np.linalg.norm(img1,2)
            b=np.linalg.norm(img2,2)
            c=np.linalg.norm(img3,2)
            print (a,b,c)
            print('-----------------')
            if(min(a,b,c)==a and a<4200):
                value='PH'
                print ('PH',a)
                switch=True
            elif(min(a,b,c)==b and b<4200):
                print ('mS/cm',b)
                value='mS/cm'
                
                switch=True
            elif(min(a,b,c)==c and c<4300):
                
                print ('PPM',c)
                value='PPM'
                switch=True
            else:
                print ('C°')
                value='Celsius'
                switch=False
            print('-----------------')
        
                       
            
                       
##            print ('C°',np.linalg.norm(img4,2))
            
            #media=[bottom_right[0]/2,bottom_right[1]/2]
            
            #iup=i[top_left[1]:media[0],top_left[0]:bottom_right[0]]          
            #idown=i[media[0]:bottom_right[1],top_left[0]:bottom_right[0]]

            
            img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,23,1)
            img=cv2.bitwise_not(img)
            kernel = np.ones((3,3))
            img = cv2.erode(img,kernel,iterations = 4)
            if(add<tramas and not(token)):
                try:
                    aux=input('Mover a la izquierda /1 mover a la derecha /2 Bajar /3 Subir /4 terminar ajuste /5')
                except ValueError:
                    print 'Valor no detectado'
                if(aux==1):
                    ycar=ycar-5
                if(aux==2):
                    ycar=ycar+5
                if(aux==3):
                    xcar=xcar+5
                if(aux==4):
                    xcar=xcar-5
                if(aux==5):
                    token=True
                add=0    
            try:
                    img1=img[xcar:(xcar+141),ycar:(ycar+76)]
                    img2=img[xcar:(xcar+141),(ycar+100):(ycar+176)]
                    img3=img[xcar:(xcar+141),(ycar+196):(ycar+272)]

        ##            img1=img[xcar:(xcar+141),ycar:(ycar+76)]
        ##            img2=img[xcar:(xcar+141),(ycar+76+24):(ycar+(76*2)+24)]
        ##            img3=img[xcar:(xcar+141),(ycar+(76*2)+(24*2)):(ycar+(76*2)+(24*3))]
        ##            #numero=(str(segmentos(img1))+str(segmentos(img2))+str(segmentos(img3)))
                    
                    
                    
                    
                    numero,a,b,c,d,e,f,g=segmentos(img1)
                    numero3,a,b,c,d,e,f,g=segmentos(img3)
                    numero2,a,b,c,d,e,f,g=segmentos(img2)
                    
                    numero=float(str(numero)+puntoa+str(numero2)+puntob+str(numero3))
                    if(numero != aux2):
                         pubnub.publish().channel('canal1').message({'value':numero,'text':value}).async(publish_callback)
                         aux2=numero       
                 
                   
                    cv2.imshow('Hola',p)
                    cv2.imshow('Hola1',img2)
                    cv2.imshow('G',g)
                    cv2.imshow('A',a)
                    cv2.imshow('B',b)
                    cv2.imshow('C',c)
                    cv2.imshow('D',d)
                    cv2.imshow('E',e)
                    cv2.imshow('F',f)
                    add+=1
                    
                    
            
            except(ValueError):
                        print ValueError
            if (cv2.waitKey(1) & 0xFF==ord('q')):
                                cv2.imwrite("MS.jpg",p)
                                cv2.imwrite("MS2.jpg",img) 
                                cap1.release()
                                cv2.destroyAllWindows()
                                break 


if __name__ == "__main__":
    
    
    main()
    pubnub.unsubscribe().channels("canal1").execute()
    

