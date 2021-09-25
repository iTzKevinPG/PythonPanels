from Legum.Product import Product

class Legum(Product):
     
    #Default parameters
    typeProduct = "Legumbre"
    
    def __init__(self, idLegum, name):
        
        Product.__init__(self, idLegum, name, self.typeProduct)
        pass

    def showLegums(self):
            
        print("Estas son las legumbres")
        
        for i in range(len(Product.products)):
            
            if Product.products[i]['typeProduct'] == self.typeProduct:   
                
                print(f"{i+1}. {Product.products[i]['name']} con identificador {Product.products[i]['idProduct']} y el de tipo {Product.products[i]['typeProduct']}")
                
            pass
        
        pass
