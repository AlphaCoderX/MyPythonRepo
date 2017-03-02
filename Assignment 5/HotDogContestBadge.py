#Programmer Raphael Heinen
#Date 3/1/17
#Version 1.0
import functions
import random
import time
#generates hot dogs for players to
#eat and then returns the winner
def hotdogs():
    
    eating = True
    winner = ""
    
    players = ["Tom", "Sally", "Fred"]
    hotdogs = [0,0,0]
    
    while eating:
        print "chomp... chomp... chomp...\n"
        sallyT = random.randrange(1,7)
        tomT= random.randrange(1,7)
        fredT= random.randrange(1,7)
        
        hotdogs[1] +=sallyT
        hotdogs[2] += fredT
        hotdogs[0] +=tomT

        
        time.sleep(1)
        print "Tom has eaten %s hotdogs:" %hotdogs[0]
        print "Sally has eaten %s hotdogs:" %hotdogs[1]
        print "Fred has eaten %s hotdogs:" %hotdogs[2]
        
        if max(hotdogs) >= 50:
            eating = False
            num = hotdogs.index(max(hotdogs))
            winner = players[num]
            
    return winner
        
#prompts the user for a winner and bet
#also keeps track of users money and
#prints the winner
def guess():
    
    wallet = 100
    on = True;
    
    while on:
        guess = functions.userString("Pick a winner(Tom, Sally, Fred)")
        bet = functions.userInt("How much do you want to bet (cash = %s):" %wallet) 

        print "Ready, set eat!"
        time.sleep(3)
        win = hotdogs()
    
        if guess == win:
            wallet = wallet + bet
            print "You guessed right, %s wins! (cash = %s)" % (win, wallet)
            
            
        else:
            wallet = wallet - bet
            print "Nice try! The top dog was actually %s (cash = %s)" % (win, wallet)
            
            
            if wallet <= 0:
                on = False
            
    
            
def main():
    guess()        
    
main()
