

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Kabbadi(models.Model):
    sl_no = models.AutoField(primary_key=True)  # AutoField for unique sl_no
    dept_no = models.IntegerField(unique=True)  # dept_no as IntegerField, unique
    nation = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Dept No: {self.dept_no}, State: {self.state}"

class StateTournament(models.Model):
    sl_no = models.AutoField(primary_key=True)  # AutoField for unique sl_no
    location = models.CharField(default="India", max_length=100)

    # Choices for places field
    INDIA = 'India'
    ABROAD = 'Abroad'
    PLACES_CHOICES = [
        (INDIA, 'India'),
        (ABROAD, 'Abroad'),
    ]
    
    places = models.CharField(
        max_length=6,  # The length of the string can be at most the length of "Abroad"
        choices=PLACES_CHOICES,
        default=INDIA,  # Default value is "India"
    )

    dept_no = models.ForeignKey(Kabbadi, on_delete=models.CASCADE)

    def __str__(self):
        return f"Location: {self.location}, Places: {self.places}"

class Team(models.Model):
    sl_no = models.AutoField(primary_key=True)  # AutoField for unique sl_no
    dept_no = models.ForeignKey(Kabbadi, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=20, null=True)
    player_age = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(38)])

    def __str__(self):
        return f"Player Name: {self.player_name}, Age: {self.player_age}, Dept No: {self.dept_no.dept_no}"
