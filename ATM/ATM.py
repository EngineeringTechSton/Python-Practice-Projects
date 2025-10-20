# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 23:11:49 2025

@author: MALIK COMPUTERS
"""


import pygame

import time
import keyboard
pygame.mixer.init()
pygame.mixer.music.load("atm.mp3")
print("Welcome to HBL Bank...")
print("           💵HBL ATM🏧")
print("Enter your atm card (Press Enter to continue...)")
print("            Quit: Esc")
a=keyboard.read_key()
if a=='enter':
    acc=input("Enter The Account name:___ ")
    if acc=="Farhan Shakeel":
        print("Now enter your pin code:  ***** ")
        pin=int(input("PIN:_____"))
        if pin==69941:
            print("Account accessed $ ....")
            balance=50000
            print('Your account balance is', balance)
            new_op=input("Press Key:###\nWithdraw: W\nDeposit: D\n").lower()
            if new_op=='w':
                print("           HBL ATM")
                print("Enter the amount you wanna withdraw: ")
                w_amount=int(input('Withdraw Amount: $ '))
                if w_amount>balance:
                    print("Your Balance is LOW")
                    print('Please take you card.........') 
                else:
                    balance-=w_amount
                    print("Transaction is in process.....")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    print("💲💲💰")
                    print('Now account balance is', balance)  
                    time.sleep(1.6)
                    print("Thank You for using ATM ......")
            elif new_op=='d': 
                print("Enter The amount You wanna Deposit: ")
                amount=int(input('Rs: '))
                if amount<1000:
                    print("Amount less than 1000 can't be deposit.")
                elif amount >=1000:
                    balance+=amount
                print("Depositing........")
                time.sleep(3)
                print('Now account balance is', balance)
                print("Thank you for Depositing Money")                   
                   
        else:
            print("Incorrect pin.....")
    elif acc=="Muhammad Shakeel":
        print("Now enter your pin code:  ***** ")
        pin=int(input("PIN:_____"))
        if pin==00000:
            print("Account accessed $ ....")
            balance=100000
            new_op=input("Press Key:###\nWithdraw: W\nDeposit: D\n").lower()
            if new_op=='w':
                print("           HBL ATM")
                print("Enter the amount you wanna withdraw: ")
                w_amount=int(input('Withdraw Amount: $ '))
                if w_amount>balance:
                    print("Your Balance is LOW")
                    print('Please take you card.........') 
                else:
                    balance-=w_amount
                    print("Transaction is in process.....")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    print("💲💲💰")
                    print('Now account balance is', balance)  
                    time.sleep(1.6)
                    print("Thank You for using ATM ......")
            elif new_op=='d': 
                print("Enter The amount You wanna Deposit: ")
                amount=int(input('Rs: '))
                if amount<1000:
                    print("Amount less than 1000 can't be deposit.")
                elif amount >=1000:
                    balance+=amount
                print("Depositing........")
                time.sleep(3)
                print('Now account balance is', balance)
                print("Thank you for Depositing Money")             
        else:
            print("Incorrect pin.....")
    elif acc=="Muhammad Sufyan":
        print("Now enter your pin code:  ***** ")
        pin=int(input("PIN:_____"))
        if pin==12345:
            print("Account accessed $ ....")
            balance=6000
            print('Your account balance is', balance)
            new_op=input("Press Key:###\nWithdraw: W\nDeposit: D\n").lower()
            if new_op=='w':
                print("           HBL ATM")
                print("Enter the amount you wanna withdraw: ")
                w_amount=int(input('Withdraw Amount: $ '))
                if w_amount>balance:
                    print("Your Balance is LOW")
                    print('Please take you card.........') 
                else:
                    balance-=w_amount
                    print("Transaction is in process.....")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    print("💲💲💰")
                    print('Now account balance is', balance)  
                    time.sleep(1.6)
                    print("Thank You for using ATM ......")
            elif new_op=='d': 
                print("Enter The amount You wanna Deposit: ")
                amount=int(input('Rs: '))
                if amount<1000:
                    print("Amount less than 1000 can't be deposit.")
                elif amount >=1000:
                    balance+=amount
                print("Depositing........")
                time.sleep(3)
                print('Now account balance is', balance)
                print("Thank you for Depositing Money")             
        else:
            print("Incorrect pin.....")   
    elif acc=="Muhammad Zaid":
        print("Now enter your pin code:  ***** ")
        pin=int(input("PIN:_____"))
        if pin==98765:
            print("Account accessed $ ....")
            balance=2800
            print('Your account balance is', balance)
            new_op=input("Press Key:###\nWithdraw: W\nDeposit: D\n").lower()
            if new_op=='w':
                print("           HBL ATM")
                print("Enter the amount you wanna withdraw: ")
                w_amount=int(input('Withdraw Amount: $ '))
                if w_amount>balance:
                    print("Your Balance is LOW")
                    print('Please take you card.........') 
                else:
                    balance-=w_amount
                    print("Transaction is in process.....")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    print("💲💲💰")
                    print('Now account balance is', balance) 
                    time.sleep(1.6)
                    print("Thank You for using ATM ......")
            elif new_op=='d': 
                print("Enter The amount You wanna Deposit: ")
                amount=int(input('Rs: '))
                if amount<1000:
                    print("Amount less than 1000 can't be deposit.")
                elif amount >=1000:
                    balance+=amount
                print("Depositing........")
                time.sleep(3)
                print('Now account balance is', balance)
                print("Thank you for Depositing Money")             
        else:
            print("Incorrect pin.....")    
elif a=="esc":
    print("Plesase!  Take your Card ")
