from django.db import models

# Create your models here.
# when I cannot migrate model after deleting existing table
# http://stackoverflow.com/questions/29888046/django-1-8-create-initial-migrations-for-existing-schema
class Item(models.Model):
	text = models.TextField(default="")
