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

def main():
       cap1=cv2.VideoCapture(0)
       while(True):
            _,im=cap1.read()
            #im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            im=im[0:300,0:300]
            cv2.imshow('Vivo',im)
            cv2.imwrite("MS2.jpg",im)
            im = Image.open('MS2.jpg')
            output = StringIO.StringIO()
            im.save(output, "JPEG", quality=89)
            encoded_string1 = base64.b64encode(output.getvalue())
            pubnub.publish().channel('canal1').message({'src':'data:image/jpeg;base64,'+encoded_string1}).async(publish_callback)  
            if (cv2.waitKey(1) & 0xFF==ord('q')):
                                cv2.destroyAllWindows()
                                break 


if __name__ == "__main__":
    
    
    main()
    pubnub.unsubscribe().channels("canal1").execute()
