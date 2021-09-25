from Legum.Product import Product

class Fruit(Product):
     
    #Default parameters
    typeProduct = "Fruta"
    
    def __init__(self, idFruit, name):
        
        Product.__init__(self, idFruit, name, self.typeProduct)
        pass
    
    def showFruits(self):
            
        print("Estas son las frutas")
        
        for i in range(len(Product.products)):
            
            if Product.products[i]['typeProduct'] == self.typeProduct:   
                
                print(f"{i+1}. {Product.products[i]['name']} con identificador {Product.products[i]['idProduct']} y el de tipo {Product.products[i]['typeProduct']}")
                
            pass
        
        pass


