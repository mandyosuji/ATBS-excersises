print('Hello, what is your name?')
name = 'Mandy'
yourName = input()
if yourName == name:
    print('Hi Mandy! Good to see you again :)')
else:
    print(yourName + '?' + ' I don\'t think we\'ve met. Do you wish to continue?')
nextStep = input()
if nextStep == 'yes' or nextStep == 'Yes':
    print('Great! Welcome, ' + yourName + '.')
else:
    print('Bummer. See you next time!')
