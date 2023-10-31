import time
import random
import sys
print ("Welcome to the Interactive Phone Troupleshooting System version 3.8")
time.sleep(0.5)
rnd = (int(random.randrange(50)) *50 + 123141235134)#random nummber
print("Your Case Number is", str(rnd))
time.sleep(0.5) #waits 0.5 seconds before moving on to the next text

while True:# repeats the question until a valid answer is typed
#all of the code for the phones
    def phone():#if "phone()" is typed then this code will run
        print('Please select the type of phone you have.')#Displays question on the user's screen
        print('1. iPhone')
        print('2. Samsung')
        print('3. OnePlus')
        ptype = input ('Please select 1, 2 or 3    ')#allows user to answer and stores the answer into a variable
        if ptype == '1':# if the answer is 1 
            iphone()#moves on to the next question
        elif ptype == '2':
            samsung()
        elif ptype == '3':
            oneplus()

    def iphone():
        print('What type of iPhone do you have?')
        print('1. iPhone 7')
        print('2. iPhone 8')
        print('3. iPhone X')
        itype = input ('Please select 1, 2 or 3    ')
        if itype == '1':
            iphone7()
        elif itype == '2':
            iphone8()
        elif itype == '3':
            iphonex()

    def iphone7():
        print('What type of iPhone 7 do you have?')
        print('1. iPhone7')
        print('2. iPhone 7 Plus')
        i7type = input ('Please select 1 or 2    ')
        if i7type == '1':
            size7()
        elif i7type == '2':
           size7plus()

    def size7():
        print('What is the capacity of your iPhone 7?')
        print('1. 32GB')
        print('2. 128GB')
        capacity7 = input ('Please select 1 or 2    ')

    def size7plus():
        print('What is the capacity of your iPhone 7 Plus?')
        print('1. 32GB')
        print('2. 128GB')
        capacity7plus = input ('Please select 1 or 2    ')
                   
    def iphone8():
        print('What type of iPhone 8 do you have?')
        print('1. iPhone8')
        print('2. iPhone 8 Plus')
        i8type = input ('Please select 1 or 2    ')
        if i8type == '1':
            size8()
        elif i8type == '2':
           size8plus()

    def size8():
        print('What is the capacity of your iPhone 8?')
        print('1. 64GB')
        print('2. 256GB')
        capacity8 = input ('Please select 1 or 2    ')

    def size8plus():
        print('What is the capacity of your iPhone 8 Plus?')
        print('1. 64GB')
        print('2. 256GB')
        capacity8plus = input ('Please select 1 or 2    ')

    def iphonex():
        print('What type of iPhone X do you have?')
        print('1. iPhone X')
        print('2. iPhone XS')
        print('3. iPhone XS Max')
        print('4. iPhone XR')
        ixtype = input ('Please select 1, 2, 3 or 4    ')
        if ixtype == '1':
            sizex()
        elif ixtype == '2':
            sizexs()
        elif ixtype == '3':
           sizexsmax()
        elif ixtype =='4':
            sizexr()

    def sizex():
        print('What is the capacity of your iPhone X?')
        print('1. 64GB')
        print('2. 256GB')
        capacityx = input ('Please select 1 or 2    ')

    def sizexs():
        print('What is the capacity of your iPhone XS?')
        print('1. 64GB')
        print('2. 256GB')
        print('3. 512GB')
        capacityxs = input ('Please select 1, 2 or 3    ')

    def sizexsmax():
        print('What is the capacity of your iPhone XS Max?')
        print('1. 64GB')
        print('2. 256GB')
        print('3. 512GB')
        capacityxsmax = input ('Please select 1, 2 or 3    ')
                           
        
    def sizexr():
        print('What is the capacity of your iPhone XR?')
        print('1. 64GB')
        print('2. 128GB')
        print('3. 256GB')
        capacityxr = input ('Please select 1, 2 or 3    ')


    def samsung():
        print('What type of Samsung do you have?')
        print('1. Samsung Galaxy S')
        print('2. Samsung Glaxy Note')
        stype = input ('Please select 1 or 2    ')
        if stype == '1':
            s()
        elif stype == '2':
            note()

    def s():
        print('What type of Samsung Galaxy S9 do you have?')
        print('1. Samsung Galaxy S9')
        print('2. Samsung Galaxy S8')
        sstype = input ('Please select 1 or 2    ')
        if sstype == '1':
            ssize9()
        elif sstype == '2':
           ssize8()

    def ssize9():
        print('What is the capacity of your Samsung Galaxy S9?')
        print('1. 128GB')
        print('2. 256GB')
        capacitys9 = input ('Please select 1 or 2    ')

    def ssize8():
        print('What is the capacity of your Samsung Galaxy S8?')
        print('1. 64GB')
        print('2. 128GB')
        capacitys8 = input ('Please select 1 or 2    ')
                   
    def note():
        print('What type of Samsung Galaxy Note do you have?')
        print('1. Samsung Galaxy Note 9')
        print('2. Samsung Galaxy Note 8')
        ntype = input ('Please select 1 or 2    ')
        if ntype == '1':
            note9()
        elif ntype == '2':
           note8()

    def note9():
        print('What is the capacity of your Samsung Galaxy Note 9?')
        print('1. 128GB')
        print('2. 512GB')
        capacityn9 = input ('Please select 1 or 2    ')

    def note8():
        print('What is the capacity of your Samsung Galaxy Note 8?')
        print('1. 64GB')
        print('2. 128GB')
        capacityn8 = input ('Please select 1 or 2    ')

            
    def oneplus():
        print('What type of OnePlus phone do yopu have?')
        print('1. OnePlus 5')
        print('2. OnePlus 6')
        otype = input ('Please select 1 or 2    ')
        if otype == '1':
            one5()
        elif otype== '2':
            on6()
        
    def one5():
        print('What type of OnePlus 5 do you have?')
        print('1. OnePlus 5')
        print('2. Oneplus 5T')
        o5type = input ('Please select 1 or 2    ')
        if o5type == '1':
            onep5()
        elif o5type == '2':
            onep5t()

    def onep5():
        print('What is the capacity of your OnePlus 5?')
        print('1. 64GB')
        print('2. 128GB')
        capacity5 = input ('Please select 1 or 2    ')

    def onep5t():
        print('What is the capacity of your OnePlus 5T?')
        print('1. 64GB')
        print('2. 128GB')
        capacity5t = input ('Please select 1 or 2    ')

    def one6():
        print('What type of OnePlus 6 do you have?')
        print('1. OnePlus 6')
        print('2. Oneplus 6T')
        o6type = input ('Please select 1 or 2    ')
        if o6type == '1':
            onep6()
        elif o6type == '2':
            onep6t()

    def onep6():
        print('What is the capacity of your OnePlus 6?')
        print('1. 64GB')
        print('2. 128GB')
        capacityp6 = input ('Please select 1 or 2    ')

    def onep6t():
        print('What is the capacity of your OnePlus 6T?')
        print('1. 64GB')
        print('2. 128GB')
        capacity6t = input ('Please select 1 or 2    ')

#all the code for the tablets
    def tablet():
        print('Please select the type of phone you have.')
        print('1. Apple')
        print('2. Samsung')
        print('3. Lenovo')
        ttype = input ('Please select 1, 2 or 3    ')
        if ttype == '1':
            apple()
        elif ttype == '2':
            samsungt()
        elif ttype == '3':
            lenovo()

    def apple():
        print('What type of iPad do you have?')
        print('1. iPad')
        print('2. iPad Pro')
        print('3. iPad Pro (New)')
        atype = input ('Please select 1, 2 or 3    ')
        if atype == '1':
            ipad()
        elif atype == '2':
            ipadp()
        elif atype == '3':
            ipadpro()

    def ipad():
        print('What is the capacity of your iPad?')
        print('1. 32GB')
        print('2. 128GB')
        capacity1 = input ('Please select 1 or 2    ')

    def ipadp():
        print('What is the capacity of your iPad Pro?')
        print('1. 64GB')
        print('2. 256GB')
        print('3. 512GB')
        capacity11 = input ('Please select 1, 2 or 3    ')

    def ipadpro():
        print('What is the capacity of your iPad Pro (New)?')
        print('1. 64GB')
        print('2. 256GB')
        print('3. 512GB')
        print('4. 1TB')
        capacity2 = input ('Please select 1, 2, 3 or 4    ')

    def samsungt():
        print('What type of table do you have?')
        print('1. Tab A Series')
        print('2. Tab S Series')
        sttype = input ('Please select 1 or 2    ')
        if sttype == '1':
            taba()
        elif sttype == '2':
            tabs()

    def taba():
        print('Which table of the Tab A Series do you have?')
        print('1. Galaxy Tab A 10.1”')
        print('2. Galaxy Tab A 10.5”')
        satype = input ('Please select 1 or 2    ')
        if satype == '1':
            a1()
        elif satype == '2':
            a5()

    def a1():
        print('What type of Tab A 10.1 do you have?')
        print('1. Wifi')
        print('2. 4G')
        a1type = input ('Please select 1 or 2    ')
          
    def a5():
        print('What type of Tab A 10.5 do you have?')
        print('1. Wifi')
        print('2. 4G')
        a5type = input ('Please select 1 or 2    ')

            
    
    def tabs():
        print('Which table of the Tab S Series do you have?')
        print('1. Galaxy Tab S3')
        print('2. Galaxy Tab S4')
        tstype = input ('Please select 1 or 2    ')
        if tstype == '1':
            s3()
        elif tstype == '2':
            s4()

    def s3():
        print('What type of Tab S3 do you have?')
        print('1. Wifi')
        print('2. 4G')
        s3type = input ('Please select 1 or 2    ')

    def s4():
        print('What type of Tab S4 do you have?')
        print('1. Wifi')
        print('2. 4G')
        s4type = input ('Please select 1 or 2    ')

    def lenovo():
        print('What type of tablet do you have?')
        print('1. Tab 4')
        print('2. Yoga Tab')
        ltype = input ('Please select 1 or 2    ')
        if ltype == '1':
            ltab4()
        elif ltype == '2':
            yoga()

    def ltab4():
        print('What type of Tablet do you have?')
        print('1. Tab 4 10"')
        print('2. Tab 4 10" Plus')
        print('3. Tab 4 8"')
        print('4. Tab 4 8" Plus')
        tab4type = input ('Please select 1, 2, 3 or 4    ')

    def yoga():
        print('What type of Tablet do you have?')
        print('1. Yoga Tab 3 10"')
        print('2. Yoga Tab 3 Pro (Wifi)')
        print('3. Yoga Book with Android')
        print('4. Yoga Book C930')
        yogatype = input ('Please select 1, 2, 3 or 4    ')
        if yogatype == '1':
            yogatab3()


    def yogatab3():
        print('What Operating System is your Yoga Tab 3 running?')
        print('1. Windows')
        print('2. Android')
        yogatab3os = input ('Please select 1 or 2    ')


    print ('What type of device are having problems with?')
    print ('1. Phone')
    print ('2. Tablet')
    device = input ('Please select 1 or 2    ')
    if device == '1':
        phone() #runs phone questions + code       
        break #ends loop
    elif device == '2':
        tablet()#runs tablet questions + code 
        break
        


problem_keys = {}#dictionary

keywordsFile = open("keywords.txt").readlines() #opens and uses file keyword for the keywords
solutionsFile = open("solutions.txt").readlines()#opens and uses file solution for the solutions

for line in keywordsFile:
    problem_name = line.split () [0]
    solution_lineNumber = line.split () [1] #separates keywords into numbered groups

    problem_keys[problem_name] = solution_lineNumber #links numbered keyword groups with solitions line number

is_solution_found = False

while True:
    userinput = input("Please describe the problem with your device:") #lets user input problem and creates user variable
    time.sleep(0.5)

    userinput = userinput.lower()

    if userinput == ("quit"): #lets user quit if typed quit
        quit()
        
    user_input_keywords = userinput.split() #finds keywords in inputed sentence

    for input_key in user_input_keywords:
        if input_key in problem_keys:

            lineNumber = int(problem_keys[input_key])
            print (solutionsFile[lineNumber])
            time.sleep(7.5)
            is_solution_found = True
            quit()

    if is_solution_found == False: #This code will be active if no keywords are found
            print("Apologies, I couldn't find a solution to your problem. Please be more specific") 
            time.sleep(0.5)
            user_input = input("Please try again by pressing enter, then inputting another keyword or 'quit' to exit the program.")
            time.sleep(0.5)
            if userinput == ("quit"):#lets user quit if typed quit
                quit()



