from django.shortcuts import render
from models import Schedule

def schedule_list(request):
    schedule_list = Schedule.objects.all().select_related(depth=1)
    return render(request, 'scheduler/schedule_list.html', {'schedule_list': schedule_list})


