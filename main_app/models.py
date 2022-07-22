from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Hat(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
    name=models.CharField(max_length=100)
    typeof=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    age=models.IntegerField()
    #Adding Many to Many
    hats = models.ManyToManyField(Hat)

    def __str__(self):
        return self.name
    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

# change the default sort
  class Meta:
    ordering = ['-date']