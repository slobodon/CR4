#Define the class

class ItemToPurchase:
    def __init__(self):
        self.item_name ='none'
        self.item_price=0
        self.item_quantity =0
    
    def __str__(self):
        return '{} {} @ ${} = ${}'.format(self.item_name, int(self.item_quantity), float(self.item_price),int(self.item_quantity) * float(self.item_price) ).center(50)
    
  #set the number of items parameter to 2 and initialize lists
N=2
itemList=[]
priceList=[]
quantityList=[]

#prompt for inputs and recieve the inputs

for i in range(N):
    print('Item {}'.format(i+1).center(50))
    itemList.append(input('Enter the item name:\n'.center(50)))
    priceList.append(input('Enter the item price:)\n'.center(50)))
    quantityList.append(input('Enter the item quantity)\n'.center(50)))

#output resuits
print('TOTAL COST'.center(50))



for j in range(N):
     item = ItemToPurchase()
     item.item_name= itemList[j]
     item.item_price = priceList[j]
     item.item_quantity =quantityList[j]
     print(item)


Total = 0
for k in range(N):
	Total += int(priceList[k])* float(quantityList[k])
print('TOTAL:${}'.format(Total).center(50))


#print(itemList)
#print(priceList)
#print(quantityList)

#SEt the value of the class