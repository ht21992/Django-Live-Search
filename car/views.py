from django.shortcuts import render
from .models import Car
import json
# Create your views here.

def main(request):
    json_data = list(Car.objects.values())
    manufacturer_number = len(Car.objects.values('make',).distinct().order_by())
    cars = Car.objects.all()
    context ={'cars':cars, 'json_data': json.dumps(json_data),'checkbox_number':manufacturer_number}
    return render(request, 'car/main.html',context= context)
