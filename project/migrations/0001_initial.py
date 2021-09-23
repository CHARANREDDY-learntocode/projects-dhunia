# Generated by Django 3.2 on 2021-04-07 05:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Technology', max_length=50)),
            ],
            options={
                'verbose_name': 'Technologie',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Tool', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the project', max_length=200, verbose_name='Project Name')),
                ('description', models.TextField(help_text='Description of the project', verbose_name='Project Description')),
                ('hardware_used', models.CharField(blank=True, help_text='Hardware materials used in the project', max_length=300, verbose_name='Hardware Used')),
                ('price', models.IntegerField(verbose_name='Price in INR(₹)')),
                ('video_demo_link', models.CharField(max_length=80, verbose_name='Youtube Video Link')),
                ('time_of_upload', models.DateTimeField(auto_now_add=True, verbose_name='Time of upload')),
                ('quantity', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('pdf_available', models.FileField(blank=True, upload_to='PDF-Files', verbose_name='PDF file available')),
                ('technology', models.ManyToManyField(help_text='Technology used in the project', to='project.Technology')),
                ('tools', models.ManyToManyField(help_text='Tools(Programming Languages, frameworks, others) used in the project', to='project.Tool')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]