from django.shortcuts import render
from models import Schedule

def schedule_list(request):
    schedule_list = Schedule.objects.all()
    return render(request, 'scheduler/schedule_list.html', {'schedule_list': schedule_list})


