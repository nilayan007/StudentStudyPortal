from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #on_delete=models.CASCADE means when the user get deleted, then the notes get deleted from the db
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    class Meta:      
        verbose_name = "notes" 
        verbose_name_plural = "notes"        # its remove the extra 's' from notes in django admin panel 
    def __str__(self):
        return self.title       # for display the object name to its title name 



class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #on_delete=models.CASCADE means when the user get deleted, then the notes get deleted from the db
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    descriptions=models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title       # for display the object name to its title name 
 
 
 
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title   
                