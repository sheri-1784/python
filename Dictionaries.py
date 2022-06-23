from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()


alien = {}
alien['name'] = 'kaka'
alien['age'] = 44
alien['loc'] = 'lahore'

print('Alien age is:', alien['age'])
print('Alien name is:', alien['name'].title())
print('Alien is living in',alien['loc'].title())

print()
print(alien)
print()
alien['x'] = 12
alien['y'] = 24
alien['loc'] = 'karachi'
print(alien)

alien = {}
alien['x'] = int(input('Enter X: '))
alien['y'] = int(input('Enter Y: ' ))
alien['sp'] = input('Define speed ')

if alien['sp'] == 'slow':
    x_inc = 1
    y_inc = 3
elif alien['sp'] == 'med':
    x_inc = 2
    y_inc = 4
else:
    x_inc = 3
    y_inc = 6
    
alien['x'] = alien['x'] + x_inc
alien['y'] = alien['y'] + y_inc

print()    
print('Alien New x Position:',alien['x'])
print('Alien New y Position:',alien['y'])

print(alien)
del alien['sp']
print()
print(alien)

fav_lang = {
    'sarah':'python',
    'majid':'java',
    'sonia':'php',
    }

print('Sara Favorite Language:',fav_lang['sarah'].title())

print(fav_lang.get('majed','The value does not exist'))

user = {
    '1st name':'ashar',
    'last name':'umer',
    'user name':'samar',
    }

for key, value in user.items():
    print(key,end=': ')
    print(value.title())
print()    
fav_lang = {
    'sarah':'python',
    'majid':'java',
    'sonia':'php',
    'tarah':'C++'
    }

for name, lang in fav_lang.items():
    print(name.title(),"favourite language is:",lang.title())
print()

for name in fav_lang:
    print(name.title())
print()

for name in fav_lang.values():
    print(name.title())

   
lang = {
    'sarah':'python',
    'majid':'java',
    'sonia':'php',
    'tarah':'C++',
    'ashar':'python',
    'samar':'C++',
    'umer':'java',
    }

friends = ['sarah', 'sonia', 'kaka']
for name in lang:
    print('Hi,',name.title())

    if name in friends:
        print('\t',name.title(),', do you like to code in',lang[name].title())
    else:
        print('\t\nHi', name.title(),"Please take part in poll")

for name in reversed(lang.keys()):
    print(name.title(),end=' ')
for val in set(lang.keys()):
    print('Popular languages are:',val.title())

alien1 = {'a':1,'b':2,'c':3}
alien2 = {'a':4,'b':5,'c':6}
alien3 = {'a':7,'b':8,'c':9}

aliens = [alien1, alien2, alien3]

for alien in aliens:
    print(alien)

aliens = []
for alien in range(30):
    alienx = {'a':1,'b':2}
    aliens.append(alienx)

for alien in aliens[:5]:
    print(alien)
    
print('Total aliens are:',len(aliens))

for alien in aliens[:5]:
    if alien['a'] == 1:
        alien['a'] = 11
    if alien['b'] == 2:
        alien['b'] = 22
print()
for alien in aliens[:5]:
    print(alien)

pizza = {
    'crust':'thick',
    'topp': ['pepperoni','grill chiken'],
    }
print('You have ordered a',pizza['crust'],'crust pizza with')
for val in pizza['topp']:
    print('\t',val.title())

key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]
kv = {}

for num in range(len(key)):
    kv[key[num]] = value[num]
print(kv)

person = {"name": "Jessa", "country": "USA", "tele": 1178}

print(person.keys())
print(person.items())
#updating a disctionary
person['weight'] = 75
person.update({'height': 165,'age':38})
person.update([('company','Google'),('city','Texas')])
person['country'] = 'Canada'

print()
for key in person:
    print(key.title(),'=', person[key])
    
print()
for key, value in person.items():
    print(key.title(),'=', value)    

print()
for key in person.items():
    print(key[0].title(),'=',key[1]) #need to understand.   
    
print('\nDict Length is',len(person))

print(person.popitem())

del person['tele']

print()
for key in person.items():
    print(key[0].title(),'=',key[1])

print()    
person.clear()
print(person)

person['weight'] = 75
person.update({'height': 165,'age':38})
person.update([('company','Google'),('city','Texas')])
person['country'] = 'Canada'
print(person)

dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}

dict1.update(dict2)
print(dict1)

dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}

dict3 = {**dict1,**dict2}

for key, val in dict3.items():
    print(key,':',val)
    
print()
for key in dict3.items():
    print(key[0],':',key[1])
    
print()
for key in dict3:
    print(key,':',dict3[key])

print()
dict4 = dict3.copy()
print(dict4)

print()
dict5 = dict(dict4)
print(dict4)

print()
dict6 = dict(dict5.items())
print(dict6)

bio = {'name': 'Jessy', 'company': 'Google'}
add = {"state": "Texas", 'city': 'Houston'}
edu = {'college': 'UT Austin', 'level': 'Master'}
person = {'bio data':bio,'address':add,'education':edu}

for key in person:
    if key == 'bio':
        print('Personal Details:')
        for nkey in bio:
            print(nkey.title(),':',bio[nkey])
    elif key == 'add':
        print('\nAddress Details:')
        for xkey in add.items():
            print(xkey[0].title(),':',xkey[1])
    else:
        print('\nQualifications:')
        for x,y in edu.items():
            print(x.title(),':',y)


for key, val in person.items():
    print(key.title(),'Details:')
    for x,y in val.items():
        print(' ',x.title(),':',y)
    print()           
       
print()
jessi = {'name': 'Jessi', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

class6 = {'student1':jessi,'student2':emma,'student3':kelly}

print('Student3 Name:',class6['student3']['name'],'\n')

print('Class Details\n')
for key, val in class6.items():
    print(key.title())
    for x,y in val.items():
        print(x.title(),':',y)
    print()

dict1 = {'c': 45, 'b': 95, 'a': 35}

print(sorted(dict1.keys()))
print(sorted(dict1.values()))
print(sorted(dict1.items()))
'''
number = [2,4.5,7.6,4,3,4,6]
even = {x: x**2 for x in number if x % 2 == 0}
print(even)
print()

subj = ['math','chem','comp','urdu']
mark = [45,34,55,66]

record = {key:val for key,val in zip(subj,mark)}
print(record)

key = [3,5,7,8,76,5,4,33,3,25,6,7,8,9,75]
number = {x:x*2 for x in key if x%5==0}
print(number)
