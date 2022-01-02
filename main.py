techcompanies=['apple','saudi :aramco','amazon','tesla','space x','Gazprom','Microsoft','Alibaba']
print('big five company:',techcompanies[0:4])
print('After five big compaies:',techcompanies[4:10])

carcompanies=['ford','ferarry','lamba','Mustang','BMW']

new_big_world=techcompanies+carcompanies
print(new_big_world)
array=['pynative',4]
jamol=['jamol','sarvar','ismoil','mirjalol']
if 'jamol' in jamol:
    print('yes')
else:
    print('no')
print(jamol[-1])
jamol.append('ismoil')
print(jamol)
jamol.insert(1,'Saidhox')
print(jamol)
jamol.clear()
print(jamol)
jamol.sort()
print(jamol)
Listitem=[1,2,321,2,21,3,-2,]
Listitem.sort()
print(Listitem)
clothes=['Louse','Adidas','Guchi','Channel','H&M']
print(clothes[0:3])
#tuple//
Mytuple=('Jamol','Sadikov','Sayfuddinvich')
print(type(Mytuple))
for Tuple in Mytuple:
    print(Tuple)

hash=("Murod","abuduaxad","Abdusamad")
print(type(hash))
if "Murod" in hash:
    print('yes')
else:
    print('no')



tupless=('wood','metal','plastic')
print(len(tupless))
tac=(1,2,3,4,5,6,7,8,9)
print(tac[2:5])

#Dictionary//
jamol={
    'name':'Jamolliddin',
    'surname':'Sodikov',
    'age':2
}
print(jamol)

jamol2=dict(name='jamol',age=2,surname='sodikov')
print(jamol2)




jamol={1,2,34,43,21}
jamol2={2121,212,331,212,1,2}
diferent=jamol.difference(jamol2)
print(diferent)


library=dict(name='diyora',surname='kHodjaeva',age=19,university='wiut',income='100k')
library['income']='35'
library['surname']='sodikova'
del library['university']
first_company={'bigblutton','zoom','facebook''apple','amazon'}
second_company={'bigblutton','zoom','nike','puma','appke'}
find_difference=first_company.difference(second_company)
print(find_difference)








love=dict(name='Diyora',surname='Khodjaeva',age=19,study='wiut')
print(love)
love['surname']='sodikova'
print(love)
del love['surname']
print(love)
if 'study'in love:
    print(love['study'])

love2=dict(name='madina',surname='tillayeva',university='art')
print(love2)
try:
    print(love2['nsame'])
except:
    print('Error')
jamol=dict(name='Diyora',surname='Khodjaeva',university='wiut')
jamol['name']='Diyorahon'
del jamol['university']
print(jamol)
jamol['surname']='Sadikova'
print(jamol)
if 'Sadikov' in jamol:
    print('good')
else:
    print('not bad')
function_set=set()
function_set.add(1)
function_set.add(2)
function_set.add('21')
function_set.remove('21')
print(function_set)
if 4 in function_set:
    print('hi Jamol')
else:
    print('hi diyora')
#Set//
setA={1,2,3,4,5,6}
setB={1,4,5,8,12}
diff=setA.difference(setB)
print(diff)
Jamolldin={'bitcoin','cardano','matic','xrp','chainlink','yearsfinance'}
Mirjalol={'bitcoin','solana','mobox','Axis','avalance','matic','ada'}
diffrences=Jamolldin.difference(Mirjalol)
print(diffrences)
difff=Mirjalol.difference(Jamolldin)#/to know diffrence variable is located
print(difff)
dis=Jamolldin.symmetric_difference(Mirjalol)
Jamolldin.update(Mirjalol)#to sum up two vairable into one
print(Jamolldin)





print(Jamolldin.issubset(Mirjalol))
fragen={1,2,3,4,5,6} #it worked because gefragt has of element in fragen
gefragt={1,2,3,4,5,6,11,33,44}
print(gefragt.issuperset(fragen))
#String
jamol='I\'m programmer'# it working because of backslash
print(jamol)

tom=' hi '
sarif='jamol'
sentences= tom + '' + sarif
print(sentences)

gap=' hi jamol  '
print(gap)
gap=gap.strip()
print(gap)
rax=' i rammping amazing'
print(rax.find('z'))
word='hi,jgar,nima,gap'
words=word.split(".")
print(words)

#try cat exception
try:
    ja=int(input('enter your number'))
    print(ja)
except:
    print('invalid number')

try:
    wodsa=int (input('put any digit: '))
    print(wodsa)
except:
    print('Invalid number')





try:
    value=10/2
    jal=int(input('put number: '))
    print(jal)
except ZeroDivisionError:
    print('zerodivide by zero')
except ValueError:
    print('invalid input')

#loop








print('jamol want to sell his product which multiples sell that you say')
sell='just say how many sell you produced'
sell+='(if you are tired of saing of product and fed up of this type to me like this "hi")'
value=''
while value!='hi':
    value=input(sell)
    if value!='hi':
        print(int(value)**8)






Jamoll=list(range(1,40))
for i in Jamoll:
    if i==12:
        break
    print(f'{i**8}')

ismoil=list(range(1,100))
for i in ismoil:
    if i==21:
        break                  #it will stop our algoritim cuz i said break when it will rach 21
    print(f'{i*10}')



Numbers=list(range(1,25))
for i in Numbers:
    if i==12:
        continue             #it will continue our algoritim,but it will leave number which was indicated
    print(f'{i**10}')

print('its help you to recognize anout library')
question='it will give loevely book that you want to have'
question+='(just say when you "finish" searaching your book)'
product=''
while product!='finish':
    product=input(question)
    if product!='finish':
        print(int(value)**1)

ticket=list(range(1,100))
for i in ticket:
    if i==10:
        continue
    elif i==23:
        break
    print(f'{i**10}')








print("we will help you get through")
question='it will help you collect book'
question+='(when it finish your ssearching book just say "finish")'
value=''
while value!='finish':
   value=input(question)
   if value!='finish':
       print(int(value)**1)








ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break


array=[]

print('we will corresponding of role your positions in our company')
f=1
while True:
    question=f'{f}'
    name=input(question)
    names.append(name)
    answer=input("will you add friends")
    if answer=='yes':
        f+=1
        continue
    else:
        break




son=1
while son<=5:
    print(son,end='')
    son=son+1

number=10
while number<=20:
    print(number,end='')
    number=number+number

#json

import json
jamol={

    'name':'Jamollidin',
    'age':20,
    'university':'wiut',
    'lanuguages':['english','deutch','russian','uzbek']

}
jamolJson=json.dumps(jamol,indent=10)
print(jamol)

#random
import random
a=random.randint(1,10)
print(a)
mylist=list('sakdknas')
a=random.choice(mylist)
print(a)

#decorator

def f1(func):
    def wrapper():
        print('srated')
        func()
        print('end')

    return wrapper

def f():
    print('hello')
f1 (f)()





class username:
     def calculation_of_price(self,x,y):
         return x * y

username1=username()
username1.name='jamolldin'
username1.surname='sodikov'
username1.age=10
username1.income=1000
print(username1.calculation_of_price(username1.income,username1.age))

username2=username()
username2.name='Sarvar'
username2.surname='Holland'
username2.sallary=100
username2.income=1000
print(username2.calculation_of_price(username2.sallary,username2.income))
