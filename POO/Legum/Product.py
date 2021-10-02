class Product:
         
    #Instance parameters
    products = []
    
    def __init__(self, idProduct, name, typeProduct):
        
        self.products.append({'idProduct': idProduct, 'name': name, 'typeProduct': typeProduct})
                
        print(f"Se agrego el producto: {name} que es una: {typeProduct}")
        pass

