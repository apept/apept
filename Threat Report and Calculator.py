#!/usr/bin/env python
# coding: utf-8

# In[1]:


#step 1 - State the terms of likelihood and impact

qual_report = """This a qualitative risk analysis. The legitimacy of this report will be based on how strong 
the reasons given. This document allows the 'user' or person in charge, to weigh risks and document the risk
process in a way that can be recorded. Improvements in risk profile could show signs of progress being made.   

This qualitative risk analysis will be based on three things. 
1. Likelihood of the risk effecting your organization, government, or context (geography).
2. The reasons given for the likelihood of a given risk estimate. 
2. If the risk would succeed, what would the impact likely be. 
For the person completing this report, you will be giving broad likelihoods.
When asked specific questions about likelihood and impact the first question will be looking for
"low" "moderate" or "high."

When asked for a percentage afterwards, please enter a decimal. Example: .79 = 79%. 

These categories will help the decision maker get a quick grasp on the situation and use the data in actionable ways.
Based on the breakdown, you can think of each category representing an approximate percentage. 
LOW = 1-33%
MODERATE = 34-66%
HIGH = 67-100%"""

print(qual_report)






# In[2]:


#Step 2 - report writer should state their context. 
context = input("Please state the organization, government, or geography that this report is covering.\n")


# In[3]:


#step 3 receive input from the "Live DATA Stream"
#share how likely it is that it will effect your context
#Record the impact expected. 
#this is actionable information that is going on "now" in the organization or around the world.  
#it is important that we see the story of the data. It will help other viewers to agree or 
#disagree with the assessments made. Are the original inputs of data cohesive with the risk level
#placed on it. 
questionlive = input("Please enter the live data you have from your organization or threat data that is immediate \nor near immediate:\n")

likelihoodlive = input("What is the likelihood that the live data you just wrote about will effect your context? Low, Moderate, or High \n")

livepercent = float(input("What percent would you give this. Please enter a decimal from .00 to 1.0\n"))
 
livereason = input("What reason/s do you have for thinking the way you do?\n 'My reasons are that...'\n")

impactlive = input("What will the impact likely be on your organization if this threat data succeeds against your organization \nor progresses against your organization \n")

impactlivereason = input("Please state why you think it will have that impact:\n")

livepercentinverse = 1.0 - livepercent

print(f"Your safety likelihood on this one measure, the live data stream is {livepercentinverse:.5%}")

liverecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety score? ")





# In[4]:


#step 4 - Receive input from past data stream
pastdata = input("What past data do you have that would be relevant to calculating your risk profile? ")

likelihoodpast = input("What likelihood is there that the past data you just wrote of will impact this organization?\nLow, Moderate, or High ")

pastpercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0 "))

pastreason = input("What reason/s do you have for thinking this? ")

impactpast = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High ")

impactpastreason = input("Please state why you think it will have that impact? \n")

pastpercentinverse = 1.0 - pastpercent


print(f"Your safety likelihood on this one measure, the past data stream is {pastpercentinverse:.5%}")

pastrecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety score? ")


# In[5]:


#Step 5 - Receive data from the business/industry specific (or government specific) data stream. 
industrydata = input("What industry data do you have that would be relevant in calculating your risk profile?")

likelihoodindustry = input("What likelihood is there, that the industry data you just wrote of will impact this organization?\nLow, Moderate, or High ")

industrypercent = float(input("What percent would you give this? Please input a decimal between.00 and 1.0 "))

industryreason = input("What reason/s do you have for thinking this? ")

impactindustry = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High ")

impactindustryreason = input("Please state why you think it will have that impact? \n")

industrypercentinverse = 1.0 - industrypercent

print(f"Your safety likelihood on this one measure, the industry data stream is {industrypercentinverse:.5%}")

industryrecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety score? ")


# In[6]:


#Step 6 - Receive data from the Geopolitical stream - This stream has to do with public events, global events, politics and more. 
geodata =  input("What Geopolitical data do you have that would be relevant in calculating your risk profile")

likelihoodgeo = input("What likelihood is there, that the geopolitical data you just wrote of will impact this organization?\nLow, Moderate, or High")

geopercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0:  "))

georeason = input("What reason/s do you have for thinking this? ")

impactgeo = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High:  ")

impactgeoreason = input("Please state why you think it will have that impact\n")

geopercentinverse = 1.0 - geopercent

print(f"Your saftety likelihood on this one measure, the geopolitical data stream is {geopercentinverse:.5%}\n")

georecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety scores? ")


# In[7]:


techdata = input("What technology do you have, and what is the state of that technology, that would be relevant in calculating your risk profile")

likelihoodtech = input("What likelihood is there, that your technology that you just wrote of, will impact this organization\nLow, Moderate, or High: ")

techpercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0:  "))

techreason = input("What reason/s do you have for thinking this? ")

impactech = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High:  ")

impacttechreason = input("Please state why you think it wiill have that impact/n ")

techpercentinverse = 1.0 - techpercent

print(f"Your safety likelihood on this one measure, the technology data stream is {techpercentinverse:.5%}/n")

techrecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety scores? ")


# In[8]:


#Step 8 - Third Party Data Stream - Have there been audits, how safe are they? Have you discussed security?
thirddata = input("What third parties do yo work with and what is the state of their security profile")

likelihoodthird = input("What likelihood is there, that these third parties, have weaknesses that will impact this organization\nLow, Moderate, or High: ")

thirdpercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0:  "))

thirdreason = input("What reason/s do you have for thinking this? ")

impacthird = input("What is the impact this will have on the organization or context? \nLow, Moderate, or High:  ")

impactthirdreason = input("Please state why you think it will have that impact/n ")

thirdpercentinverse = 1.0 - thirdpercent

print(f"Your safety likelihood on this one measure, the third party data stream is {thirdpercentinverse:.5%}/n")

thirdrecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety scores? ")


# In[9]:


#Step 9 - Zero Day Stream - I think we need to plan for the worst...the black swans.
#no doubt, a Zero Day or black swan event, will be worse for a airport than it will for an elementary school. 
#still, we should expect, or even key in unknown events to effect our overall score.
#the More software, the more third party's etc will mean the great likelihood something like this will occurr. 
#the industry we are in, will greatly or modestly effect the impact. Banking fraud is a big impact.
#school computer hacked may not matter so much unless there is leakable information. 

likelihoodzero = input("What likelihood is there, that a zero day vulnerability will will impact this organization\nLow, Moderate, or High: ")

zeropercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0:  "))

zeroreason = input("What reason/s do you have for thinking this? ")

impactzero = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High:  ")

impactzeroreason = input("Please state why you think it wiill have that impact/n ")

zeropercentinverse = 1.0 - zeropercent

print(f"Your safety likelihood on this one measure, the zero day/black swan data stream is {zeropercentinverse:.5%}/n")

zerorecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety scores? ")


# In[11]:


#Step 10 - Other Data Stream - What else might be relevant?
otherdata = input("What other data do you think is import to consider for your security profile")

likelihoodother = input("What likelihood is there, that this other data will impact this organization\nLow, Moderate, or High: ")

otherpercent = float(input("What percent would you give this? Please input a decimal between .00 and 1.0:  "))

otherreason = input("What reason/s do you have for thinking this? ")

impactother = input("What is the impact this will have on the organization or context?\nLow, Moderate, or High:  ")

impactotherreason = input("Please state why you think it wiill have that impact/n ")

otherpercentinverse = 1.0 - otherpercent

print(f"Your safety likelihood on this one measure, the other data stream is {thirdpercentinverse:.5%}/n")

otherrecs = input("What do you think your organization could do/put into place which could lower the\n likelihood of this threat/issue and improve your safety scores? ")


# In[12]:


#Step 11 - Equation to get total safety likelihood or total risk likelihood. 

safetyscore = livepercentinverse * pastpercentinverse * industrypercentinverse * geopercentinverse * techpercentinverse * thirdpercentinverse * zeropercentinverse * otherpercentinverse

print("This is your safety score. The likelihood that you will remain safe", safetyscore, "%")


#Step 12 - Output to text file. Print/write all the individual scores first
#this includes likelihoods and impacts, and their reasons. Again, this will be an overall report. 
#then a calculation of the overall score. 

#This could be just fine


# In[13]:


#convert all float data to strings for output.
lp_string = str(livepercent)
lpinverse_string = str(livepercentinverse)

pp_string = str(pastpercent)
ppinverse_string = str(pastpercentinverse)

ip_string = str(industrypercent)
ipinverse_string = str(industrypercentinverse)

gp_string = str(geopercent)
gpinverse_string = str(geopercentinverse)

tp_string = str(techpercent)
tpinverse_string = str(techpercentinverse)

thp_string = str(thirdpercent)
thpinverse_string = str(thirdpercentinverse)

zp_string = str(zeropercent)
zpinverse_string = str(zeropercentinverse)

op_string = str(otherpercent)
opinverse_string = str(otherpercentinverse)

sc_string = str(safetyscore)


# In[15]:


f = open("trythreat.txt", "w")
print(qual_report, file=f)
print("______________________", file=f)
print("What is your context:", context, file=f)
print("______________________", file=f)
#Output Step 3
print("-THE LIVE DATA STREAM-", file=f)
print("Live Data:", questionlive, file=f)
print("Likelihood it affects the org:", likelihoodlive, file=f)
print("Percent likely:", lp_string, file=f)
print("Reasons for estimate:",livereason, file=f)
print("Possible impact on org:", impactlive, file=f)
print("Reasons for thinking so:", impactlivereason, file=f)
print("Safety likelihood for live data:", lpinverse_string, file=f)
print("Recommendations:", liverecs, file=f)

#output step 4
print("______________________", file=f)
print("-THE PAST DATA STREAM-", file=f)
print("Past Data:", pastdata, file=f)
print("Likelihood it affects the org:",likelihoodpast, file=f)
print("Percent likely:", pp_string, file=f)
print("Reasons for estimate:", pastreason, file=f)
print("Possible impact on org:", impactpast, file=f)
print("Reasons for thinking so:", impactpastreason, file=f)
print("Safety likelihood for past data:", ppinverse_string, file=f)
print("Recommendations:", pastrecs, file=f)


#output step 5
print("______________________", file=f)
print("-THE INDUSTRY DATA STREAM-", file=f)
print("Industry Data:", industrydata, file=f)
print("Likelihood it affects the org:",likelihoodindustry, file=f)
print("Percent likely:", ip_string, file=f)
print("Reasons for estimate:", industryreason, file=f)
print("Possible impact on org:", impactindustry, file=f)
print("Reasons for thinking so:", impactindustryreason, file=f)
print("Safety likelihood for past data:", ipinverse_string, file=f)
print("Recommendations:", industryrecs, file=f)


#output step 6
print("______________________", file=f)
print("-THE GEOPOLITICAL STREAM-", file=f)
print("Geopolitical Data:", geodata, file=f)
print("Likelihood it affects the org:",likelihoodgeo, file=f)
print("Percent likely:", gp_string, file=f)
print("Reasons for estimate:", georeason, file=f)
print("Possible impact on org:", impactgeo, file=f)
print("Reasons for thinking so:", impactgeoreason, file=f)
print("Safety likelihood for past data:", ppinverse_string, file=f)
print("Recommendations:", georecs, file=f)


#Output step 7
print("______________________", file=f)
print("-THE TECHNOLOGY STREAM-", file=f)
print("Technology Data:", techdata, file=f)
print("Likelihood it affects the org:",likelihoodtech, file=f)
print("Percent likely:", tp_string, file=f)
print("Reasons for estimate:", techreason, file=f)
print("Possible impact on org:", impactech, file=f)
print("Reasons for thinking so:", impacttechreason, file=f)
print("Safety likelihood for past data:", tpinverse_string, file=f)
print("Recommendations:", techrecs, file=f)


#Output step 8
print("______________________", file=f)
print("-THE THIRD PARTY STREAM-", file=f)
print("Third Party Data:", thirddata, file=f)
print("Likelihood it affects the org:",likelihoodthird, file=f)
print("Percent likely:", thp_string, file=f)
print("Reasons for estimate:", thirdreason, file=f)
print("Possible impact on org:", impacthird, file=f)
print("Reasons for thinking so:", impactthirdreason, file=f)
print("Safety likelihood for past data:", thpinverse_string, file=f)
print("Recommendations:", thirdrecs, file=f)

#Output step 9
print("______________________", file=f)
print("-THE ZERO DAY STREAM-", file=f)
print("Likelihood it affects the org:",likelihoodzero, file=f)
print("Percent likely:", zp_string, file=f)
print("Reasons for estimate:", zeroreason, file=f)
print("Possible impact on org:", impactzero, file=f)
print("Reasons for thinking so:", impactzeroreason, file=f)
print("Safety likelihood for past data:", zpinverse_string, file=f)
print("Recommendations:", zerorecs, file=f)

#Output step 10
print("______________________", file=f)
print("-OTHER DATA STREAM-", file=f)
print("Other Data:", otherdata, file=f)
print("Likelihood it affects the org:",likelihoodother, file=f)
print("Percent likely:", op_string, file=f)
print("Reasons for estimate:", otherreason, file=f)
print("Possible impact on org:", impactother, file=f)
print("Reasons for thinking so:", impactotherreason, file=f)
print("Safety likelihood for past data:", opinverse_string, file=f)
print("Recommendations:", otherrecs, file=f)


#Output Step 11
print("______________________", file=f)
print("-Overall Total Safety Likelihood-", file=f)
print("Your overall safety score is", sc_string, "%", file=f)


f.close()


# In[ ]:


#reflections on this calculator
#1 - The value of this calculator is to reinforce the strong likelihood, at least to most industry's, 
  #that there safety likelihood is low. The way that cross multiiplying percentages typically works is to lower the combined safety numbers. 
  #thus, the total safety score will most of the time be much lower than the individual safety scores. 
#2 - The value of this calculator is that the perspectival data is present for the manager/Cyber lead to evaluate. 
  #it can help to develop a strategic plan for lowering the likelihoods of breaches or vulnerabilities. 
#3 - Its a final report that can be compared against periodically to see if your organization is getting better. 
#4 - With each new avenue/stream of data that you include in your assessment, your likelihood of safety will 
#keep going down. This makes sense. But, it should be a strong wake up call to any practioners
#as well as C suite executives that the more complex your organization, generally speaking, the more likely there is 
#a vulnerability. 
#A drawback of this report is that unless the reasons really back up the %'s, there could be constant questioning. 
#data driven organizations will have to dig deep to provide solid reasons for their estimates. 
#still, the other reflections still stand. 


# In[ ]:




