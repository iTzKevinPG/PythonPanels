from LoadData import LoadData

data = LoadData()

data.loadData('https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD%22')
data.firstElements(10)
data.lastElements(15)
data.dataGroupby((['Sexo', 'Estado']), 'suma')