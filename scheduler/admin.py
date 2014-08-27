from django.contrib import admin
from models import Schedule, Visitor, VisitorSchedule, Court, Member, MemberSchedule, HelperSchedule


class VisitorScheduleInline(admin.TabularInline):
    model = VisitorSchedule
    extra = 2

class MemberScheduleInline(admin.TabularInline):
    model = MemberSchedule
    extra = 6


class HelperScheduleInline(admin.TabularInline):
    model = HelperSchedule
    extra = 2


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        VisitorScheduleInline, MemberScheduleInline, HelperScheduleInline,
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
admin.site.register(Member, MemberAdmin)