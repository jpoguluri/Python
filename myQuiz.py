# My first program in Python


print ("Welcome to Bible Quiz")
print (" ")

# Get # of questions from user
q = int (input ("Choose total number of questions for quiz(1-10): "))

# Ensure # of questions selected are in acceptible range
while q < 1 or q > 10:
      print ("OOPS! You selected", q, "questions.")
      print ("Please select your questions from 1 to 10 ONLY")
      print ("")
      q = int (input ("Choose total number of questions for quiz(1-10): "))


# Initialize parameters
i = 0
p = 0
t = q

''' i -> correct answers.
    q -> chosen # of questions.
    t -> # of questions remaining, at given instant of time.
    p -> Percentage of correct answers
    '''

# Question-1
print ("")
# Question should be asked only if questions remaining (t) are graeter than 0 
if t > 0:
   print ("Q1: How many books are in Bible?")
   print ("1: 39 2: 27")
   print ("3: 56 4: 66")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   # Reduce remaining questions by 1 
   t = t - 1
   if resp == "4":
      # If answer is correct, increment i by 1
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-2
   print ("")
if t > 0:
   print ("Q2: How many number of Chapters are in the book of Acts?")
   print ("1: 25 2: 26")
   print ("3: 27 4: 28")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1 
   if resp == "4":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-3
   print ("")
if t > 0:
   print ("Q3: How many number of Chapters are in the Gospel of Mark?")
   print ("1: 16 2: 17")
   print ("3: 18 4: 19")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "1":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-4
   print ("")
if t > 0:
   print ("Q4: How many number of Chapters are in book of revelation?")
   print ("1: 22 2: 23")
   print ("3: 24 4: 25")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "1":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-5
   print ("")
if t > 0:
   print ("Q5: How many number of books are in new testament?")
   print ("1: 27 2: 39")
   print ("3: 66 4: 28")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "1":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-6
   print ("")
if t > 0:
   print ("Q6: How many number of books are in old testament?")
   print ("1: 27 2: 39")
   print ("3: 66 4: 28")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "2":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-7
   print ("")
if t > 0:
   print ("Q7: About howmany years old was Jesus when he started his public ministry?")
   print ("1: 20 2: 30")
   print ("3: 40 4: 50")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "2":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-8
   print ("")
if t > 0:
   print ("Q8: About how long did Jesus preach and teach before his crucifixtion?")
   print ("1: 2.5yrs 2: 3.5yrs")
   print ("3: 4.5yrs 4: 5.5yrs")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "2":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer") 
# Question-9
   print ("")
if t > 0:
   print ("Q9: During Jesus temptation, how many days & nights did he fast?")
   print ("1: 20 2: 30")
   print ("3: 40 4: 50")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "3":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")
# Question-10
   print ("")
if t > 0:
   print ("Q10: Identify the longest pslam in bible?")
   print ("1: Ps 1 2: Ps 119")
   print ("3: Ps 100 4: Ps 23")
   print ("")
   resp = input ("Choose right option: ")
   print ("")
   t = t -1
   if resp == "2":
      i = i + 1
      print ("Your response", resp, "is CORRECT answer")
   else:
       print ("Your response", resp, "is INCORRECT answer")

   
# Quiz Results to be displayed only after all quiz questions selected are asked t = 0                
if t <= 0:
   print ("Your Bible Quiz Results")
   print ("=======================")
   print ("")
   # print ("value of t", t)
   p = int(i*100/q)
   print ("You correctly answered: ", i, "out of", q, "questions")
   print ("")
   print ("Your percentage of correct answers: ", p, "%")
   print ("")
   if p == 100:
      print ("Your grade is: A+ --> Awesome! Great Job!!")
   elif p >= 75:
      print ("Your Grade is: A. --> Good Job!")
   elif p < 75 and p > 50:
        print ("Your Grade is: B. --> Not too bad!")
   elif p < 50 and p > 30:
        print ("Your Grade is: C. --> Way to go!")     
   else:
    print ("Your Grade is: D.  --> High time to open bible")

    

