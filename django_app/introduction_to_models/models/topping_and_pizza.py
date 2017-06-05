from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고 있는 토핑목록을 뒤에 출력
        # ex) 치즈피자 (치즈, 토마토소스)
        # topping_string = ''
        # for topping in self.topping.all():
        #     topping_string += topping.name
        #     topping_string += ', '
        #
        # topping_string = topping_string[:-2]
        # return '{} ({})'.format(self.name, topping_string)
        # str.join, list comprehension을 사용해서 한 줄로 줄이기
        return '{}의 토핑 : {}'.format(self.name, ', '.join(t.name for t in self.topping.all()))


    class Meta:
        ordering = ('name',)

# M2M에서는 중간에 pk를 공유하는 테이블이 생겨서 공유
