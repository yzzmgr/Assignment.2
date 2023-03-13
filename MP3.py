#This inherits the item class from Item.py
class mp3(Item):

    #Methods
    def playExtract(self):
        print(f"Playing a {self.Duration} second extract of {self.Title} by {self.Artist}.")

    def download(self):
        print(f"Downloading the {self.Title} by {self.Artist}...")
        print("Download completed.")
        
        #Attributes
    Duration = 0
    Artist = ''
