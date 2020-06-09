# -*- coding: utf-8 -*-

Created on Mon Feb  3 02:14:54 2020

@author: HASSAN ENTERPRISES



# DEBUGGING IS THE PROCESS IN WHICH ERROR ARE DETECTED IN THE CODING AND THEN REMOVED TO EXECUTE THE PROGRAM






#finding a number in any thing line or paragraph;;;;
import re
s="my phonenumber is +91872345"
phonenumRegx=re.compile(r"\+\d\d\d\d\d\d\d\d")
mo=phonenumRegx.search(s)
print("mobile number is",mo.group())
# by busing group() our answer is in this form
#mobile number is +91872345
#=======================================================================
import re
s="my phonenumber is +91872345 and my office number is +81453214"
phonenumRegx=re.compile(r"\+\d\d\d\d\d\d\d\d")
mo=phonenumRegx.findall(s)
print("mobile number is",mo)
#================================== Answer is in list form by using findall=========
#mobile number is ['+91872345']
#===========================================================================
import re
s="my phonenumber is +91872345 and my office number is +81453214"
phonenumRegx=re.compile(r"\+\d\d\d\d\d\d\d\d")
mo=phonenumRegx.findall(s)
for i in mo:
    print("mobile number is",i)
 #=====answer==================================================================   
#mobile number is +91872345
#mobile number is +81453214
import re 
 #function finditer,search,findall,split
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"garbage")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)
    #basically finditer ya bathatha hai joo word apkoo find kerna haiii wooo kitnay word ka bad hai 
   #or kitnay word say phalay hai just like this
    #<re.Match object; span=(23, 30), match='garbage'>
    
    print(mtstys[23:30])
#======================================================================
#meta character using dot . bht saray matches ko nikhalay ga
import re 
 #function finditer,search,findall,split
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r".")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)    
    #print(mtstys[23:30])
# META CHARACTER USING ^ starts with 
import re 
# indentation between ^ i soo no answer is given on the console
 #function finditer,search,findall,split
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"^ i")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)    
# META CHARACTER USING ^ starts with     
import re     
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"^i")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)
#============================================================================================
#META CHARACTER USING $ ENDS WITH 
import re   
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"me $")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)
#========================================================================================================
#META CHARACTER USING * ZERO OR MORE OCCURENCE 
 #kitnayb bhi a hoo ya kitnay bhi i hoooo
import re   
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"ai*")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)    
#======================================================================================================
import re   
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"a*i*")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)       
#========================================================================================================
#META CHARACTER USING + ONE HOO YA USSAY ZADIYA HOOOOOO    
import re   
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r"a*i+")
matches=pat.finditer(mtstys)
for match in matches:
    print(match)     
#==============================================================================================================
# META CHARACTER USING {} USNIG TO BECAUSE EXACTLY SPECIFIED NUMBER OF OCCERENCE
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'you{3}')
matches=pat.finditer(mtstys)
for match in matches:
    print(match) 
#========================================================================================================
#META CHARACTER USING ( )GROUPED
import re
s="my phonenumber is +91872345"
phonenumRegx=re.compile(r"\+\d\d\d\d\d\d\d\d")
mo=phonenumRegx.search(s)
print("mobile number is",mo.group())    
#========================================================================================================
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'(you)')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)

#========================================================================================================
#METE CHARACTER USING | EITHER OR OR
# YA TO MUJHY YA CHAIYA YA YA CHAIYA 
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'have|you')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)
#=========================================================================================================
#specified a special character
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'\A')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)    
#===========================================================================================================
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'\Ai')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)      
#===================================================================================================
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'\bi')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)     
#========================================================================================================
import re 
mtstys="i have find you in the garbage box until you are my faviroute girls you donethe same thing with me "
pat= re.compile(r'have\b')
matches=pat.finditer(mtstys)
for match in matches:
    print(match)    
#================================================================================================
# {} specified the exactly the number of occurence     
import re
mystsy="phone number of my home is  2345-4356"   
pattern=re.compile(r"\d{4}-\d{4}")
matches=pattern.search(mystsy)
print(matches)
#====================================================================================================
import re 
myphone =" my phone number is +92366213796 but my father phone number is +92315828725 and my mother phonenumber is +92316745321" 
patterns=re.compile(r"\+\d{11}")          
match=patterns.findall(myphone)
print("All phonenumber is",match)

Re.txt file as described in the video!
Meta Characters
#[] A set of characters
#\ Signals a special sequence (can also be used to escape special characters)
#. Any character (except newline character)
#^ Starts with
#$ Ends with
#* Zero or more occurrences
#+ One or more occurrences
#{} Exactly the specified number of occurrences
#| Either or
#() Capture and group
#Special Sequences
#\A Returns a match if the specified characters are at the beginning of the string
#\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
#\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

#\d Returns a match where the string contains digits (numbers from 0-9)
#\D Returns a match where the string DOES NOT contain digits
#\s Returns a match where the string contains a white space character
#\S Returns a match where the string DOES NOT contain a white space character
#\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
#\W Returns a match where the string DOES NOT contain any word characters
#\Z Returns a match if the specified characters are at the end of the string    

#=====================  LAB TASKS ===========================================
import re
strs="a quick brown for jump over the lazy dog"
print(re.match("a",strs))
#============================================================================
import re
strs="a quick brown for jump over the lazy dog"
if re.match("a",strs):
    print("it found")
else:
    print("it not found")    
    
#=============================================================================
import re
pattern="[a-zA-Z]"
str="a quick brown for jump over the lazy dog"
print(re.search(pattern,str))
if (re.search(pattern,str)):
    print("found")
else:
    print("not found")


#==============================================================================
import re
a=input("enter:")
pattern="[\w\w.-_]+@[\w\w.-]"
if re.search(pattern,a):
    print("okay")



    
#==============================================================================
# match,search,findall    
y=input("enter the value")
print(re.findall("in",y))
#==============================================================================
import random
x=[1,2,4,3,5,6]
y=random.choice(x)
print(y)
#====================================================
import random
print(random.choice([1,2,3,4,5,6,]))

y=[1,2,4,3,5,6]
#====================================================
print(random.randrange(1,23))
print(random.random())
print(random.shuffle(y))
print(random.seed())
print(random.uniform(5,10))
#===================================================
import re
txt="some butterfly look very beautiful in the light of the sun "
print(re.sub("some","hey",txt))
print(re.sub("\s","*",txt,2))

#====================================================








    