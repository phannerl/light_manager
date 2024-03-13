from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Home, Room, Light

def light_handle(light_brightness_list_org, expected_brightness_org) -> list[list[int]]:
    # input:  [200, 300, 600, 700], 700
    # output:  [[200, 200, 300], [700]]
    final_result = []
    stack = [(light_brightness_list_org, expected_brightness_org, [])]
    while stack:
        light_brightness_list, expected_brightness, previous_result = stack.pop()
        for i, light_brightness in enumerate(light_brightness_list):
            if light_brightness > expected_brightness:
                continue
            elif light_brightness == expected_brightness:
                if previous_result:
                    final_result += [previous_result +
                                    [light_brightness]]
                else:
                    final_result += [[light_brightness]]
                continue
            else:
                stack.append((light_brightness_list[i:], expected_brightness -
                            light_brightness, previous_result + [light_brightness]))
    return final_result

class LightCalculation(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        light_brightness_list = data['LightBrightness']
        expected_brightness = data['ExpectedBrightness']
        list_of_light_brightness = sorted(light_brightness_list)
        return HttpResponse(light_handle(list_of_light_brightness, expected_brightness))

class RoomDetailView(View):
    def get(self, request, id):
        lights = list(Light.objects.filter(room=id))
        print(lights)
        if lights:
            light_data = [{
                "room": i.room.id,
                "name": i.name,
                "color": i.color
            } for i in lights]
            return JsonResponse({'lights': light_data}, safe=False)
        else:
            return HttpResponseNotFound()
    

