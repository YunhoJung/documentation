from django.db import models


class TimeStampedMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # 생성될 때 한번만
    modified_date = models.DateTimeField(auto_now=True)  # 수정할 때마다

    class Meta:
        abstract = True
