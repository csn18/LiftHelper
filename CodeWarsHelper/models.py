from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=128)
    start_date = models.DateField()

    def __str__(self):
        return f'{self.name_group}'

    class Meta:
        db_table = 'group'
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'


class Subdivision(models.Model):
    division_name = models.CharField(max_length=128)

    def __str__(self):
        return self.division_name

    class Meta:
        db_table = 'subdivision'
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Members(models.Model):
    member_name = models.CharField(max_length=128)
    member_division = models.ForeignKey(Subdivision, on_delete=models.CASCADE, default=0)
    member_group = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)
    code_wars_username = models.CharField(max_length=64, default='')
    progress = models.FloatField(max_length=8, default=0, blank=True)

    def __str__(self):
        return f'{self.member_name}'

    class Meta:
        db_table = 'members'
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class TypeTaskCodeWars(models.Model):
    name_type = models.CharField(max_length=128)

    def __str__(self):
        return self.name_type

    class Meta:
        db_table = 'type_tasks'
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'


class TaskKyuLevel(models.Model):
    task_level = models.CharField(max_length=16)

    def __str__(self):
        return self.task_level

    class Meta:
        db_table = 'task_levels'
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


class CodeWarsTasks(models.Model):
    id_task = models.CharField(max_length=128)
    kyu_level = models.ForeignKey(TaskKyuLevel, default=0, on_delete=models.CASCADE)
    type_task = models.ForeignKey(TypeTaskCodeWars, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_task

    class Meta:
        db_table = 'code_wars_tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


