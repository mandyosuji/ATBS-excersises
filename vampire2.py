name = 'Carol'
age = int(input('How old are you?\n'))
if name == 'Alice':
    print('Hi, ALice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
