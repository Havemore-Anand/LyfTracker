from django.db import models

# Create your models here.
class GuestBook(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class status (models.Model):
    activity = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)

    def __str__(self):
        return self.activity

class Recent_Act(models.Model):
    time =  models.CharField(max_length=100)
    Work = models.CharField(max_length=100)

    def __str__(self):
        return self.time

class Journal(models.Model):
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to="journal/")
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
    


class Like(models.Model):
    post = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like on {self.post.caption}"    
     

class Timetable(models.Model):
    DAYS = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    ]

    day = models.CharField(max_length=10, choices=DAYS)
    time = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    attendance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.day} - {self.subject}"     
        
class Socials(models.Model):
    text = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.text       