from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User
# Create your models here.


class Interest(models.Model):
    GENDER_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme')
    ]
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    localisation = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.gender} ({self.min_age} - {self.max_age})"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.CharField(max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    location = models.CharField(max_length=100)
    interests = models.ManyToManyField(Interest, blank=True )
  

    def __str__(self):
        return self.user.username
    
class ProfileInterests(models.Model):
    profile = models.OneToOneField(Profile, models.DO_NOTHING, primary_key=True)
    interest = models.ForeignKey(Interest, models.DO_NOTHING)

    # class Meta:
    #     managed = False
    #     db_table = 'profile_interests'
    #     unique_together = (('profile', 'interest'),)
>>>>>>> origin/second
