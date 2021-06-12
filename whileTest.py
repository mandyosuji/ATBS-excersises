name = 'Mandy'
yourName = input('What is your name?\n')
while len(yourName):
    if yourName == name:
        print('Hello, Mandy!')
    else:
        print('I do not know you.')
    yourName = input('What is your name?\n')
