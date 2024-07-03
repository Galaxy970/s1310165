import random
count = 1
accept = 0
Headsnumber = 0
Tailsnumber = 0

print('Who are you?')

name = input()

print('Hello,'+name+'!')


print('Tossing a coin...')

for number in range(3):
    print('Round '+str(count)+' :', end = ' ')
    accept = random.randint(1,100)

    if accept%2 == 0:
        print('Heads')
        Headsnumber += 1

    else:
        print('Tails')
        Tailsnumber += 1

    count += 1

print('Heads:'+str(Headsnumber)+',Tails:'+str(Tailsnumber))

if Headsnumber>Tailsnumber:
    print('You won')

else:
    print('You lost')
    



