from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    mobile_number = models.CharField(default="", max_length=10)
    department = models.CharField(max_length=10, default="")
    city = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name + '-' + self.email
