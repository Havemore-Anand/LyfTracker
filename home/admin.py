from django.contrib import admin
from home.models import GuestBook, status, Recent_Act, Journal,Like,Timetable,Socials


# Register your models here.
admin.site.register(GuestBook)
admin.site.register(status)
admin.site.register(Recent_Act)
admin.site.register(Journal)
admin.site.register(Like)
admin.site.register(Timetable)
admin.site.register(Socials)
