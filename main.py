
class jamol:
    def __init__(self,name,surname,latname):
        self.name=name
        self.surname=surname
        self.latname=latname
        self.array=[]
        self.quantity=0

    def __int__(self,name):
        self.array.append(name)
        self.quantity+=1

    def get_intro(self):
        return f'{self.name}{self.surname}{self.latname}'


Name=jamol('jamolldin','sodikov','sadasdsa')
Nas=jamol('asdsda','asdsa','assda')

print(Name.get_intro())

class user:
    def __init__(self,name,nationality,location):
        self.name=name
        self.nationality=nationality
        self.location=location


    def get_info(self):
        return f'{self.name}  {self.nationality}  {self.location}'


filename = 'abs.txt'
with open(filename,'w') as file:
       filename=file.write('dasdas')


class username:
    def __init__(self,name,surname,age,school):
        self.name=name
        self.surname=surname
        self.age=age
        self.school=school

    def get_introduction(self):
        return  f"My name is {self.name} and {self.surname} my age is {self.age}{self.school}"


Jamol=username("jamolldin","sodikov","19","235")
print(Jamol.get_introduction())

name="jamol"
name= input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if name.lower() != 'jamol': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {name.title()} biz jamol kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, jamol")