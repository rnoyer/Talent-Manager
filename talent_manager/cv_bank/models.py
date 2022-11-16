from django.db import models

# Create your models here.
class Roles(models.Model):
    role = models.CharField(max_length=50)

class Skills(models.Model):
    skill = models.CharField(max_length=50)

class Collabs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    resume = models.FileField(upload_to='cvteque/')
    roles = models.ManyToManyField(Roles)
    skills = models.ManyToManyField(Skills)
    # birthday = models.DateField(auto_now=False, auto_now_add=False)
    # About_him = models.CharField(max_length=300)
    # education
    # Photo
    # Living country
    # Expertise (many) > info dans la table xp précedente
    # Education (many)
    # Certifications (many)
    # Langues parlés (many)
    # Expériences précédentes (many)
