import cv2
import tensorflow as tf
import numpy as np
import czifile


HELP_TEXT='''
DT-UT classification
Multiclass classification in detection
drug trated and untreated cancer images
and its application in XAI.

Sayantani Ghosh (CU, Kolkata)
Tamojit Das (CU, Kolkata)

'''

LABELS={
    0 : 'Moderately Sensitive',
    1 : 'Resistant',
    2 : 'Sensitive'
    }


def predict_from_path(path):
  model=tf.keras.models.load_model('tam4_model.h5')
  print('Model loaded')
  img=czifile.imread(path)
  img=img.reshape(1038,1388,1)
  img=cv2.resize(img,(224,224))
  print('Reshaped resized')
  label=np.argmax(model.predict(img.reshape(-1,224,224,1)))
  print('predicted')
  return LABELS[label]

print(predict_from_path('A2.czi'))
