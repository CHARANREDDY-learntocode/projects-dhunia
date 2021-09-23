from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from django.conf import settings

# Create your models here.
class Technology(models.Model):
    class Meta:
        verbose_name = 'Technologie'

    name = models.CharField(max_length=50, help_text='Name of the Technology')

    def __str__(self):
        return f'{self.name}'


class Tool(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the Tool')

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField('Project Name', max_length=200, help_text='Name of the project')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField('Project Description', help_text='Description of the project')
    technology = models.ManyToManyField(Technology, help_text='Technology used in the project')
    tools =  models.ManyToManyField(Tool, help_text='Tools(Programming Languages, frameworks, others) used in the project')
    hardware_used = models.CharField('Hardware Used', max_length=300, help_text='Hardware materials used in the project', blank=True)
    price = models.IntegerField('Price in INR(₹)')
    video_demo_link = models.CharField('Youtube Video Link', max_length=80)
    time_of_upload = models.DateTimeField('Time of upload', auto_now_add=True)
    quantity = models.SmallIntegerField(validators=[MinValueValidator(1),])
    pdf_available = models.FileField('PDF file available', blank=True, upload_to='PDF-Files')

    def __str__(self):
        return f'{self.name}'