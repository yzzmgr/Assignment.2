class order:

    #Methods
    def validatePayment(self):
        print("Validating payment...")
        # Payment validation code here
        self.Status = "Payment Validated"

    def cancel(self):
        print("Cancelling order...")
        self.Status = "Cancelled"

    def dispatch(self):
        print("Dispatching order...")
        self.Status = "Dispatched"

    def confirmDelivery(self):
        print("Confirming delivery...")
        self.Status = "Delivered"

    def refund(self):
        print("Refunding order...")
        #This is the refund processing code
        self.Status = "Refunded"

    def archive(self):
        print("Archiving order...")
        #This is the Archival code
        self.Status = "Archived"
    
    #Attributes
    Date = ''
    Status = ''
    ShoppingCart = ''
    DeliveryAddress = ''
    PaymentMethod = ''
