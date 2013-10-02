from django.shortcuts import render, redirect
from random import randint

ATTEMPT_COUNTER = 'ATTEMPT_COUNTER'
NUMBER_TO_GUESS = 'NUMBER_TO_GUESS' 
MAX_NUM = 4


def index(request):
    return render(request, 'number_guessing/index.html')

def start_game(request):
    request.session[ATTEMPT_COUNTER] = None
    return redirect('/guess/play')

def play(request):
    if not request.session[ATTEMPT_COUNTER]:
        request.session[ATTEMPT_COUNTER] = 1
        request.session[NUMBER_TO_GUESS] = randint(0, MAX_NUM)
        return render(request, 'number_guessing/play.html', {'numbers': xrange(MAX_NUM + 1)})
    else:
        guess = int(request.POST['choice'])

    number_to_guess = int(request.session[NUMBER_TO_GUESS])
    
    if guess == number_to_guess:
        return redirect('/guess/success')
    
    request.session[ATTEMPT_COUNTER] = int(request.session[ATTEMPT_COUNTER]) + 1
        
    return render(request, 'number_guessing/play.html', 
                  {'numbers': xrange(MAX_NUM + 1), 
                   'message' : _generate_hint(guess, number_to_guess)})

def _generate_hint(guess, secret):
    if guess < secret:
        return '%d is lower than the secret number!' % guess
    else:
        return '%d is higher than the secret number!' % guess
    
def success(request):
    attempts = int(request.session[ATTEMPT_COUNTER])
    message = ''
    if attempts == 1:
        message = 'You\'ve needed only one attempt!'
    else:
        message = 'You\'ve needed %d attempts!' % attempts
    return render(request, 'number_guessing/success.html', {'message' : message})