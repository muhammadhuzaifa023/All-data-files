# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#q:1

def stats(filename):
    infile=open(filename,'r')
    x=infile.read()
    lst=x.split()
    print('Line count:',len(x.split('\n')))
    print('word count:',len(lst))
    print('character count:',len(x))
stats('shaiz.txt')    
infile.close()

f=open('test.txt','a')
f.write(input('enter the text'))
f.close()

#q:2

def distribution(filename):
    f=open(filename,'r')
    strs=f.read()
    lst=strs.split()
    num=[6,2,3,2,2,4,1,2]
    for i in range(len(num)):
        print(num[i],'students got',lst[i])
distribution('grades.txt') 

#q:3

def duplicate(filename):
    x=open(filename,'r')
    a=x.read()
    lst=a.split()
    if(len(lst) != len(set(lst))):
        return True
    else:
        return False
duplicate('duplicates.txt')    

#q:4
def abc(filename):
    x=open(filename,'r')
    w=open('abc.txt','w')
    a=x.read()
    lst=a.split()
    new=[]
    for i in range(len(lst)):
        if len(lst[i])==4:
            lst=lst.replace(lst,'xxxx')
        new.append(lst)
    for j in new:
        w.write(j)
duplicate('duplicates.txt')    
