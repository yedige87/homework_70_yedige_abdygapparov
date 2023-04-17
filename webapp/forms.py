import re
from datetime import datetime

from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ValidationError

from webapp.models import ToDo, Project


def check_date(ymd):
    pattern = '\d\d\d\d-\d\d-\d\d'
    result = ' Ошибки: '
    if re.fullmatch(pattern, ymd):
        year = int(ymd[0:4])
        month = int(ymd[5:7])
        day = int(ymd[8:10])
        print(year, month, day)
        if year < 2000 or year > 2100:
            result += 'Год за пределами столетия. '
        if month < 1 or month > 12:
            result += 'Месяц за пределами 1-12. '
        if day < 1 or day > 31:
            result += 'День за пределами 1-31. '

        if result == ' Ошибки: ':
            try:
                new_date = datetime.strptime(ymd, "%Y-%m-%d")
            except ValueError:
                result += 'Введите корректный день для данного месяца !'
            else:
                print(new_date)
                result = ' Корректно!'

    else:
        result += 'Введите дату в формате ГГГГ-ММ-ДД !'
    return result


class ToDoForm(forms.ModelForm):
    # project = forms.CharField(disabled=True)

    class Meta:
        model = ToDo
        fields = ('title', 'text', 'deadline', 'status', 'project', 'type')
        labels = {
            'title': 'Задача',
            'text': 'Описание',
            'deadline': 'Дедлайн',
            'status': 'Статус',
            'project': 'Проект',
            'type': 'Тип'
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        result = check_date(deadline)
        if result != ' Корректно!':
            raise ValidationError(result)
        return deadline

    def clean_title(self):
        title_form = str(self.cleaned_data.get('title'))
        title_init = str(self.__dict__.get('instance'))

        if len(title_form) <= 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        if ToDo.objects.filter(title=title_form).exists() and title_form != title_init:
            raise ValidationError('Заголовок с таким именем уже есть! Введите другой заголовок.')
        return title_form


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project', 'text', 'date_start', 'date_end')
        labels = {
            'project': 'Проект',
            'text': 'Описание',
            'date_start': 'Начало',
            'date_end': 'Окончание'
        }

class UserUpdateForm(forms.ModelForm):

    project = forms.CharField(disabled=True)

    class Meta:
        model = Project
        fields = ('project', 'users',)
        labels = {
            'project': 'Проект',
            'users': 'Работники'
        }
