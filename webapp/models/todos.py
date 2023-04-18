from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'new', 'Новая'
    IN_PROGRESS = 'in_progress', 'Выполняется'
    DONE = 'done', 'Завершена'


class ToDo(models.Model):
    status = models.CharField(choices=StatusChoice.choices, default=StatusChoice.NEW, verbose_name='Статус',
                              max_length=20)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    deadline = models.CharField(max_length=20, null=False, blank=False, verbose_name='Исполнить до')
    project = models.ForeignKey(verbose_name='Project', to='webapp.Project', related_name='todo', null=True,
                                blank=False, on_delete=models.CASCADE)
    type = models.ForeignKey(verbose_name='Type', to='webapp.Type', null=True, blank=False, related_name='todo',
                             on_delete=models.CASCADE)
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
