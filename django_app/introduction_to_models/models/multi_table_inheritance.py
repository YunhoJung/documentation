from django.db import models


# abstract model이랑 비교하기
# abstract model은 데이터가 db에 존재하지 않기 때문에 상속받는 두 클래스는 기능은 동일하게 가지지만 독립적인 객체이다
# 반면에 multi_table_inheritance model은 데이터가 db에 존재하기 때문에 상속받는 두 클래스는 연결되어 있다.
# student2 teacher2가 commoninfo에 저장됨


class CommonInfo2(models.Model): # 자체적으로 pk가 없고 상속받은 두 클래스의 pk를 가져온다. 한마디로 엮여있다.
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ('-name',)
        db_table = 'introduction_to_models_mti_commoninfo2'


class Student2(CommonInfo2):
    home_group = models.CharField(max_length=5)
    extra_info = models.ForeignKey(
        CommonInfo2,
        related_name='extra_students',
        null=True,
        blank=True,
    )

    def __str__(self):
        return "HomeGroup {}\'s student({}, {})".format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student2'


class Teacher2(CommonInfo2):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {} \'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_teacher2'
