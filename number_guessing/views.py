from django.shortcuts import render, redirect
from random import randint
from number_guessing.forms import GuessForm

ATTEMPT_COUNTER = 'ATTEMPT_COUNTER'
NUMBER_TO_GUESS = 'NUMBER_TO_GUESS'
PAST_GUESSES = 'PAST_GUESSES'  
NUM_CHOICES = 10


def index(request):
    return render(request, 'number_guessing/index.html')

def start_game(request):
    request.session[ATTEMPT_COUNTER] = None
    request.session[NUMBER_TO_GUESS] = randint(0, NUM_CHOICES - 1)
    request.session[ATTEMPT_COUNTER] = 1
    request.session[PAST_GUESSES] = []
    return redirect('/guess/play')

def play(request):
    form = GuessForm(request.POST, num_choices = NUM_CHOICES) if request.POST else GuessForm(num_choices = NUM_CHOICES)
    message = ''
    
    if form.is_valid():
        number_to_guess = int(request.session[NUMBER_TO_GUESS])
        guess = form.cleaned_data['choice']
        
        if guess == number_to_guess:
            return redirect('/guess/success')
        
        message = _generate_hint(guess, number_to_guess)
        request.session[ATTEMPT_COUNTER] = int(request.session[ATTEMPT_COUNTER]) + 1
        request.session[PAST_GUESSES].append((guess, guess > number_to_guess))
        
    return render(request, 'number_guessing/play.html', 
                  {'form' : form, 
                   'message' : message,
                   'past_guesses' : request.session[PAST_GUESSES]})

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