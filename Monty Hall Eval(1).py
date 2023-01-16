#!/usr/bin/env python
# coding: utf-8

# In[1]:


#someinstalls
get_ipython().system('pip install openai')
#quering open AI
import requests
import pandas as pd


# In[2]:



#importing ipython to display graphics easily
import IPython.display
from IPython.display import Image

#importing time to pause program at intervals. 
import time
from time import sleep

get_ipython().run_line_magic('env', 'OPENAI_API_KEY=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')
import openai
openai.api_key = "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"


# In[3]:


#monty hall welcome
print("The great Monty Hall welcomes you to....")
time.sleep(1)

#monty image game show
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("C:\\Users\\Isaac Fleming\\Documents\\CODE\\Welcomebanner.jpg")
imgplot = plt.imshow(img)
plt.show()
sleep(3)
print("""Frank, Drew, Ethan, and Justin...I have a wonderful game with a wonderful prize if you pick correctly. 
I have three doors for you to choose from. Behind one of these doors is a car. If you pick the correct door, 
you win the car!""")


# In[4]:


##import youtube video for the contestant to watch
from IPython.display import YouTubeVideo
threedoor = YouTubeVideo("T5QYTrDReTo", start = 0, end = 7)
display(threedoor)
sleep(15)

while True:
    user = input("Who is playing, frank, drew, ethan, or justin ")
    if user.lower() == 'frank': break
    elif user.lower() == 'drew': break
    elif user.lower() == 'ethan': break
    elif user.lower() == 'justin': break
    else:
        print("sorry")
print('Wonderful', user.upper(), 'lets begin')

#bring forth user
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("C:\\Users\\Isaac Fleming\\Documents\\CODE\\erank.jpg")
imgplot = plt.imshow(img)
plt.show()
sleep(5)

import random
RandDoorCar = random.randint(1,3)

while True:
    ContestantChoice = input("Which door are you going to chooose, 1, 2, or 3?")
    if ContestantChoice == "1":
        break
    elif ContestantChoice =="2":
        break
    elif ContestantChoice =="3":
        break
    elif not ContestantChoice.isdigit():
        print("Enter 1, 2, or 3")
    else:
        ContestantChoiceInt = int(ContestantChoice)
        print(ContestantChoiceInt)
type(ContestantChoice) 
ContestantChoiceInt = int(ContestantChoice)
type(ContestantChoiceInt)
print("You Chose Door ", ContestantChoiceInt)


# In[5]:


#monty hall opening sharing his plans to open one of the doors. 
print("Alright....,", user.upper())
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("C:\\Users\\Isaac Fleming\\Documents\\CODE\\Welcomebanner.jpg")
imgplot = plt.imshow(img)
plt.show()
sleep(5)
print("I, the great Monty Hall, am going to open for you one of the two remaining doors to let you know whats inside one of them. ")
sleep(7)

# All options with if/elif/else and option to switch choice asked. 
if RandDoorCar == 1 and ContestantChoiceInt == 1:
    print("Behind Door 2 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 1 and ContestantChoiceInt == 2:
    print("Behind Door 3 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 1 and ContestantChoiceInt == 3:
    print("Behind Door 2 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 2 and ContestantChoiceInt == 1:
    print("Behind Door 3 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 2 and ContestantChoiceInt == 2:
    print("Behind Door 3 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 2 and ContestantChoiceInt == 3:
    print("Behind Door 1 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 3 and ContestantChoiceInt == 1:
    print("Behind Door 2 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 3 and ContestantChoiceInt == 2:
    print("Behind Door 1 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
elif RandDoorCar == 3 and ContestantChoiceInt == 3:
    print("Behind Door 2 is a goat; With this knowledge would you like to switch your door to the one remaining or keep your original choice, which was door", ContestantChoiceInt)
else:
    print("your guess is as good as mine")

sleep(8)


#now, do you want to keep your answer or switch your answer?
while True:
    FinalAnswer = input("Please lock in your final answer")
    if FinalAnswer == "1":
        break
    elif FinalAnswer =="2":
        break
    elif FinalAnswer =="3":
        break
    elif not FinalAnswer.isdigit():
        print("You have to choose the doors number")
    else:
        FinalAnswerInt = int(FinalAnswer)
        print(FinalAnswerInt)

FinalAnswerInt = int(FinalAnswer)

print("your final answer is")
sleep(2)
print("Door ", FinalAnswerInt)
sleep(2)


# In[6]:


#Door reveal
print("Now, for the big moment. Let's see if your final answer which was",FinalAnswerInt, ", is the same door as the one with the new car!")
sleep(6)
if RandDoorCar == FinalAnswerInt:
    print("It's the same door, you have won the car!")
else:
    sleep(3)
    print("da")
    sleep(.5)
    print("da")
    sleep(.5)
    print("da")
    sleep(1)
    print("Sorry...you guessed wrong, the car was in", RandDoorCar)
sleep(1)
#Could autoplay from youtube Monty Hall congratulating or saying wrong
    #could get silly here..before revealing things...I could ask, "Who is the greatest technology leader of all time, Gates, Jobs, Musk, or OpenAI"


# In[7]:


print("That part of the game was fun, but its not over. I have a couple of math questions for you now")
sleep(1)
ProbQuestion1 = float(input("""My first question: After I, Monty Hall, opened one of the doors and showed a goat, what was the
likelihood that staying with your original answer was going to be correct?
.33
.66
.50  """))

print("You said ", ProbQuestion1 * 100,"%")
sleep(1)


# In[8]:


#querying the user regarding
ProbQuestion2 = float(input("""Now, for question 2. After I opened one of the doors and showed a goat, what was the likelihood switching doors would be correct?
.33
.66
.50"""))

print("You Said ", ProbQuestion2 * 100, "%")


# In[9]:


#if elif else, sorting through programs response to user's answer above
if ProbQuestion1 == .33:
    print("In question 1, You are correct, the likelihood of getting the correct door with staying, is 33% ")
elif ProbQuestion1 == .50:
    print("In question 1, You are wrong")
elif ProbQuestion1 == .66:
    print("In question 1, You are wrong")


if ProbQuestion2 == .66:
    print("In question 2, You are correct, the likelihood of getting the correct door with switching, is 66% ")
elif ProbQuestion2 == .33:
    print("In question 2, You are wrong")
elif ProbQuestion1 == .50:
    print("In question 2, You are wrong")


# In[10]:


sleep(3)
print("Let's illustrate this with three methods. Method 1, a video.")
spacey = YouTubeVideo("iBdjqtR2iK4", start = 69)
display(spacey)
sleep(1)


# In[11]:


#query openai api to ask the same question we are working through

print("Method 2 - Let's 'phone a friend' named chatgpt")
prompt = "In the Monty Hall Problem, why is it a better option to switch doors than to stay?"
response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=200)
print(response)


# In[12]:


#illustrating the problem
sleep(2)
import random
print("Method 3: Illustrating through iterating randomly")


Choice01 = random.randint(1, 3)
Door01 = random.randint(1, 3)
if Door01 == 1 and Choice01 == 1:
    print('switching would be bad')
if Door01 == 1 and Choice01 == 2:
    print('switching would be good')
if Door01 == 1 and Choice01 == 3:
    print('Switching would be good')
if Door01 == 2 and Choice01 == 1:
    print('Switching would be good')
if Door01 == 2 and Choice01 == 2:
    print('Switching would be bad')
if Door01 == 2 and Choice01 == 3:
    print('Switching would be good')
if Door01 == 3 and Choice01 == 1:
    print('Switching would be good')
if Door01 == 3 and Choice01 == 2:
    print('Switching would be good')
if Door01 == 3 and Choice01 == 3:
    print('Switching would be good')
print(""" To Illustrate: 
if the car is behind Door 1 and your initial choice was also 1, then switching would be bad
if the car is behind Door 1 and your initial choice was door 2, then switching would be good
if the car is behind Door 1 and your initial choice was door 3, then switching would be good
if the car is behind Door 2 and your initial choice was door 1, then switching would be good
if the car is behind Door 2 and your initial choice was door 2, then switching would be bad
if the car is behind Door 2 and your initial choice was door 3, then switching would be good
if the car is behind Door 3 and your initial choice was door 1, then switching would be good
if the car is behind Door 3 and your initial choice was door 2, then switching would be good
if the car is behind Door 3 and your initial choice was door 3, then switching would be bad
""")
    

print("Switching is the better option 6 of the 9 times and staying is the better option 3 of the 9 times")
percentswitch = 6 / 9
print('When you switch, it is the right decision', percentswitch, '% of the time')
percentstay = 3 / 9
print('When you stay, it is the right decision', percentstay, '% of the time')


# In[13]:


#b will stand for original choice of the contestant
#c will stand for door the car is in. 

Stay = []
Switch = []

for i in range(0,1000):
    b = random.randint(1,3)
    c = random.randint(1,3)
    if b == c:
        Stay.append(b)
    if b != c:
        Switch.append(c)
print("The total number of stays",len(Stay), ": The total number of Switches", len(Switch))
PercentStayCorrect = len(Stay) / 1000
PercentSwitchCorrect = len(Switch) / 1000

print("Staying is good", PercentStayCorrect * 100, "% of the time")
print("Switching is good", PercentSwitchCorrect * 100, "% of the time")

if len(Switch) > len(Stay):
    print("In 1000 trials, you can see that switching gives you a higher probability")
else:
    print("This random range of a 1000 tests was surely strange")


# In[14]:


print("Now, lets try this another time with an even larger number, let's use 1 Million")
sleep(1)
StayLarge = []
SwitchLarge = []

for i in range(0,1000000):
    b = random.randint(1,3)
    c = random.randint(1,3)
    if b == c:
        StayLarge.append(b)
    if b != c:
        SwitchLarge.append(c)
print("The total number of stays",len(StayLarge), ": The total number of Switches", len(SwitchLarge))
PercentStayCorrectLarge = len(StayLarge) / 1000000
PercentSwitchCorrectLarge = len(SwitchLarge) / 1000000

print("Staying is good", PercentStayCorrectLarge * 100, "% of the time")
print("Switching is good", PercentSwitchCorrectLarge * 100, "% of the time")

if len(SwitchLarge) > len(StayLarge):
    print("In one million random trials, you can see that switching gives you a higher probability")
else:
    print("This random range of a Million randomly generated tests was surely strange")


# In[15]:


print("Now, lets try this another time with an even larger number, let's use 1 billion")

StayMax = []
SwitchMax = []

for i in range(0,1000000000):
    b = random.randint(1,3)
    c = random.randint(1,3)
    if b == c:
        StayMax.append(b)
    if b != c:
        SwitchMax.append(c)
print("The total number of stays",len(StayMax), ": The total number of Switches", len(SwitchMax))
PercentStayCorrectMax = len(StayMax) / 1000000000
PercentSwitchCorrectMax = len(SwitchMax) / 1000000000

print("Staying is good", PercentStayCorrectMax * 100, "% of the time")
print("Switching is good", PercentSwitchCorrectMax * 100, "% of the time")

if len(SwitchMax) > len(StayMax):
    print("In 1 Billion random trials, you can see that switching gives you a higher probability")
else:
    print("This random range of a 1 Billion randomly generated tests was surely strange")


# In[16]:





# In[ ]:




