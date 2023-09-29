from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Workout(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    date = models.DateField(editable=True, null=True, blank=False, unique=True)
    description = models.TextField(null=True, blank=False)

    def __str__(self): # ca un fel de toString, doar ca returnam doar titlul
        return self.title

    class Meta:
        ordering = ['date']

# un data base table. Tinem ca intr-o baza de date
# Prima clasa
# asta va fi workout
class ClasaPrincipala(models.Model):
    # many to 1 relation. 1 user poate avea mai multe task-uri
    # on delete inseamna ce facem cand stergem userul cu taskurile. Aici inseamna ca
    # toate taskurile se termina odata cu userul
    # null=True. Nu stiu exact, nu stiu daca e crucial. Cumva pentru un user
    # putem sa nu avem taskuri cred
    # User e o clasa, probabil userii pe care ii avem in sistem

    objects = models.Manager()

    listaParticipanti = models.CharField(editable=False, max_length=300, null=True, blank=True)
    counterParticipanti = models.IntegerField(editable=False, null=True, blank=True)

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=False)

    oraInceput = models.TimeField(editable=True, null=True, blank=False)
    title = models.CharField(max_length=200, null=True, blank=False)

    # pentru momentul in care il facem, salveaza automat data
    create = models.DateTimeField(auto_now_add=True)

    complete = models.BooleanField(editable=True, default=False)

    def __str__(self): # ca un fel de toString, doar ca returnam doar titlul
        return self.title

    class Meta:
        # asa se ordoneaza un query set? intr-un fel in functie de complete
        # cumva in functie de daca este completat, atunci il ordoneaza primul cred
        # probabil putem ordona si in functie de mai multe, daca scriem mai multe in lista
        ordering = ['workout']

# dupa ce am scris asta a trebuit sa fac python manage.py makemigrations
# asta a facut un fisier 0001_initial.py in folderul migrations
# dupa trebuie python migrate

