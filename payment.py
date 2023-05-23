class Payment:
    def __init__(self, payment_methods):
        self.payment_methods =[]
    def select_payment_method(self, method):
        # Check if the selected payment method is available
        if method in self.payment_methods:
            print(f"Selected payment method: {method}")
        else:
            print(f"{method} is not available.")
    def cancel_payment(self):
        confirmation=input("Are you sure you want to cancel the transaction? (yes/no)")
        if confirmation.lower=="yes":
            print("Payment transaction cancelled.")
        else:
            print("Transaction not cancelled")

            
        
      

