from django.db import models


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) # 다중 일 (기사 한 명이 여러 기사 씀) r.article_set하면 r은 article에 접근가능해짐 r은 기사 하나받음 ?

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
