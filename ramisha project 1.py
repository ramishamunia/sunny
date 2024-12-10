print("Welcome to Boimela")
item_dict={}
f=open("F:/pp-08/booksdata.txt","r")
while True:
    item=f.readline()
    if item=='':
        break
    quant=f.readline()
    uprice=f.readline()
    item=item[:len(item)-1]
    quant=int(quant[:len(quant)-1])
    uprice=float(uprice[:len(uprice)-1])
    item_dict[item]=[quant,uprice]
f.close()
maxlen=60
itlen=42
def show_dict():
    print(maxlen*"=")
    print("Available Itams and Quantity")
    print(maxlen*"=")      
    for x in item_dict:
         print(x,(itlen-len(x))*" ",
               (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(maxlen*"-")

def dec_quant(key,val):
    item_dict[key][0]-=val
    
def inc_quant(key,val):
    item_dict[key][0]+=val
    
def receive_order():
    print("Order Received")
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        value=int(input("Quantity:"))
        if item not in item_dict:
            print("New item Found!")
            uprice = float(input("Unit Price:"))
            item_dict[item] = [value,uprice]
            continue
        inc_quant(item,value)
    
def process_demand():
    print("Order Received")
    # demand_list =
    demand_list = []
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        if item not in item_dict:
            print(f"The item '{item}' is not available!")
            continue
        value=int(input("Quantity:"))
        if value>item_dict[item][0]:
            print(f"Total of {item_dict[item][0]} pcs are available!")
            continue
        dec_quant(item,value)
        demand_list+=[item,value,
                      item_dict[item][1],value*item_dict[item][1]],
    #printing the payment receipt    
    print(maxlen*"=")
    print("** payment Receipt **".center(maxlen))
    print(maxlen*"=")
    print("Item",7*" ","Quant"," ","U.price",2*" ","S.Total")
    print(maxlen*"-")
    tprice = 0
    for x in demand_list:
        tprice+=x[3]
        print(x[0].title(),(itlen-9-len(x[0]))*" ",
              (4-len(str(x[1])))*" ",x[1],
              (7-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
              (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(maxlen*"-")
    print("Total Price:"," ",tprice)
    print(maxlen*"-")      
    #show_dict()    
    
while True:
    show_dict()
    print("Choose an option:")
    print("Type '1': To process demand")
    print("Type '2': To process order")
    print("Type '3': To exit the program")
    choice = input("choice: ")
    if choice=='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue
f=open("F:/pp-08/booksdata.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.close()




















