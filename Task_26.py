# Supermarket Project
items_list="""
Rice        Rs 10/kg
Sugar       Rs 8/kg
Oil         Rs 30/litre
Salt        Rs 25/kg
Paneer      Rs 40/kg
Maggie      Rs 12/pack
Boost       Rs 200/bottle"""

items={'rice':10,'sugar':8,'oil':30,'salt':25,'paneer':40,'maggie':12,'boost':200}
price_list=[]
total_price=0
only_items=[]
only_quantity=[]
only_price=[]
final_amount=0

name=input("Enter your name: ")
    
while True:
    choice=int(input("Press 1 for list or 2 to exit: "))
    if choice==2:
        print("Thank you for shopping")
        break 
    elif choice==1:
        print(items_list)
        while True:
            choice1=int(input("To buy press 1 or press 2 to exit: "))
            if choice1==2:
                print("Thank you for shopping")
                break
            elif choice1==1:
                choose_item=input("Choose your items: ").lower()
                while True:
                    quantity=input("Enter quantity: ")
                    if quantity.isdigit():
                        quantity_int=int(quantity)
                        break
                    else:
                        print("Please enter a valid quantity.")
                if choose_item in items:
                    price=items[choose_item]*quantity_int
                    price_list.append((choose_item,quantity_int,items[choose_item],price))
                    total_price+=price
                    only_items.append(choose_item)
                    only_quantity.append(quantity)
                    only_price.append(price)
                else:
                    print("Selected item is not available...Sorry for the inconvenience")
        if total_price>0:
            tax=(total_price*12)/100
            final_amount=total_price+tax
            print(30*"=","PythonLife SuperMarket",30*"=")
            print(35*" ","Hyderabad",35*" ")
            print(f"Name: ",name,30*" ")
            print(80*"-")
            print("sno",10*" ",'items',8*" ",'quantity',8*" ",'price')
            for i in range(len(price_list)):
                print(i,13*" ",only_items[i],8*" ",only_quantity[i],8*" ",only_price[i])
            print(75*"-")
            print(50*" ",'Total amount:','RS',total_price)
            print('Tax amount:',52*" ",'RS',tax)
            print(75*"-")
            print(50*" ",'Final amount:','RS',final_amount)
            print(75*"-")
            print(20*" ","Thank you & Visit Again")
            print(75*"-")
                
                
                
            
                
    
    
    
    
    
    
    