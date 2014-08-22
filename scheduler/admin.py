from django.contrib import admin
from models import Schedule, Visitor, VisitorSchedule, Court, Member


class VisitorScheduleInline(admin.TabularInline):
    model = VisitorSchedule


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        VisitorScheduleInline,
    ]


class VisitorAdmin(admin.ModelAdmin):
    pass


class CourtAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Court, CourtAdmin)
