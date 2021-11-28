import os
import random
import time

money = 1000
chance = 51
once = 1
help = 0
get_tip = 0

print("You have entered a casino and you decide to sit down at a wheel spin game.")
print("You are starting off with " + str(money) + "$, good luck!")
time.sleep(5)

continue_game = True 

while continue_game == True:
    placed_num = -1
    bet = -1
    buy_powerup = 0

    if money <= 500 and money >= 100 and once == 1:
        time.sleep(2)
        try:
            buy_powerup = input("You only have half of your starting money left, would you like to increase your chance of winning by purchasing a powerup for 100$? \n Yes = 1 No = 2: ")
        except ValueError:
            ("You must enter 1 or 2!")
        
        if buy_powerup == "1" and money >= 100:
            once = 0
            chance = 31
            money -= 100
            print("Cool, you now have " + str(money) + "$ left")
        
        elif buy_powerup == "2":
            once = 0
        


            



    while placed_num < 0 or placed_num > chance:

        if help == 5:
            tip = input("It seems like you've been having some trouble, would you like to buy a tip for 50$ \n Yes = y No = n: ")

            if tip == "y":
                help = 0
                money -= 50 
                get_tip = 1
                print("Ok cool")      
            elif tip == "n":
                get_tip == 0
        
        if get_tip == 0:
            for n in range(1, chance):
                print("| " + str(n) + " |" )
                time.sleep(0.01)
            try:
                placed_num = int(input("On which number do you want to bet money (in between 0 and " + str(chance - 1) + "): "))
            except ValueError:
                print("Invalid number")

            if placed_num < 0:
                print("number is too small")
            
            elif placed_num > 50:
                print("number is too big")
        
            while bet > money or bet < 1:
                try:
                    bet = int(input("How much would you like to bet: "))
                except ValueError:
                    print("Invalid number")
                
                if bet > money:
                    print("You do not have enough money")
                
                elif bet < 1:
                    print("You have to bet more than this")
            
            spin = random.randint(0, chance)
            print("And the winning number is...")
            time.sleep(3)
            print(spin)
            time.sleep(2)

        elif get_tip == 1:
            spin = random.randint(0, chance)
            by = random.randint(1, 5)
            less = spin - by
            more = spin + by
            print("Tip: the number will be in between " + str(less) + " and " + str(more) + ".") 
            time.sleep(3)
            for n in range(1, chance):
                print("| " + str(n) + " |" )
                time.sleep(0.01)
            try:
                placed_num = int(input("On which number do you want ot bet money on: "))
            except ValueError:
                print("Invalid number")
            
            if placed_num < 0:
                print("number is too small")
            
            elif placed_num > 50:
                print("number is too big")
        
            while bet > money or bet < 1:
                try:
                    bet = int(input("How much would you like to bet: "))
                except ValueError:
                    print("Invalid number")
                
                if bet > money:
                    print("You do not have enough money")
                
                elif bet < 1:
                    print("You have to bet more than this")

            print("And the winning number is...")
            time.sleep(3)
            print(spin)
            time.sleep(2)
            get_tip = 0



    if placed_num == spin:
        help = 0
        money += bet * 50
        print("CONGRATULATIONS!!! YOU WON \n You now have " + str(money) + "$")
    
    elif placed_num != spin:
        money -= bet
        help += 1
        print("Sorry, you get nothing. \n You now have " + str(money) + "$")
        if money <= 0:
            play_again = input("It seems you have run out of money, would you like to play again? y = yes, n = no: ")

            if play_again == "y":
                money = 1000
                print("COOL, you now have 1000$ dollars again")
                continue_game = True
        
            elif play_again == "n":
                print("Ok bye")
                continue_game = False
                os.sys.exit