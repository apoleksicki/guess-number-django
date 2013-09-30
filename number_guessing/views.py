from django.http.response import HttpResponse

def index(reques):
    return HttpResponse('foo bar baz')