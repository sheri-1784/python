from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()

'''
key = ['A','B','C']
val = [10, 20, 30]
number = {}

for num in range(len(key)):
    number[key[num]] = val[num]
print(number)

print({x:y for x,y in zip(key,val)})

num1 = dict(zip(key,val))
print(num1)


num2 = {}
for x in range(len(key)):
    num2.update({key[x]:val[x]})
print(num2)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1,**dict2}
print(dict3)

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

sample = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sample['class']['student']['marks']['history'])

emp = ['Kelly', 'Emma']
dfl = {"designation": 'Developer', "salary": 8000}

band = {}
for x in range(len(emp)):
    band[emp[x]] = dfl
print(band)

sam = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
key = ["name", "salary"]

num = {}
for x in range(len(key)):
    num[key[x]] = sam[key[x]]
print(num)

numb = {}
for x in key:
    numb[x] = sam[x]
print(numb)

print({x:sam[x] for x in key})

dumb = {}
for x in key:
    dumb.update({x:sam[x]})
print(dumb)
'''
samp = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }
'''
keys = ["name", "salary"]   

for x in keys:
    del samp[x]
print(samp)

print(samp.keys())
print(samp.items())
print(samp.values())

keys = ["name", "salary"]

for x in keys:
    samp.pop(x)
print(samp)

samp = {'a': 100, 'b': 200, 'c': 300}
for val in samp.values():
    if val == 200:
        print(val,'is present in the dict.')
        
if 200 in samp.values():
    print('200 is present in the dict.')


#samp['location'] = samp.pop('city')
samp.update({'location':samp.pop('city')})
print(samp)

sampl = {
  'Physics': 82,
  'Math': 65,
  'history': 75
  }

print(min(sampl))
'''
sample = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
    }

sample['emp3']['salary'] = 8500

print(sample)