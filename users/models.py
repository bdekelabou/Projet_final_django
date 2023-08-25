from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Étudiant'),
        ('teacher', 'Enseignant'),
        ('admin', 'Administrateur'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    student_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    teacher_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    
    # Ajoutez les arguments related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.',
    )
    
    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    project_file = models.FileField(upload_to='projects/')  # Assurez-vous d'avoir le dossier 'projects/' configuré dans vos paramètres
    status = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traité', 'Traité'), ('archivé', 'Archivé')])

class ProjectAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploads/')  # Assurez-vous d'avoir le dossier 'uploads/' configuré dans vos paramètres
    submitted = models.BooleanField(default=False)

class ProcessedProject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    processed_file = models.FileField(upload_to='processed/')  # Assurez-vous d'avoir le dossier 'processed/' configuré dans vos paramètres




