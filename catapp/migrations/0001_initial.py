# Generated by Django 3.0.6 on 2020-05-28 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=1024)),
                ('building_type', models.PositiveSmallIntegerField(choices=[(1, 'Landed'), (2, 'Condominium')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catapp.Home')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='catapp.Breed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='catapp.Human')),
            ],
        ),
    ]