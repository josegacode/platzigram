from django.http import HttpResponse, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("Server time is {}".format(now))


def sorted_numbers(request):
    numbers_str = request.GET["numbers"]
    sorted_numbers = sorted(numbers_str.split(","), key=int)
    data = {"status": "Ok", "response": sorted_numbers}
    return JsonResponse(data)


def welcome(request, age, name):
    if age > 17:
        return HttpResponse("Hola {}!".format(name))
    else:
        return HttpResponse("Sorry {}, you aren't allowed here".format(name))