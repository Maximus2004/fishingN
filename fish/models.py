from django.db import models


class DuoReg(models.Model):
    user = models.CharField(max_length=50, default='')  # ограниченый размер переменной
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user
