message = input()

happy = message.count(':-)')
sad = message.count(':-(')

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy and sad != 0:
    print('unsure')
else:
    print('none')
