#LEGB = Local → Enclosing → Global → Built-in

#L

def order():
    food = "Briyani"
    print("Your order is :", food)
order()

#E

def cart():
    discount = 10
    def checkout():
        print("Applying discount:", discount)
    checkout()
cart()


#G

user_id = "simakahmed18"

def homepage():
    print("Welcome Back! :", user_id)
def profile():
    print("Welcome to profile page: ", user_id)

homepage()
profile()

#B
'''print(__file__)'''

#Example

delivery_partner = "swiggy"   # Global

def hotel():
    item = "pizza"            # Enclosing

    def order_now():
        quantity = 2          # Local
        print(f"ordering {quantity} {item} using {delivery_partner}")

    order_now()

hotel()
