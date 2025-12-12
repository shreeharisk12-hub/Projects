
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        money = input("Enter the amount you want to play with: $")
        if(money.isdigit()):
            money = int(money)
            break
        else:
            print("Enter a valid number")
    return money

def NumberOfLines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1 - {MAX_LINES}): ")
        if(lines.isdigit()):
            lines = int(lines)
            if(1 <= lines <= MAX_LINES):
                break
            else:
                print(f"Enter between (1 - {MAX_LINES})")
        else:
            print("Enter a valid number")
    return lines

def bettings():
    while True:
        bet = input(f"Enter the bet on each line (${MIN_BET} - ${MAX_BET}): ")
        if(bet.isdigit()):
            bet = int(bet)
            if(MIN_BET <= bet <= MAX_BET):
                break
            else:
                print(f"Enter between (${MIN_BET} - ${MAX_BET})")
        else:
            print("Enter a valid number")
    return bet

user = input("Enter your name : ")

def main():
   amount = deposit()
   lines = NumberOfLines()
   while True:
       bet = bettings()
       total_bet = bet*lines
       if total_bet > amount :
           print(f"{user}, you dont have enough balance. Your current balance is ${amount}")
       else:
           break
        
   print(f"{user}, you are betting ${bet} on {lines} lines. Total bet : ${total_bet}")

main()
