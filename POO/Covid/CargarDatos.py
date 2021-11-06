import pandas as pd
import matplotlib.pyplot as plt

class LoadData():

    data: str

    def loadData(self, ruta):
        self.data = pd.read_csv(ruta)
        pass


    def firstElements(self, numElements):
        y = self.data.head(numElements)
        print(y)
        pass

    def lastElements(self, numElements):
        y = self.data.tail(numElements)
        print(y)
        pass

    def dataGroupby(self, colums, function):
        if(function == 'suma'):
            self.suma(colums)
        if(function == 'promedio'):
            self.promedio(colums)
        if(function == 'conteo'):
            self.conteo(colums) 

        x = self.data.Sexo.unique()
        y = self.data.Sexo.value_counts().tolist()

        plt.bar(x, y)
        plt.title('Contagios por Genero')
        ax = plt.subplot()
        ax.set_xlabel('Generos')
        ax.set_ylabel('Numero de contagios')
        plt.show()
        pass


    def suma(self, data):
        datosColum = self.data.groupby(by=data).sum()
        print(datosColum)
        pass

    def promedio(self, data):
        datosColum = self.data.groupby(by=data).mean()
        print(datosColum)
        pass

    def conteo(self, data):
        datosColum = self.data.groupby(by=data).count()
        print(datosColum)
        pass