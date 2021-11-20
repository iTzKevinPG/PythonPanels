import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

class PredictCNN():

    longitud, altura = 150, 150
    modelo = 'Proyect/CNN desde cero/modelo/modelo.h5'
    pesos_modelo = 'Proyect/CNN desde cero/modelo/pesos.h5'
    cnn = load_model(modelo)
    cnn.load_weights(pesos_modelo)


    def predict(self, file):
      x = load_img(file, target_size=(self.longitud, self.altura))
      x = img_to_array(x)
      x = np.expand_dims(x, axis=0)
      array = self.cnn.predict(x)
      result = array[0]
      answer = np.argmax(result)
      if answer == 0:
        print("pred: Gato")
      elif answer == 1:
        print("pred: Gorila")
      elif answer == 2:
        print("pred: Leon")
      elif answer == 3:
        print("pred: Perro")

      return answer

    pass

