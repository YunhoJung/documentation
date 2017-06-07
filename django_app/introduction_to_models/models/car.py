from django.db import models



class ManuFacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        ManuFacturer,
        # myapp.Manufacturer
        # introduction_to_models.Manufacturer
        on_delete=models.CASCADE,
    )
    # related_name과 related_query_name의 차이

    def __str__(self):
        return self.name


