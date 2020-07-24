# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:42:19 2020

@author: Arka Das
"""
print("*************************\nWelcome\n")
budget=int(input("Enter budget(0<budget<10000) in Rupees:"))

a=[" "]
b=[0]
listname=["Biscuits(1 Packet)","Cold Drink","Lays(Potato Chips)","Chocolate(100g)","Juice(1 ltr)","Noodles(Pack of 6)","Raisins(500g)","Muffins(Pack of 9)"]
listprice=[20,30,40,50,70,85,100,160]
minimuminlist=20
while budget>0:
    choice=int(input("Enter your choice:\n 1-Add an item\n 2-Exit\n"))
    if(choice==1 ):
        name=input("Enter name of item which you wish to add to cart: ")
        price=int(input("Enter price of item which you wish to add to cart: "))
        if(budget-price>=0):
            a.append(name)
            b.append(price)
            budget=budget-price;
        elif budget>=20:
            
            item="generic"
            
            price=40
            i=0
            f=0
            print("Price of product is greater than your remaining budget Rs. "+str(budget)+"\nSo you can buy the following item(s):--\n")
            for i in range(0,8):
                if(budget>listprice[i]) :
                    price=listprice[i]    
                    item=listname[i]
                    print(str(i+1)+". "+ item+"  of price Rs."+str(price)+"\n")        
            
                
            print("\nWhich one would you like to? 0-if u wish to choose nothing\n")
            
            choice1=int(input())
            if(choice1==0):
                break
            else:
                
                a.append(listname[choice1-1])
                b.append(listprice[choice1-1])
                budget=budget-listprice[choice1-1];
                break    
    elif(choice==2):
        
        break;
    else:
        print("Choice is invalid\n")
    print("\nAmountRemaining: Rs. "+str(budget)+"\n")  
print("\n*************************\n")    
for i in range(1,len(b)):
    print("\n"+str(i)+". "+a[i]+" Rs. "+str(b[i]))
print("\nAmountRemaining: Rs. "+str(budget))    
print("\n*************************\nThank you. \n")    