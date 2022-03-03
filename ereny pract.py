#!/usr/bin/env python
# coding: utf-8

# In[5]:


#lab 1
# Read 1st Number
Num1 = input("plz enter 1st number:")
# Read 2st Number 
Num2 = input("plz enter 2st number:")
# Convert  Numbers from str to float
Num1 = float(Num1)
Num2 = float(Num2)
# print  sum
print ('sum =' , Num1+Num2)
# print  sub
print ('sub =' , Num1-Num2)
# print  Mul
print ('Mul =' , Num1*Num2)


# In[4]:


# Read Age
age = input('Plz Enter your Age :')
gender = input("plz Enter Gender :")
# convert Age
age = float(age)
# compare Age
if age >= 18 and (gender == 'M' or gender=='Male'):
         print('Male ok')
elif age <18 and  (gender == 'M' or gender=='Male'):
         print('Male No')
elif age >=20 and  (gender == 'F' or gender=='Female'):
          print('Female ok')
elif age <20 and  (gender == 'F' or gender=='Female'):
          print('Female No')
else:
          print(" undefined Gender")
    


# In[2]:


#lab 2
#Read 1st Number
num1 = input('plz Enter 1st number : ')
#Read 2st Number
num2 = input('plz Enter 2st number : ')
#Read operation
op =input('plz Enter the operation')
# convort operands to Numbers
num1 = float(num1)
num2 = float(num2)
if op =='+':
    res = num1+num2
    print ("sum =",res)
elif op =='-':
    res=num1-num2
    print ("sub =",res)
elif op =='*' or op=='x' or op== 'X':
    res = num1*num2
    print ( "Mul = ",res)
elif op =='/' or op=='\\':
    res = num1/num2
    print ("Div = ",res)


# In[3]:


numlist =[1,2,3,4]
floatlist=[2.1,3.4]
list1=[1,2,3,4,3.2,5.6,'ALI','MOHAMED']
print(numlist)
print(floatlist)
print(list1)


# In[7]:


numlist[0]


# 

# In[8]:


numlist[-1]


# In[9]:


numlist[0:1]


# In[10]:


numlist[0:2]


# 

# In[12]:


numlist[:2]


# In[11]:


numlist[2:]


# In[13]:


list1=[1,2,3,4,3.2,5.6,'ALI','MOHAMED']
list1[4]='Hazem'
list1


# In[14]:


del(list1[6])
list1


# In[15]:


del(list1)
list1


# In[16]:


names=['mohamed','ali','hazem']
jobes=['DOC','ENG','SING']
names+jobes


# In[17]:


names=['mohamed','ali','hazem']
jobes=['DOC','ENG','SING']
names*3


# In[19]:


len(names)


# In[21]:


3 in names


# In[22]:


'hazem'in names


# In[35]:


if 'hazem' in names:
     print('hello')
else :
      print('Bye')


# In[37]:


names=['mohamed','ali','hazem']
numbers=[1,2,3,4,5,6,7]
print(len(names))
print(min(names))
print(min(numbers))
print(max(names))
print(max(numbers))


# In[38]:


names.append('abduallah')


# In[39]:


names


# In[45]:


numbers.append(6000)
print(numbers)


# In[46]:


numbers.count(6000)


# In[47]:


names.count('abduallah')


# In[48]:


names=['mohamed','ali','hazem']
numbers=[1,2,3,4,5,6,7]
numbers.extend(names)


# In[50]:


print(numbers)


# In[51]:


z=names+numbers


# In[52]:


print(z)


# In[53]:


names.index('hazem')


# In[59]:


names


# In[60]:


names[2]
names.pop()


# In[61]:


names


# In[64]:


names


# In[65]:


names.remove('sherif')


# In[66]:


names


# In[67]:


names=['mohamed','ali','hazem']


# In[68]:


names.reverse()


# In[69]:


names


# In[70]:


names.sort()


# In[71]:


names


# In[76]:


names=['hazem','ali','mohamed','ibrahim']
namesT=('hazem','ali','mohamed')
print(type(names))
print(type(namesT))


# In[78]:


namesT=('hazem','ali','mohamed')
print(namesT[0:2])


# In[79]:


namesT=('hazem','ali','mohamed')
namesT[0]='ali'


# In[87]:


namesT=('hazem','ali','mohamed',2,1,2,60.2)
ages=(20,30,40)
namesT*2


# In[88]:


len(namesT)


# In[90]:


min(ages)


# In[91]:


max(ages)


# In[92]:


ages=(20,30,40)
type(ages)


# In[94]:


ages=list(ages)
type(ages)


# In[95]:


ages.append(80)


# In[96]:


ages


# In[97]:


ages= tuple(ages)
type(ages)


# In[99]:


#Dictionary
search ={'names':'ali','ages':29}
search['ages']


# In[100]:


search['names']='mohamed'


# In[101]:


search


# In[102]:


del(search['ages'])
search


# In[104]:


search ={'names':'ali','ages':29}
search.clear()
search


# In[105]:


del(search)
search


# In[106]:


search ={'names':'ali','ages':29}
len(search)


# In[107]:


str(search)


# In[110]:


dic1={'names':'ali','ages':29,'salary' :9000}
dic2=dic1.copy()
dic2


# In[111]:


list1={'names','age','salary','add'}
dic3=dict.fromkeys(list1)
dic3


# In[118]:


dic1['names']


# In[119]:


dic1.get('names')


# In[121]:


dic1.items()


# In[126]:


dic1.values()
dic1.keys()


# In[127]:


msg='welcom to python'
type(msg)


# In[129]:


msg[-1]


# In[130]:


msg*3


# In[131]:


msg[3:6]


# In[139]:


#special char
msg='welcom %s to python'%'Ali'
print(msg)


# In[142]:


name='mohamed'
number=3
msg='welcom %s to python %d'%(name,number)
print(msg)


# In[143]:


msg.replace('3','4')


# In[144]:


msg.replace('python','java')


# In[145]:


len(msg)


# In[147]:


msg.index('python')


# In[148]:


msg='ali'
msg.capitalize()


# In[149]:


msg ='welcome to python course'
print(msg[1])


# In[152]:


print(msg[0])
print(msg[1])
print(msg[2])
index =len(msg)-1
print(msg[index])


# In[156]:


numbers=range(2,10,2)
print(numbers)
numbers=list(numbers)
print(numbers)


# In[162]:


for s in range(len(msg)):
    print (msg[s])


# In[163]:


for s in msg:
    print (s)


# In[164]:


list1=['mohamed','ali','ibrahim']
for name in list1:
    print(name)


# In[170]:


dic={'name':'hazem','age': 29,'gender':'male'}
for key,value in dic.items():
       print(key,",",value) 


# In[175]:


num=input('plz Enter the Number')
while num!='0':
    print ('continue')
    num=input('plz enter number:')
    print ('bye bye')


# In[177]:


print("*")


# In[179]:


for i in range (0,5):
    print('*',end='')


# In[184]:


#*****
#*****
for line in range(2):
    for i in range (0,5):
        print('*',end='')
    print('\n')


# In[198]:


word ='python'
for c in word:
    if c=='h':
         break
    print(c)


# In[200]:


word ='python'
for c in word:
    if c=='h':
        pass
    else:
        print(c)


# **********
# **********
# **********
# welcom to python course
# **********
# **********

# In[217]:


def printstart() :
    for line in range(3):
        for i in range(0,10):
            print('*',end='')
    print('\n')
    


# In[242]:


for line in range(3):
    for i in range(0,10):
         print('*',end='')
    print('\n')
    

print('welcom to python course')   
    
for line in range(2):
    for i in range(0,10):
         print('*',end='')
    print('\n')
    


# In[243]:


def printstart() :
    for line in range(2):
        for i in range(0,10):
            print('*',end='')
    print('\n')


# In[246]:


printstart() 
print('welcom to python course')
printstart()   


# In[249]:


def printstart(row,col) :
    for line in range(row):
        for i in range(0,col):
            print('*',end='')
    print('\n')


# In[254]:


printstart(3,10) 
print('welcom to python course')
printstart(2,10)   


# In[274]:


#convert from reqire arrgument to deful arr
def printstart(col=1,row =1) :
    
    for line in range(row):
        for i in range(0,col):
            print('*',end='')
        print('\n')
  


# In[276]:


printstart() 
print('welcom to python course')
printstart(col=10,row=2)


# In[35]:


#function definition is here
def changeme(x):
  "This changes a passed list into this function"
   
x=[1,2,3,4];
print('values insid the function:',x)
return

#now you can call change me function 
mylist =[10,20,30];
changeme(mylist);
  print ('value outside the function:',mylist)


# In[22]:


total= 0
def summ(num1,num2):
   
    total=num1+num2
    print('inside the function sum local total',total)
    return (total)

def sub(num1,num2):
   
    total=num1-num2
    print('inside the function sub global total:',total)
    return (total)

   


# In[23]:


sumres=summ(10,20)
subres=sub(10,20) 
print('outside the function sub global total:',total)
print('outside the function summres:',sumres)
print('outside the function subres:',subres)
    


# In[63]:


#lab (3:1)
def max_two_numbers(num1,num2):
    if num1>num2:
        return (num1)
    else :
        return (num2)
def max_three_numbers(num1,num2,num3):
    m =max_two_numbers(num1,num2)
    fin=max_two_numbers(m,num3)
    return(fin)
num1 =input ("plz enter 1st number:")
num2 =input ("plz enter 2st number:")
num3 =input ("plz enter 3st number:")
res = max_three_numbers(num1,num2,num3)
print('max=',res)


# In[66]:


#lab (3:2)
def uniqelist(nonunique):
    res = []
    for n in nonunique:
        if n not in res:
            res.append(n)
    return(res)

numbers =[1,2,3,3,3,4,4,6,7,8,9,5,2,6,0] 
Hamada = uniqelist(numbers)
print(Hamada)


# In[110]:


class Dog :
    color = []
    eyecolor = []
    H = None
    L = None
    w = None


# In[111]:


Reks = Dog()
Lasse = Dog()


# In[112]:


Reks.color=['Black','Gray','White']
Lasse.color=['Gold','Gray','White']


# In[113]:


print('Reks.color:',Reks.color)
print('Lasse.color:',Lasse.color)


# In[ ]:

















