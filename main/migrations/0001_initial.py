# Generated by Django 2.2.10 on 2020-05-25 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(default='p', max_length=1)),
                ('payment', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+ Type'), ('A-', 'A- Type'), ('B+', 'B+ Type'), ('B-', 'B- Type'), ('AB+', 'AB+ Type'), ('AB+', 'AB- Type'), ('O+', 'O+ Type'), ('O-', 'O- Type')], max_length=2, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_working', models.BooleanField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('attendence', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+ Type'), ('A-', 'A- Type'), ('B+', 'B+ Type'), ('B-', 'B- Type'), ('AB+', 'AB+ Type'), ('AB+', 'AB- Type'), ('O+', 'O+ Type'), ('O-', 'O- Type')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_receptionist', models.BooleanField(default=False)),
                ('is_hr', models.BooleanField(default=False)),
                ('user_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=200)),
                ('prescription', models.TextField()),
                ('appoint', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to='main.Appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_prescription', to='main.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_prescription', to='main.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='main.UserCategory'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='main.UserCategory'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointment', to='main.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to='main.Patient'),
        ),
    ]
