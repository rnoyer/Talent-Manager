from django.db import models

# Create your models here.
class Roles(models.Model):
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ("Roles")

    def __str__(self):
        return self.role

class Skills(models.Model):
    skill = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ("Skills")

    def __str__(self):
        return self.skill

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

    class Meta:
        verbose_name_plural = ("Collabs")

    def __str__(self):
        collab = f"{self.last_name.upper()} {self.first_name.capitalize()}"
        return collab

    def get_roles(self):
        return " / ".join([r.role.capitalize() for r in self.roles.all()])

    def get_skills(self):
        return " / ".join([s.skill.capitalize() for s in self.skills.all()])
