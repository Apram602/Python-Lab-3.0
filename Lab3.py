print("")
print("WELCOME TO THE AMANDO SHOPPING SITE\n")
print("1. Add a product to the cart ") 
print("2. Search for a product ")
print("3. Delete a product from the cart ")
print("4. Display the contents of the cart")
print("5. Purchase items")
print("6. Quit\n")


shoppingCart={}
x=int(input("Please Select From Menu: "))
z=0

while x !=6:
    if x==1:
        if len(shoppingCart) >= 5:
            print("Cart is full. You cannot add more products.")
        else:
            product_name = input("Enter Product Name: ")
            product_price = float(input("Enter Product Price: "))
            brand = input("Enter Brand: ")
            shoppingCart[product_name] = {"product-price": product_price, "brand": brand} 
            print("") 
            print("Added Product:\n", product_name) 
            print("Price:", product_price) 
            print("Brand:", brand)

    elif x==2:
        search=input("Enter product to search: ")
        if search in shoppingCart:
            print("Found:", shoppingCart[search])
        else:
            print("No product exists with this name.")

    elif x ==3:
        if shoppingCart =={}:
            print("Cart is empty, no item is found")
        else:
            delete = input("Enter Product to delete from cart: ")
            if delete in shoppingCart:
                del shoppingCart[delete]
                print("Deleted", delete)
            else:
                print("Product not found in cart")

    elif x==4:
        if shoppingCart =={}:
            print("Cart is empty.")
        else:
            print("Your Cart:\n",shoppingCart)
            print("")

    elif x == 5:
        if shoppingCart =={}:
            print("Cart is empty, please select an item before completing purchase.\n")
        else:
            purchase= input("Complete purchase (Y/N)?\n") 
            if purchase =='Y':
                print("Thank you for your business.")
                z=z+product_price
                print("Your Total",z)
                shoppingCart.clear()
            elif purchase == 'N':
                print("Please continue shopping.")
            else:
                print("Please answer either Y or N.” and repeat this process")
         

    print("")
    print("WELCOME TO THE AMANDO SHOPPING SITE\n")
    print("1. Add a product to the cart ") 
    print("2. Search for a product ")
    print("3. Delete a product from the cart ")
    print("4. Display the contents of the cart")
    print("5. Purchase items")
    print("6. Quit\n")

    x=int(input("Please Select From Menu: "))

print("You have Quit the Menu...")


