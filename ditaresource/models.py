from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Client(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=60)


class Specialist(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=60)
    speciality = models.CharField(max_length=60)


class Tutor(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=60)


class TutorAvailability(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    datee = models.DateField()
    timeStart = models.TimeField(default=timezone.now().time())
    timeEnd = models.TimeField(null=True)


class Unitss(models.Model):
    course = models.CharField(max_length=15)
    unitCode = models.CharField(max_length=10)
    unitName = models.CharField(max_length=29)


class TutorUnitss(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unitss, on_delete=models.CASCADE)


class ClientTutorSession(models.Model):
    tutorAvailability = models.ForeignKey(TutorAvailability, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)


class Issue(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    issue = models.CharField(max_length=60)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(null=True)
    STATUS_CHOICES = [
        ("RECEIVED", "Received"),
        ("COMPLETED", "Completed"),
        ("PENDING", "Pending"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    def __str__(self):
        return self.username
