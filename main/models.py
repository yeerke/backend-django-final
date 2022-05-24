from django.db import models

class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

class Journal(BookJournalBase):
    BULLET = 1
    FOOD = 2
    TRAVEL = 3
    SPORT = 4

    type_choices = (
        (BULLET, 'bullet'),
        (FOOD, 'food'),
        (TRAVEL, 'travel'),
        (SPORT, 'sport')
    )

    type = models.PositiveSmallIntegerField(choices=type_choices, null=False)
    publisher = models.CharField(max_length=50)

