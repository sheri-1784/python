from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

import wizcoin

purse = wizcoin.WizCoin(2,5,99)
#print(purse)
print('G:',purse.g,'S:',purse.s,'K:',purse.k)
print('Total Value:',purse.value())
print('Total Weight:',int(purse.weight()))

print('----------------------')

coinjar = wizcoin.WizCoin(13,0,0)
print('G:',coinjar.g,'S:',coinjar.s,'K:',coinjar.k)
print('Total Value:',coinjar.value())
print('Total Weight:',int(coinjar.weight()))

print('----------------------')

wall = wizcoin.WizCoin(1,1,100)
print('G:',wall.g,'S:',wall.s,'K:',wall.k)
print('Total Value:',wall.value())
print('Total Weight:',int(wall.weight()))
print(wall.s)
wall.s = wall.s + 5
print(wall.s)

