from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Compte(models.Model):
    ROLE_CHOICES=(
        ('P','PATIENT'),
        ('M','MEDECIN')
        )
    roles=models.CharField(max_length=10, choices=ROLE_CHOICES, default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    def  __str__(self):
         return self.user.username 
class Utilisateur(models.Model):
    SEXE_CHOICES=(
        ('H','Homme'),
        ('F','Femme'),
        )
    compte=models.ForeignKey(Compte,on_delete=models.CASCADE,default=True)
    sexe=models.CharField(max_length=10, choices=SEXE_CHOICES,default=True)    
    class Meta:
        abstract=True

class Spécialité(models.Model):
    nom=models.CharField(max_length=200, null=True)
    def  __str__(self):
         return self.nom    


class Ville(models.Model):
    nom=models.CharField(max_length=200, null=True)
    def  __str__(self):
         return self.nom   



class Medecin(Utilisateur):
    name=models.CharField(max_length=200, null=True)
    local=models.CharField(max_length=200, null=True)
    numero_tel=models.CharField(max_length=200, null=True)
    prix_visite=models.FloatField(null=True)
    start_time= models.TimeField(null=True, blank=True)
    end_time=models.TimeField(null=True, blank=True)
    spécialité=models.ForeignKey(Spécialité,null=True, on_delete=models.SET_NULL)
    ville=models.ForeignKey(Ville,null=True,on_delete=models.SET_NULL)
    note=models.FloatField(null=True,default=True)
    
    def  __str__(self):
         return self.compte.user.username 

class Patient(Utilisateur):
    age=models.IntegerField(null=True)
    def  __str__(self):
         return self.compte.user.username

RATE_CHOICES = [
        (1, '1'),
        (2, "2"),
        (3, '3'),
        (4, '4'),
        (5, '5'),
]
class Commentaire(models.Model):
    medecin=models.ForeignKey(Medecin,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,default=True)
    body=models.TextField(max_length=200, null=True)
    rate=models.PositiveSmallIntegerField(max_length=5, default=True)
    modified = models.DateTimeField(auto_now=True)
    note=models.FloatField(null=True,default=True)
    def  __str__(self):
         return '{}-{}'.format(self.medecin.compte.user, str(self.patient.compte.user.username)) 

class Contact(models.Model):
    message=models.TextField(max_length=100, null=True)
    Name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)



    
