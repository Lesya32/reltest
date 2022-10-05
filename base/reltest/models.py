from django.db import models


class MPS(models.Model):
    MPS = models.IntegerField(db_column='MPS', primary_key=True, unique=True)
    NAME = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MPS'

    def __str__(self):
        return self.NAME