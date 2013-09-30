from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'number_guessing/index.html')

def play(request, choice = None):
    
    if 'number' not in request.session:
        request.session['number'] = 2
    else:
        selected_choice = request.POST['choice']
    
    
    if int(selected_choice) == 2:
        return HttpResponse('Hurray! You\'ve won!')
    else: 
        return render(request, 'number_guessing/play.html', {'numbers': range(5)})