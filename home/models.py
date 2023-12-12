# models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()


def __str__(self):
  return self.name
# ye object ka name contact 1, contact 2 ke jgh pe name se display krne k liye ye customisation lga skte hai isee jo str se return krwaaenge us object ka name ko wo display krega 

    