from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[
        ('homme', 'Homme'),
        ('femme', 'Femme'),
        ('autre', 'Autre'),
    ])
    orientation = models.CharField(max_length=20, choices=[
        ('hetero', 'Hétérosexuel'),
        ('homosexuel', 'Homosexuel'),
        ('asexuel', 'Asexuel'),
        ('bisexuel', 'Bisexuel'),
        ('pansexuel', 'Pansexuel'),
        ('queer', 'Queer'),
    ])
    birth_year = models.IntegerField()
    country = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=15, choices=[
        ('celibataire', 'Célibataire'),
        ('marie', 'Marié(e)'),
        ('veuf', 'Veuf(ve)'),
        ('divorce', 'Divorcé(e)'),
    ])

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)  # Champ pour stocker l'intérêt sélectionné

    def __str__(self):
        return f'{self.user.username} - {self.interest}'

