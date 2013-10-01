from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect,\
    HttpResponseRedirectBase

ATTEMPT_COUNTER = 'ATTEMPT_COUNTER'
NUMBER_TO_GUESS = 'NUMBER_TO_GUESS' 


def index(request):
    print 'bar'
    return render(request, 'number_guessing/index.html')

def start_game(request):
    request.session[ATTEMPT_COUNTER] = 0
    request.session[NUMBER_TO_GUESS] = 2
    print 'foo'
    return redirect('/guess/play')
    

def play(request, choice = None):
    request.session[ATTEMPT_COUNTER] = int(request.session[ATTEMPT_COUNTER]) + 1
    
    if request.session[ATTEMPT_COUNTER] == 1:
        return render(request, 'number_guessing/play.html', {'numbers': range(5)})
    else:
        print request.session['NUMBER_TO_GUESS']
        selected_choice = request.POST['choice']
    
    
    if int(selected_choice) == 2:
        return render(request, 'number_guessing/success.html')
    else: 
        return render(request, 'number_guessing/play.html', {'numbers': range(5)})
    
def success(request):
    return render(request, 'number_guessing/success.html')