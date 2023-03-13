class Ttem:
    
    #Methods
    def viewFullDescription(self):
        print(f"Code: {self.Code}")
        print(f"Title: {self.Title}")
        print(f"Description: {self.Description}")
        print(f"Category: {self.Category}")
        print(f"Picture: {self.Picture}")
        print(f"Quantity in Stock: {self.QuantityInStock}")
        print(f"Price: {self.Price}")

    def addToCart(self, quantity):
        if quantity > self.QuantityInStock:
            print("Error! Not enough stock.")
            return False
        self.QuantityInStock -= quantity
        return True

    def updateStockLevel(self, quantity):
        self.QuantityInStock += quantity
        
        #Attributes
    Code = ''
    Title = ''
    Description = ''
    Category = ''
    Picture = ''
    QuantityInStock = 0
    Price = 0
    
    
        
        