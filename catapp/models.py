from django.db import models

MALE = 'M'
FEMALE = 'F'
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class Breed(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=MALE,
        max_length=1,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)
    breed = models.ForeignKey(
        'Breed',
        related_name='cats',
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        'Human',
        related_name='cats',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.name


class Human(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=MALE,
        max_length=1,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)
    home = models.ForeignKey(
        'Home',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.name


class Home(models.Model):
    LANDED = 1
    CONDOMINIUM = 2
    BUILDING_TYPE_CHOICES = [
        (LANDED, 'Landed'),
        (CONDOMINIUM, 'Condominium'),
    ]
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=1024)
    building_type = models.PositiveSmallIntegerField(
        choices=BUILDING_TYPE_CHOICES,
        default=LANDED,
    )

    def __str__(self):
        return self.name
