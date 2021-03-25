file1 = open("Bills.txt","a") 
import datetime

time = datetime.datetime.now()

print(f'\t\t\t\t\t\t\t\t{time}\n\n')

date = [f'{time} \n']
file1.writelines(date)
print('\n')
net = 0

while True :
    print('\n')
    product = input('Enter the name of the Prouct :- ')
    if product != 'q' and product != 'Q':
        buy = input('Enter the buying price of the Product :- ')
        if buy != 'q' and buy != 'Q':
            quantity = input('Ente the Quantity of Product :- ')
            if quantity != 'q' and quantity != 'Q':
                total = float(buy)*float(quantity)
                net = total+net


                L = [f"\t\t\t\t\t\t\t\tProduct : {product} \n", f"Price : {buy} \n", f"Quantity : {quantity} \n", f"Total : {total} \n" f"Net : {net} \n\n"]  
        
                file1.writelines(L) 
            else:
                print('\n')
                file1.close()
                file1 = open("Bills.txt","r+")  
                print(file1.read()) 
                close = input()
                break

        else:
            print('\n')
            file1.close()
            file1 = open("Bills.txt","r+") 
            print(file1.read())
            close = input()
            break

    else:
        print('\n')
        file1.close()
        file1 = open("Bills.txt","r+")  
        print(file1.read())
        close = input()
        break

