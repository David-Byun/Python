from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_all_rooms(request):
    return HttpResponse("see all rooms")


def see_one_room(request, room_id):
    return HttpResponse(f"see room with {room_id}")
