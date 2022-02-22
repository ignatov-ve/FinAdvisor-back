from django.db import models


# Create your models here.

class Okved(models.Model):
    okved = models.CharField(max_length=8, primary_key=True, null=False)
    name = models.CharField(max_length=512, null=False)

    class Meta:
        db_table = 'okveds'
