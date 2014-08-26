from django.contrib import admin
from models import Schedule, Visitor, VisitorSchedule, Court, Member, MemberSchedule


class VisitorScheduleInline(admin.TabularInline):
    model = VisitorSchedule


class MemberScheduleInline(admin.TabularInline):
    model = MemberSchedule


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        VisitorScheduleInline, MemberScheduleInline,
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