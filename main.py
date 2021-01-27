import sys
from tensorflow.keras.models import load_model
from numpy import argmax
from czifile import imread
from cv2 import resize
from threading import Thread
from warnings import filterwarnings
from time import sleep

filterwarnings('ignore')

print('Modules Loaded')
print()

LABELS={
    0 : 'Moderately Sensitive',
    1 : 'Resistant',
    2 : 'Sensitive'
    }


def predict(path):
    try:
        model=load_model('tam4_model.h5')
        img=imread(path)
        img=img.reshape(1038,1388,1)
        img=resize(img,(224,224))        
        label=argmax(model.predict(img.reshape(-1,224,224,1)))
        print(path,'->',LABELS[label])
    except Exception as e:
        print(path,'->',e)

    sleep(15)
        

if __name__=='__main__':
    for args in sys.argv[1:]:
        Thread(target=predict,args=(args,)).start()


    
        



