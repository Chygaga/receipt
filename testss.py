item_list = (input("Enter the item list "))
item_price1 = int(input("Enter the item price: N "))

def vat_calc(price):
    if price<5000:
        vat_amount=price*0
    else:
        vat_amount=price* 0.05
    return vat_amount
        #totalprice = vat_amount+price


def totalPrice(price, vat):
    totalCost =price+vat
    return totalCost


print("VAT amount: N", vat_calc(item_price1))
print ("Total cost", totalPrice(item_price1, vat_calc(item_price1)))
#print(totalprice)