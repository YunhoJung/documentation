from django.db import models

from introduction_to_models.models import Car


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    cars = models.ManyToManyField(
        Car,
        related_name='%(app_label)s_%(class)ss',
        related_query_name='%(app_label)s_%(class)s',  # 안에 요소 검사할때
    #
    )

    # cars필드에 MTM으로
    # related_name, related_query_name을 설정 후 migrate
    # 이 둘의 차이 ? 이것은 하나의 매니저 만드는 것 동적으로 해야 오류가 안걸림.  m2m으로 서로 얽혀있기때문에.

    class Meta:
        abstract = True  # class는 있으나 데이터베이스에는 없음
        ordering = ('-name',)


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return "HomeGroup {}\'s student({}, {})".format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student' # Student 클래스와 Teacher 클래스가 모두 CommonInfo를 상속받기때문에 db_table 테이블 이름이 겹치게 된다. 이를 막기 위해 이름을 따로 지정해준다.


class Teacher(CommonInfo):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {} \'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_teacher'
