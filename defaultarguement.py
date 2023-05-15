#default arguments demo
def grocery(item, price=40.00):
    #to display the given arguments
    print("item=%s" %item)
    print("price=%.2f" %price)
#call grocery() and pass arguments
grocery(item='Sugar', price=50.75) #pass 2 arguments
grocery(item='sugar') #default value for price is used
          

