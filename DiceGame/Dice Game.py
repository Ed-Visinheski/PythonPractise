import time
import random
pp1 = 0
pp2= 0
ptie1 = 0
ptie2 = 0
wpoints = 0
points=0
rnumb=1
trnumb=1

def roll():#def is used as a code shortcut
    roll1 = random.randint(1, 6)#Acts as a die, randomly selects an integer from 1-6 and stores its value
    print('1st Roll:',roll1,' points were added')#states how many points that roll added
    time.sleep(1)#Makes program wait certain ammount of time. In this code it has to wait 1 second before continuing
    roll2 = random.randint(1, 6)#Acts as the second die
    print('2nd Roll:',roll2,' points were added')
    time.sleep(1)
    if (roll1 + roll2) % 2 == 0:#calculates if its even or odd
        diff = 10
        print('EVEN TOTAL:',diff,'points were added')
        time.sleep(1)
        points = roll1 + roll2 + diff#if its even it adds 10 points
    else:
        diff = -5
        print('ODD TOTAL:',diff,' points were removed')
        time.sleep(1)
        points = roll1 + roll2 + diff#if its odd it adds -5 points
    if roll1 == roll2:#calculates if the roll is a double
        roll3 = random.randint(1, 1)
        print('DOUBLE ROLL:',roll3,'points were added')
        time.sleep(1)
        points = points + roll3#adds the third roll to the rest
    if points <0:
        points = 0#Makes it so you cant get a negative code
        
    return points


def tieroll():
    troll = random.randint(1, 6)#rolls only when it ties
    return troll

print("Welcome to Eduardo's 2 player dice game!")
print('')
time.sleep(1)#Makes program wait certain ammount of time. In this code it has to wait 1 second before continuing
print("(If you can't remember your account use Guest1 as your username + password)")
time.sleep(1)
print ("User1 please login to continue")
time.sleep(1)
username = input('Type in your username: ')#Makes have to type in their username before continuing
time.sleep(0.5)
password = input('Type in your password: ')
time.sleep(0.5)
print('')


#Authentication code for User1

while username == username and password == password:

    if username == 'Guest1' and password == 'Guest1': #correct username and password
        print("Welcome! ")
        break

    if username == 'Ed' and password == 'Dog': 
        print("Welcome! ")
        break

    if username == 'Pat' and password == 'Goat': 
        print("Welcome! ") 
        break

    if username == 'Sam' and password == 'Horse': 
        print("Welcome! ") 
        break

    if username == 'Obi' and password == 'Chicken': 
        print("Welcome! ") 
        break

    elif username != 'Guest1' and password != 'Guest1': #wrong username and password
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username == 'Guest1' and password != 'Guest1': #wrong password
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Guest1' and password == 'Guest1': #wrong username
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue


    elif username != 'Ed' and password != 'Dog': 
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username == 'Ed' and password != 'Dog': 
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Ed' and password == 'Dog': 
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Pat' and password != 'Goat': 
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username == 'Pat' and password != 'Goat': 
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue
    elif username != 'Pat' and password == 'Goat': 
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Sam' and password != 'Horse': 
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username == 'Sam' and password != 'Horse': 
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Sam' and password == 'Horse': 
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username != 'Obi' and password != 'Chicken': 
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username == 'Obi' and password != 'Chicken': 
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue
    elif username != 'Obi' and password == 'Chicken': 
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    
print ("User2 please login to continue")
time.sleep(1)
print("(If you can't remember your account use Guest2 as your username + password)")
time.sleep(1)
username2 = input('Type in your username: ')
time.sleep(0.5)
password2= input('Type in your password: ')
time.sleep(0.5)
print('')

#Authentication code for User2


while username2 == username2 and password2 == password2:


    if username2 == 'Guest2' and password2 == 'Guest2': #correct username and password
        print("Welcome! ")
        break
    
    if username2 == 'Ed' and password2 == 'Dog': 
        print("Welcome! ") 
        break

    if username2 == 'Pat' and password2 == 'Goat': 
        print("Welcome! ") 
        break

    if username2 == 'Sam' and password2 == 'Horse': 
        print("Welcome! ") 
        break

    if username2 == 'Obi' and password2 == 'Chicken': 
        print("Welcome! ") 
        break

    elif username2 != 'Guest2' and password2 != 'Guest2': #wrong username and password
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue 

    elif username2 == 'Guest2' and password2 != 'Guest2': #wrong password
        print("Your Password is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue
    elif username2 != 'Guest2' and password2 == 'Guest2': #wrong username
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ") 
        password = input("Password: ") 
        continue

    elif username2 != 'Ed' and password2 != 'Dog': 
        print("Your Username and Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue 

    elif username2 == 'Ed' and password2 != 'Dog': 
        print("Your Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Ed' and password2 == 'Dog': 
        print("Your Username is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Pat' and password2 != 'Goat': 
        print("Your Username and Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue 

    elif username2 == 'Pat' and password2 != 'Goat': 
        print("Your Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Pat' and password2 == 'Goat': 
        print("Your Username is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Sam' and password2 != 'Horse': 
        print("Your Username and Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue 

    elif username2 == 'Sam' and password2 != 'Horse': 
        print("Your Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Sam' and password2 == 'Horse': 
        print("Your Username is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue

    elif username2 != 'Obi' and password2 != 'Chicken': 
        print("Your Username and Password is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue 

    elif username2 == 'Obi' and password2 != 'Chicken': 
        print("Your Password is wrong!") 
        userName = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue
    
    elif username2 != 'Obi' and password2 == 'Chicken': 
        print("Your Username is wrong!") 
        username2 = input("\n\nUsername: ") 
        password2 = input("Password: ") 
        continue


if username == username2:#Same usernames and password for user1 and user2 the game will close - this is a form of cheating
    print ("You can't use the same account for both users!")
    time.sleep(2)
    exit()#game closing
else:
    print('Welcome User1 and User2')
    time.sleep(1)

print('Press "e" for an explanation on how the game works')
explanation = input('Or press "Enter" to skip: ')

while explanation == explanation:
    if explanation == 'e':
        print('This is a quick explanation on the game works!')
        time.sleep(1)
        print('')
        print("WARNING- This Game is automatic")
        print("All you'll have to do is sit back and enjoy!")
        print('')
        time.sleep(1)
        print('EVEN TOTAL- An even total will give you an extra 10 points')
        print('')
        time.sleep(1)
        print('ODD TOTAL- An odd total will remove 5 points')
        print('')
        time.sleep(1)
        print('DOUBLE ROLL- When you get the same number on both rolls; this will give you an extra third roll')
        print('')
        time.sleep(1)
        print("If you get a tie... Well you'll have to find that out for yourself")
        print('')
        time.sleep(1)
        print('Also dont forget to be competetive and get No.1 on the leaderboard')
        print('')
        time.sleep(1.5)
        print (input('Press "Enter" to start the Game'))
        print('')
        break  
    elif explanation != 'e':
        print('You have skipped the explanation!')
        print('')
        time.sleep(0.5)
        print (input('Press "Enter" to start the Game'))
        print('')
        break
    

print('Game starting in...')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GO!')
print('')
print('-------------------------------------------------------------')

    

for i in range(1,6):#makes it 5 rounds
    pp1 += roll()#player 1 roll
    print('-')
    print('Round',rnumb,':',username, 'you now have: ',pp1,' Points.')
    print('')
    print('')
    time.sleep(1)
    pp2 += roll()#player 2 roll
    print('-')
    print('Round',rnumb,':',username2,'you now have: ',pp2,' Points')
    time.sleep(1)
    print('')
    print('-------------------------------------------------------------')
    rnumb = (rnumb + 1)


if pp1>pp2 and pp1 != pp2:#calculates the winner
    endpoints = pp1
    winner_calc = (endpoints, username)
    winner = username
    print('Well done, ',winner,' you won with ',endpoints,' Points')
elif pp2>pp1 and pp1 != pp2:#calculates the winner
    endpoints = pp2
    winner_calc = (endpoints, username2)
    winner = username2
    print('Well done, ',winner,' you won with ',endpoints,' Points')

else:
    print('~~~~~~~~~~~~~IT LOOKS LIKE THERES A TIE~~~~~~~~~~~~~~~~~~')
    print('-------------------------------------------------------------')
    print('')
    print('THE GAME MUST GO ON')
    time.sleep(1)
    print('You two will only roll one die and the game will continue until a winner is decided')
    time.sleep(1)
    print('Game starting in...')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('GO!')
    
    

while pp1==pp2:#calculates if there is a tie or not
    ptie1 += tieroll()
    print('-')
    print('TIE ROUND',trnumb,':',username, 'you now have: ',ptie1,' Points.')
    print('')
    print('')
    time.sleep(1)
    pp1 += ptie1
    ptie2 += tieroll()
    print('-')
    print('TIE ROUND',trnumb,':',username2,'you now have: ',ptie2,' Points')
    time.sleep(1)
    pp2 += ptie2
    print('')
    print('------------------------------------------------------------')
    trnumb = (trnumb + 1) 

if ptie1>ptie2 and ptie1 != ptie2:#calculates the winner with the tieing points
    endpoints = ptie1
    winner_calc = (endpoints, username)
    winner = username
    print('Well done, ',winner,' you won with ',endpoints,' Points')
elif ptie2>ptie1 and ptie1 != ptie2:
    endpoints = ptie2
    winner_calc = (endpoints, username2)
    winner = username2
    print('Well done, ',winner,' you won with ',endpoints,' Points')

#received help from student in my class for the leaderboard
#writes the final scores in txt file named leaderboard
finalscore = open('finalscore.txt', 'a')
finalscore.write(username)#writes the username of User1
finalscore.write(', ')
finalscore.write(str(pp1))#writes User1 scores in the txt file
finalscore.write('\n')#seperates user 1 and 2
finalscore.write(username2)#writes the username of User2
finalscore.write(', ')
finalscore.write(str(pp2))#writes User2 scores in the txt file
finalscore.write('\n')
finalscore.close()


scorelist = []
with open("finalscore.txt", 'r') as file:#opens leaderboard file and reads top 5 scores
    scorelist = []
    for line in file:
        scorelist.append(line[0:-1].split(","))
        scorelist.sort(key=lambda x: int(x[1]))
scorelist.reverse()
print('')
print("TOP 5 SCORES:")
#shows top 5 scores
print('1.',scorelist[1])
print('2.',scorelist[2])
print('3.',scorelist[3])
print('4.',scorelist[4])
print('5.',scorelist[5])

print('')
print (input('Press "Enter" to end the Game: '))
exit()#Closes the game
