import time
print ("Welcome to the Interactive Phone Troupleshooting System version 2.8")
time.sleep(0.5)#waits 0.5 seconds before moving on to the next text

problem_keys = {}#dictionary

keywordsFile = open("keywords.txt").readlines() #opens and uses file keyword for the keywords
solutionsFile = open("solutions.txt").readlines()#opens and uses file solution for the solutions

for line in keywordsFile:
    problem_name = line.split () [0]
    solution_lineNumber = line.split () [1] #separates keywords into numbered groups

    problem_keys[problem_name] = solution_lineNumber #links numbered keyword groups with solitions line number

is_solution_found = False

while True:
    userinput = input("Please describe the problem with your phone:") #lets user input problem and creates user variable
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
