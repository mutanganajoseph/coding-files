import random
import os
import time


def spin_row():
    print("\n")
    symbols =['🍏','🥕','🍒','🍉','⭐','🔔']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))



def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍏':
            return bet * 100
        elif row[0] == '🥕':
            return bet * 15
        elif row[0] == '🍒':
            return bet * 20
        elif row[0] == '🍉':
            return bet * 50
        elif row [0] == '⭐':
            return bet * 250
        elif row[0] == '🔔':
            return bet * 200
        
    return 0
    


def main():

    balance = 100

    print('**************************')  
    print('Welcome to python slots!') 
    print('**************************') 

    print('*******************************')  
    print('symbols: 🍒 🍍 🍏 ⭐ 🍉 🥕 🔔')
    print('*******************************')  

    
    while balance >0:
         print('\n*******************************')  
         print(f'Current balance: ${balance}')
         print('************************** \n')


         bet = input("place your bet amount:$ ")

         if not bet.isdigit():
            print("\nPlease Enter Valid value \n")
            continue

         bet = int(bet)

         if bet > balance:
            print("\nInsufficient founds \n")
            continue

         if bet <=0:
            print("\nBet must be greater than 0\n" )
            continue

         balance -= bet     

         row = spin_row()
         
         print("Spinning...\n")

         print_row(row)

         payout = get_payout(row, bet)

         if payout > 0:
            print (f" \nYou won this round! you received: ${payout}")

         else:
            print(f"\nYou lost this round.")

         
         balance += payout
         

         #choice = input("\nDo you want to Continue Y/N: ").upper()
         #if choice != 'Y':
          #  break   
         



if __name__ =='__main__':
    main()  

 