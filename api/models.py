from django.db import models

# Create your models here.
class Proc(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=400)
    mem = models.FloatField(null=True)
    cpu = models.FloatField(null=True)
    disk = models.FloatField(null=True)
    gpu = models.FloatField(null=True)
    network = models.FloatField(null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
