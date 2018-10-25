from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("2nd App!")

def help(request):
    my_dict = {'help_insert':"Template tag for help page"}
    return render(request, 'second_app/help.html', context=my_dict)
