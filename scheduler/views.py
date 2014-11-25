from django.shortcuts import render
from models import Schedule, VisitorSchedule, MemberSchedule, HelperSchedule
from datetime import datetime


def schedule_list(request):
    schedule_list = Schedule.objects.filter(event_date__gte=datetime.now()).select_related()

    for schedule in schedule_list:
        visitor_schedules = VisitorSchedule.objects.filter(schedule_id=schedule.id).select_related()
        schedule.visitor_schedules = visitor_schedules

        member_schedules = MemberSchedule.objects.filter(schedule_id=schedule.id)
        schedule.member_schedules = member_schedules

        helper_schedules = HelperSchedule.objects.filter(schedule_id=schedule.id)
        schedule.helper_schedules = helper_schedules

    return render(request, 'scheduler/schedule_list.html', {'schedule_list': schedule_list})

