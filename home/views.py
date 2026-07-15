from django.shortcuts import redirect, render, HttpResponse
from home.models import GuestBook,status,Recent_Act,Journal,Timetable,Socials
from django.contrib import messages


# Create your views here.
def index(request):
   if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("messages")

        GuestBook.objects.create(
            name=name,
            message=message
        )
        
        
        return redirect("/?success=1")
   Status = status.objects.first()
   r = Recent_Act.objects.first()
   posts = Journal.objects.all()
   timetable = Timetable.objects.all().order_by("day", "time")
   socials = Socials.objects.all()
   
   #print("Activity:", Status.activity)
      
   return render(request, "index.html", {
       "status" : Status,
       "Recent_Act" : r,
       "posts" : posts,
        "timetable": timetable,
        "socials" : socials

   })

