from django.shortcuts import render, redirect
from random import randint

ATTEMPT_COUNTER = 'ATTEMPT_COUNTER'
NUMBER_TO_GUESS = 'NUMBER_TO_GUESS' 


def index(request):
    return render(request, 'number_guessing/index.html')

def start_game(request):
    request.session[ATTEMPT_COUNTER] = 0
    number = randint(0 ,4)
    request.session[NUMBER_TO_GUESS] = randint(0 ,4)
    return redirect('/guess/play')
    

def play(request, choice = None):
    if request.session[ATTEMPT_COUNTER] == 0:
        request.session[ATTEMPT_COUNTER] = int(request.session[ATTEMPT_COUNTER]) + 1
        return render(request, 'number_guessing/play.html', {'numbers': range(5)})
    else:
        selected_choice = request.POST['choice']
    
    guess = int(selected_choice)
    number_to_guess = int(request.session[NUMBER_TO_GUESS])
    message = ''
    
    if guess == number_to_guess:
        return redirect('/guess/success')
    elif guess < number_to_guess:
        message = '%d is lower than the secret number!' % guess
    else:
        message = '%d is higher than the secret number!' % guess
    
    request.session[ATTEMPT_COUNTER] = int(request.session[ATTEMPT_COUNTER]) + 1
        
    return render(request, 'number_guessing/play.html', {'numbers': range(5), 'message' : message})
    
def success(request):
    attempts = int(request.session[ATTEMPT_COUNTER])
    message = ''
    if attempts == 1:
        message = 'You\'ve needed only one attempt!'
    else:
        message = 'You\'ve needed %d attempts!' % attempts
    return render(request, 'number_guessing/success.html', {'message' : message})