from django.db import models
import os

# Function to change the name of the uploaded CSV file
def name_change(instance, filename):
    path = 'csv_files/'
    return os.path.join(path, 'squares.csv')


class SquaresCSV(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=name_change)


class Players(models.Model):
    player = models.CharField(max_length=2)
    first_round = models.IntegerField(default=0)
    second_round = models.IntegerField(default=0)
    sweet_sixteen = models.IntegerField(default=0)
    elite_eight = models.IntegerField(default=0)
    final_four = models.IntegerField(default=0)
    championship = models.IntegerField(default=0)


class WinningNumbers(models.Model):
    spot1 = models.IntegerField(default=0)
    spot2 = models.IntegerField(default=1)
    spot3 = models.IntegerField(default=2)
    spot4 = models.IntegerField(default=3)
    spot5 = models.IntegerField(default=4)
    spot6 = models.IntegerField(default=5)
    spot7 = models.IntegerField(default=6)
    spot8 = models.IntegerField(default=7)
    spot9 = models.IntegerField(default=8)
    spot10 = models.IntegerField(default=9)


class LosingNumbers(models.Model):
    spot1 = models.IntegerField(default=0)
    spot2 = models.IntegerField(default=1)
    spot3 = models.IntegerField(default=2)
    spot4 = models.IntegerField(default=3)
    spot5 = models.IntegerField(default=4)
    spot6 = models.IntegerField(default=5)
    spot7 = models.IntegerField(default=6)
    spot8 = models.IntegerField(default=7)
    spot9 = models.IntegerField(default=8)
    spot10 = models.IntegerField(default=9)