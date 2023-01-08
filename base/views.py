from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Let\'s learn Python.'},
    {'id': 2, 'name': 'Design with me.'},
    {'id': 3, 'name': 'Frontend Developer.'}
]

"""
We created this "/test" url just to show 
"""


def test(request):
    return render(request, 'test.html')


def home(request):
    # return HttpResponse("Home page")
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    # return HttpResponse("Room page")
    """
        Syntax of filter function : 
        ----------------------------------
        filter(function, sequence)
        ----------------------------------
        In functions we used lambda function and in sequence we used rooms.

        Syntax of lambda function : 
        ----------------------------------
        lambda arguments: expression
        ----------------------------------
        Note that lambda function can have any number of arguments but only one expression, which is evaluated and return the output.
        So here "x" is argument(i.e. this lambda function has 1 argument only) and "x['id'] == int(pk)" is the expression.
    """
    current_room = list(filter(lambda x: x['id'] == int(pk), rooms))
    context = {'room': current_room[0] if len(current_room) > 0 else None}
    return render(request, 'room.html', context)
