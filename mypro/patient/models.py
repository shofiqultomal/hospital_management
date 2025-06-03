from django.db import models

# Create your models here.
GENDER_CHOICES=(
    ('male','Male'),
    ('female','Female'),
    ('other','other'),
)

class patient (models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES,default='male')
    mobile = models.IntegerField(null=True)
    detail = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    next_visit = models.IntegerField(default=0)
