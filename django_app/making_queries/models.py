from django.db import models

# queryset은 데이터베이스에 할당되지 않는다.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(blank=True)
    pub_date = models.DateField(null=True)
    mod_date = models.DateField(auto_now_add=True, null=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return '{} ({})'.format(
            self.headline,
            self.pub_date,
        )
# '''
# 쿼리와 쿼리셋의 차이
# In [43]: Blog.objects.filter(Q(entry__headline__contains='Lennon') & Q(entry__pub_date__year=2017))
# Out[43]: <QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>]>
#
# In [44]: Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2017)
# Out[44]: <QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>, <Blog: This blog has (Lennon, 2017) and (Other, 2008)>]>
#
# In [45]: Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2017)
# Out[45]: <QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>]>
# 3가지의 차이 인지하기 !
# '''
#
# In [47]: Blog.objects.exclude(entry__headline__contains='Lennon', entry__pub_date__year=2008)
# Out[47]: <QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>]>
#
# In [48]: Blog.objects.exclude(entry__headline__contains='Lennon').exclude(entry__pub_date__year=2008)
# Out[48]: <QuerySet []>
# In [51]: Blog.objects.exclude(entry__in=Entry.objects.filter(headline__contains='Lennon', pub_date__year=2008))
# Out[51]: <QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>]>
#

# A N B -> filter
# ~(A N B) -> exclude 계산
# ~A U ~B -> exclude 실제 값

# pingback
# .pk = None하면 복사할 떄 용이.
# _set.all -> 역참조