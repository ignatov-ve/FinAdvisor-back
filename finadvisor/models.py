from django.db import models


# Create your models here.

class Okved(models.Model):
    okved = models.CharField(max_length=8, primary_key=True, null=False)
    name = models.CharField(max_length=512, null=False)
    industry_code = models.CharField(max_length=2, null=False, default='00')

    class Meta:
        db_table = 'ci_okveds'


class Industry(models.Model):
    code = models.CharField(max_length=2, primary_key=True, null=False)
    name = models.CharField(max_length=512, null=False)

    class Meta:
        db_table = 'industries'


class Region(models.Model):
    code = models.CharField(max_length=2, primary_key=True, null=False)
    name = models.CharField(max_length=512, null=False)

    class Meta:
        db_table = 'regions'
