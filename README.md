# List-lab
In this project I created a cool list.

Here is my code: '''
Name: Adam Reisfeld

Title: Pythonator: Guess Your Olympic Sport

Short Description: Think of an Olympic sport and we will do our best to guess it.

'''

#ask for name
name = input('What is your name?: ')
print('Hello ' + name + ', nice to meet you!')

#intor info
print('Think of an Olympic sport, and I will try to guess it!')
print('For all questions, answer in either True or False please.')

#varaibles/questions
team_sport = input('It is a team sport? ')
while team_sport not in ['True', 'False']: team_sport = input('Please enter only True or False: ')

uses_ball = input('It uses a ball? ')
while uses_ball not in ['True', 'False']: uses_ball = input('Please enter only True ot False: ')

summer_sport = input('It is in the Summer Olympics? ')
while summer_sport not in ['True', 'False']: summer_sport = input('Please enter only True ot False: ')

water_sport = input('It is played in water? ')
while water_sport not in ['True', 'False']: water_sport = input('Please enter only True or False: ')

requires_judges = input('It requires judges to score? ')
while requires_judges not in ['True', 'False']: requires_judges = input('Please enter only True ot False: ')

#if/else/elif statements
if team_sport == 'True':
        if uses_ball == 'True':
            if water_sport == 'True':
                print('You are thinking of... WATER POLO!')
            elif summer_sport == 'True':
                print('You are thinking of... BASKETBALL!')
            else:
                print('You are thinking of... SOCCER!')
        else:
            if summer_sport == 'True':
                print('You are thinking of... VOLLEYBALL!')
            else:
                print('You are thinking of... ICE HOCKEY!')
else:
        if water_sport == 'True':
            print('You are thinking of... SWIMMING')
        elif requires_judges == 'True':
            if summer_sport == 'True':
                print('You are thinking of... GYMNASTICS!')
            else:
                print('You are thinking of... SKIING!')
        elif uses_ball == 'True':
            print('You are thinking of... TENNIS!')
        else:
            print('STOP TRYING TO SEE WHAT WILL HAPPEN IF YOU ONLY ENTER FALSE! PLAY THE GAME FOR REAL!') #easter egg

#check if we guessed correctly
check = input('Did we guess correctly?: ').lower()
if check == 'yes':
    print('Woohoo!')
else:
    print('I give up :(')
    correct_sport = input('What sport did you think of?: ')
    print('Ahhhh ' + correct_sport + ', that was my next guess!')
   

#ending
print('Thank you for playing our game! We hope you enjoyed your experience!')

