#Nivel 1: Venta Básica funcional

print("Hi, Welcome to Dollar Town 🤑")
client= input ("Please enter your name: ") 
product = input ("Please tell me what product do you want to buy: ")
price = int(input("How much does this product cost?: "))
amount = int(input("How much of this product are you carrying?: "))
subtotal = (price*amount)


if subtotal >= 50000:
    dcto = (50000*5)/100
    total= (subtotal-dcto)
    print(" ")
    print(f"Client: {client} \nProduct: {product} \nSubtotal: {subtotal} \nDcto 5%: {dcto} \nTotal: {total} ")


else: 
    print(" ")
    print(f"Client: {client} \nProduct: {product} \nSubtotal: {subtotal} \nDcto 5%: No apply \nTotal: {subtotal} ")




