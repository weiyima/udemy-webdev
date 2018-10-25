from django.shortcuts import render

# Create your views here.
def index(requests):
    my_dict = {'insert_content':"Hello I'm from level two first app"}
    return render(requests, 'first_app/index.html',context=my_dict)

def randomfunction():
    pass