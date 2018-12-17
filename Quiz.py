def Quiz():
    questions = [('What is the name of the game character known as a plumber?\n1-Sonic\n2-Mario\n3-Donkey Kong', '2'),
('What is the name of the company responsible for the Final Fantasy franchise?\n1-Capcom\n2-Square Enix\n3-Konami', '2'),
('According to the Castlevania franchise timeline, what year is the events of Symphony Of The Night?\n1-1792\n2-1797\n3-1799', '2'),
('According to the website VG Chartz, which is the best selling videogame in history?\n1-Super Nintendo\n2-Playstation 1\n3-Playstation 2', '3')]

    correct = 0
    wrong = 0

    for quest, rightAns in questions:
        print(quest)
        print()
        answer = input('Answer: ')
        print()
        if answer == rightAns:
            print(f'Correct! The right answer is {rightAns}')
            correct += 1
        else:
            print('Error!')
            wrong += 1
        
    if correct > wrong:
        print('You Win!')

    elif correct == wrong:
        print('TIE!')

    else:
        print('You Lose')
    

def main():
    again = 'Y'
    while again == 'Y':
        print()
        print('Quiz\n1-Start\n2-Exit')
        opt = input('Answer: ')
        if opt == '1':
            Quiz()
        elif opt == '2':
            print('Turn Off!')
            exit()
        print()
        print('Try Again? Y or N')
        again = input('Option: ').upper()
        if again == 'N':
            print('Shutdown!')
            exit()
    else:
        print('Invalid Answer.')
            
main()