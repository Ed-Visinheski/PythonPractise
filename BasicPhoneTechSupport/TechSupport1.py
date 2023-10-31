import webbrowser
import sys
import time
import random
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )# It delays the text letter by letter
        sys.stdout.flush()
        time.sleep(0.015)

a1 = ('Unfortunately we could not find what is wrong with your phone. We recommend to taking it to a specialist or the phone provider.')#solutions
a2 =('We recommend to taking it to a specialist or a repair shop')

delay_print ('Welcome to the Interactive Phone Troupleshooting System version 1.8')
print('')
time.sleep(1)
rnd = (int(random.randrange(50)) *50 + 123141235134)#random number generator
print("Your Case Number is", str(rnd))
time.sleep(1)#waits 1 second before continuing



while True:
    def apple():#all the code and questions for Apple
        q1 = None
        while q1 not in ('software','hardware'):
            q1 = input('Is it a software or hardware issue?')
            q2 = None
            q3 = None
            q4 = None
            if q1 == 'software':#if chosen software then it will ask these questions
                while q2 not in ('yes','no'):
                    q2 = input('Does your iPhone still turn on? Yes or No?')#input allows user to type
            if q2 == 'yes':#if user typed yes ...
                while q3 not in ('yes','no'):
                    q3 = input('Has your iPhone been slow?')#Next Question

            elif q2 == 'no':#if user typed no...
                print("Try hoolding down the power button. If that doesn't work you should contact the iPhone provider or the Apple store.")#responce/solution
                while q3 not in ('yes','no'):
                    q3 = input('Has your iPhone been slow?')#Next Question

            if q3 == 'yes':
                print("If your iPhone has been slow, try deleting some apps and closing tabs")
                while q4 not in ('yes','no'):
                    q4 = input("Has your iPhone been acting strange?")
            elif q3 == 'no':
                while q4 not in ('yes','no'):
                    q4 = input("Has your iPhone been acting strange?")
            if q4 == 'yes':
                print("You most likely have a bug/virus. Try installing anti virus software or updating your IOS to the newest vesion.")
            elif q4 == 'no':
                print(a1)

            elif q1 == 'hardware':#if chosen hardware then it will ask these questions
                q5 = None
                while q5 not in ('yes','no'):
                    q5 = input('Is your Iphone screen cracked?')
                if q5 == 'yes':
                    print('You should get your phone screen fixed or the phone might not operate properly')
                    print(a2)
                    q6 = None
                    while q6 not in ('yes','no'):
                        q6 = input ('Is your phone Charging?')
                elif q5 == 'no':
                    q6 = None
                    while q6 not in ('yes','no'):
                        q6 = input ('Is your phone Charging?')
                if q6 == 'yes':
                    q7 = None
                    while q7 not in ('yes','no'):
                        q7 = input('Does your phone have a faulty buttons?')

                elif q6 == 'no':
                    print('Check if your cable is broken. If it is then buy a new one but if it isnt the charging port or battery is broken')
                    print(a2)
                    q7 = None
                    while q7 not in ('yes','no'):
                        q7 = input('Does your phone have faulty buttons?')
                if q7 == 'yes':
                    print('If your phone buttons are faulty or unresponsive you can find software solutions. Of course you can always get it physicaly repared from your manufactured or from a repair shop for a cheaper price.')
                    q8 = None
                    while q8 not in ('yes','no'):
                        q8 = input('Has your phone been in contact with Water?')
                elif q7 == 'no':
                        q8 = None
                        while q8 not in ('yes','no'):
                            q8 = input('Has your phone been in contact with Water?')
                if q8 == 'yes':
                    print ('TURN OFF YOUR PHONE IMMEDIATELY. Put your phone in a bag of rice for 48 hours, many silica gel packets and placing them in a zip lock with your phone or even a Bheestie bag.')
                elif q8 == 'no':
                    print(a1)

    def android(): #All code and questions for android
        q9 = None
        while q9 not in ('software','hardware'):
            q9 = input('Is it a software or hardware issue?')
            q10 = None
            q11 = None
            q12 = None
            if q9 == 'software':#if chosen software then it will ask these questions
                while q10 not in ('yes','no'):
                    q10 = input('Does your phone still turn on? Yes or No?')
            if q10 == 'yes':
                while q11 not in ('yes','no'):
                    q11 = input('Has your phone been slow?')

            elif q10 == 'no':
                print("Try hoolding down the power button. If that doesn't work you should contact the phone provider or the Samsung store(if you have a Samsung).") 
                while q11 not in ('yes','no','Yes','No'):
                    q11 = input('Has your phone been slow?')

            if q11 == 'yes':
                print("If your iPhone has been slow, try deleting some apps and closing tabs")
                while q12 not in ('yes','no'):
                    q12 = input("Has your phone been acting strange?")
            elif q11 == 'no':
                q12 = None
                while q12 not in ('yes','no'):
                    q12 = input("Has your phone been acting strange?")
            if q12 == 'yes':
                print("You most likely have a bug/virus. Try installing anti virus software or updating your IOS to the newest vesion.")
            elif q12 == 'no':
                print(a1)

            elif q9 == 'hardware':#if chosen hardware then it will ask these questions
                q13 = None
                while q13 not in ('yes','no'):
                    q13 = input('Is your phone screen cracked?')
                if q13 == 'yes':
                    print('You should get your phone screen fixed or the phone might not operate properly')
                    print(a2)
                    q14 = None
                    while q14 not in ('yes','no'):
                        q14 = input ('Is your phone Charging?')
                elif q13 == 'no':
                    q14 = None
                    while q14 not in ('yes','no'):
                        q14 = input ('Is your phone Charging?')
                if q14 == 'yes':
                    q15 = None 
                    while q15 not in ('yes','no'):
                        q15 = input('Does your phone have a faulty buttons?')
                elif q14 == 'no':
                    print('Check if your cable is broken. If it is then buy a new one but if it isnt the charging port or battery is broken')
                    print(a2)
                    q15 = None
                    while q15 not in ('yes','no'):
                        q15 = input('Does your phone have faulty buttons?')
                if q15 == 'yes':
                    print('If your phone buttons are faulty or unresponsive you can find software solutions. Of course you can always get it physicaly repared from your manufactured or from a repair shop for a cheaper price.')
                    q16 = None
                    while q16 not in ('yes','no'):
                        q16 = input('Has your phone been in contact with Water?')
                elif q15 == 'no':
                        q16 = None
                        while q16 not in ('yes','no'):
                            q16 = input('Has your phone been in contact with Water?')
                if q16 == 'yes':
                    print ('TURN OFF YOUR PHONE IMMEDIATELY. Put your phone in a bag of rice for 48 hours, many silica gel packets and placing them in a zip lock with your phone or even a Bheestie bag.')
                elif q16 == 'no':
                    print(a1)#prints set solution
                        
            
                         
    os = input('Do you have an Apple or Android phone?')
    if os == 'apple':
        apple() #runs all apple code from above
        Web = input('Would you like to visit the Apple Support page?')
        if Web == 'yes':
            webbrowser.open('https://support.apple.com/en-gb') #end of questions and webbrowser.open opens support site
            break #ends program
        elif Web == 'no':
            print ("If you have any more questions we would be glad to help you!")
            break

    elif os == 'android':
        android()#plays all android code from above
        Web = input ('Would you like to visit the Samsung Support page?')
        if Web == 'yes':
            webbrowser.open('https://www.samsung.com/uk/support/service-centre/')
            break
        elif Web == 'no':
            print ("If you have any more questions for me I would be glad to help you!")
            break
            
    
