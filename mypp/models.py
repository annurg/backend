from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Year(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, related_name='cities')
    year = models.FloatField(max_length=4)
    temperature = models.FloatField(max_length=3, default=40)

    # def __str__(self):
    #     return str(self.year)