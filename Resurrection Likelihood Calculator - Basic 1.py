#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is a calulator to run various likelihood scenarios based on Richard Swineburnes book on the Resurrection."The Resurrection of God incarnate"

# K = the evidence of natural theology for God's existence
# E = the detailed historical evidence of
    # e1 - life of Jesus as a prophet/revealter
    # e2 - supermiracle validation (resurrection)
    # e3 - being God incarnate satisfied in no other...than possible Jesus /good life
    #Please note, Swinburne dinstinguishes between e and f. E being the possible evidence of such a thing and f being the actual evidence of such a thing. I just stick with E. 
# H1 = the evidence that God became incarnate in Jesus
# H2 = the Hypothesis that Jesus Christ rose from the dead
# H = the conjunction of H1 and H2

# Our interest will be with the Probality of H given E and K or P(H | E & K) 
# Admittedly (as Swinburne points out), our values will be rough. That is why I am building this calculator so I can run hundreds of simulations. 

#Swinburne sets the likelihood of Theism given background knowledge at .5
#swinburne sets the likelihood of the claim that God became incarnate in a world of sin and suffering at .5


# In[2]:


#step 1 - Swinburne sets the likelihood of Theism given background knowledge at .5
#Please input your Probability of theism


p_tbk = float(input("please enter a number between between .01 and 1.0 that you think represents the likelihood that God exists. You thought ")) 
#p_tbk is theism given background knowledge

print("Your probability of theism given background knowledge is")
print(p_tbk)

if p_tbk > .5:
    print("Why do you think the likelihood of God's existence is rather high?")
elif(p_tbk == .5):
    print("Philosopher of Religion, Richard Swineburne also estimates the same as you did. \n He figures this is a pretty safe bet")
else:    
    print("Why do you think the likelihood of God's existence is rather low? \nWhat tips the scales under 50% for you?")





# In[3]:


#step 2 #swinburne sets the likelihood of the claim that God became incarnate in a world of sin and suffering at .5,
#this is when we are assuming theism. So, given theism. 
p_iss = float(input("What is the likelihood that God became incarnate in \n in a world of sin and suffering?")) 
       #p_iss is the probability of incarnation given a world of sin and suffering
print("The probability of the incarnation when we assume theism is")
print(p_iss)

if p_iss > .5:
    print("Do you think it's rational to estimate that initial probability so high? \nHave you considered contrary evidence to your initial estimate? \nWhy do you hold this to be so certain?")
elif(p_iss == .5):
    print("Swineburne also estimates this number at .5. He seems to think that it's likelihood is just as probable as it's denial")
else:
    print("Thanks for your estimate. By answering lower than .5, are you implying \nThat God not revealing himself in/as a human is more likely than him doing so?")


# In[4]:


#step 3 is to define a probability of the incarnation given theism. .5 * .5
print("This step of the calculator takes your last two estimates and multiplies them together") 

p_ik = p_tbk * p_iss #probability of incarnation given theism 
print("The probability incarnation and theism is")
print(p_ik)

subtracted_value = 1.0 - p_ik #this is to be used two steps down. In Swinburnes original, the leftover is .75, but everyone elses will be different. 
print(subtracted_value)
print("This is the difference when subtracted from 1, or 100%")


# In[6]:


#step 4 is to take the probability of evidence given the incarnation and evidence for God's existence. 
#he places this rather low at 1/10
#the probability of the evidence 1-3, given the claim of the incarnation and the evidence for God's existence

p_eik = .1 #the probability of evidence given incarnation and the background knowledge theism. 
print("The probability of the three pieces of evidence given the claim of the incarnation and knowledge of God is")
print(p_eik)



# In[7]:


#now, according to Swineburne's formula's we need to bring some of these together. 
#we are looking now for the p(e&c|k)= p(e|c&k)* p(c|k)
#take the last two cells and multiply them
print("the probability of both together is")
combined_p_ik_eik = p_ik * p_eik
print(combined_p_ik_eik)

print("swineburnes original numbers bring us to 1/40 or .025")





# In[ ]:


#Question what is the p(~c/k) = 3/4, this is what it left from the 1/4 we assigned earlier. 


# In[8]:


#Question: What is the chance that E will still occurr if there is no incarnation?
# This could be whether there is no God or he doesn't become incnarate. 
#Namely, what is the probability of those three pieces of evidence occuring in the same individual?
#At the outset, this seems immensley improbable. In the book he says that all three occurring in human history
#in various individuals is somewhat likely, especially with those that are non-miraculous. 
#but all three together in the same individual, fairuly unlikely. 
#swineburne assigns 1/1000 as the likelihood for the original example. 

evidence_occuring_no_god = .001

#This is a very key number. If you lower the likelihood of these three occuring in the same perons (e1-e3) 
#Then, all things staying the same, it only increases the likelihood in the final analysis. 
#but, if you raise the likelihood of this evidence occuring when there is no god, 
#then you are basically having to affirm a miracle, assuming you think the evidence for Jesus' res is compelling. 
#again, one can just say that the three e's, never all happened in Jesus. 
#thus, even if the likelihood for them occuring is minute, in the end they did not happen. 
#that of course would not be compelling. It goes back to e and if they occurred. 
#I suppose someone could argue that the likelihood of three such events occurring in the same person is high...
#Maybe they think that given all the possiblities of human life / interaction, the dice are bound to role three 6's.
#if you have enough roles, then you will get there. Thus, it is all random. 
#my thought would be, that something being random in a series of events, does not necessarily exclude meaningful...?
#still, they would have to deny resurrection...so that one should still keep the likelihood rather low of all three
#occurring in the same person. 


# In[9]:


#Question: What is the chance that E will still occurr if there is no incarnation?
# This could be whether there is no God or he doesn't become incnarate. 
#Namely, what is the probability of those three pieces of evidence occuring in the same individual?
#At the outset, this seems immensley improbable.  
#swineburne assigns 1/1000 as the likelihood. 

p_e_k = combined_p_ik_eik + (subtracted_value * evidence_occuring_no_god)  #and the 1/1000 from above
print(p_e_k)

print("swineburne's original numbers bring us to 103/4000 or .02575")


# In[10]:


#let's finish the equation
#p(c|e&k)= p(e|c&K) * p(c|k) / p(e|k)

total_p = p_eik * p_ik / p_e_k
print(total_p)
print("That is the likelihood everyone!")


# In[11]:


#All of the above represents the proability on the strength of the evidence, that we have about Jesus of Nazareth...
#that God has or will become incarnate. 
#swineburne's contention is that to avoid, one will have to give very different values to the numbers above. 
#Examples 1: "The problem of evil shows there is no God, therefore the first two are at 0%"
#example 2: "Even if there is a 50% chance that there is a God, he is clearly to be understand more as deism asserts..."
   #and therefore, the second percentage should be 0%. 
#in each of these scenarios you end up reducing the evidence down to accident/randomness. 


# In[ ]:


#Another point to remember, Swineburne spends an entire book on the three pieces of evidence.
#if one reads Swineburne and remains unconvinced by the evidence being actual evidence, then...
#these three evidences are just hypothetical, namely, that if they would occur it would give us such percentages. 
#a lot is bound up in e. 
#swineburne does work hard to weed out unneccessary assumptions and works with good scholars on the subject. 

