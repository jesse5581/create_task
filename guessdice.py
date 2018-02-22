import random
def guessdice():
    guesses = 1
    sum = 0 
    wrong = True
    print ('You must choose the sum of two dice rolled randomly, ie(2-12)')
    for choices in range(2): 
        d = random.choice([1,2,3,4,5,6])
        sum += d
    print ('guess what the dice rolled')
    while wrong == True:
        guess = int(raw_input('Guess: '))
        if guess == sum:
            print('You won!')
            wrong = False
        else:
            print ('Try Again!')
            guesses += 1
    return guesses       
    
     