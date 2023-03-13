#This inherits the class item from Item.py
class book(Item):

    # Methods
    def preview(self):
        print(f"Previewing{self.Title} by {self.Author}:\n{self.Synopsis}")
        
        #Attributes
    ISBN = 0
    Author = ''
    Synopsis = ''
