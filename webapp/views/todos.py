from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.utils.http import urlencode

from webapp.forms import ToDoForm, SearchForm, ProjectForm, UserUpdateForm
from webapp.models import Project
from webapp.models.todos import ToDo

class GroupPermissionCreateMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager', 'TeamLead', 'Developer'  ]).exists()

class ToDoCreateView(GroupPermissionCreateMixin, LoginRequiredMixin, CreateView):
    template_name = 'todo_create.html'
    model = ToDo
    form_class = ToDoForm

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class ToDoDetail(DetailView):
    template_name = 'todo.html'
    model = ToDo


class GroupPermissionEditMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager', 'TeamLead', 'Developer'  ]).exists()


class ToDoUpdateView(GroupPermissionEditMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'todo_update.html'
    form_class = ToDoForm
    model = ToDo
    success_message = 'Задача обновлена'
    groups = ['Admin', 'Manager']

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


# class ArticleUpdateView(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'article_update.html'
#     form_class = ArticleForm
#     model = Article
#     success_message = 'Статья обновлена'
#     permission_required = 'webapp.change_article'
#     # permission_denied_message = 'У Вас не хватает прав доступа'

# class ToDoUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'todo_update.html'
#     form_class = ToDoForm
#     model = ToDo
#
#     def get_success_url(self):
#         return reverse('todo_detail', kwargs={'pk': self.object.pk})
class GroupPermissionDeleteMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager', 'TeamLead']).exists()

class ToDoDeleteView(GroupPermissionDeleteMixin, LoginRequiredMixin, DeleteView):
    template_name = 'todo_confirm_delete.html'
    model = ToDo
    success_url = reverse_lazy('index')

class ProjectTasksView(LoginRequiredMixin, ListView):
    template_name = 'project_tasks.html'
    model = ToDo
    context_object_name = 'todos'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1
    #project = Project.objects.get(pk=project_id)
    #extra_context = {'project': project}

    def get(self, request, *args, **kwargs):
        self.project_id = kwargs['project_id']
        print('project_id =', self.project_id)
        print(request)
        project = Project.objects.get(pk=self.project_id)
        print(project.project)
        users = project.users.all()
        print(users)
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.extra_context = {'users': users}
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.project_id:
            print('self.project_id =', self.project_id)
            query = Q(project=self.project_id)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

class ProjectsView(LoginRequiredMixin, ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('created_at',)

class GroupPermissionCreateProjectMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

class ProjectCreateView(GroupPermissionCreateProjectMixin, LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('projects_view')

class GroupPermissionUpdateProjectMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

class ProjectUpdateView(GroupPermissionUpdateProjectMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project_update.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class GroupPermissionUpdateProjectUsersMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager', 'TeamLead']).exists()

class ProjectUsersUpdateView(GroupPermissionUpdateProjectUsersMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project_users_update.html'
    model = Project
    form_class = UserUpdateForm
    success_message = 'Проект обновлен'
    groups = ['Admin', 'Manager', 'TeamLead']

    def get_success_url(self):
        return reverse('projects_view')


class ProjectToDoCreateView(LoginRequiredMixin, CreateView):
    initial = {'project_id': '1'}
    template_name = 'project_todo_create.html'
    model = ToDo
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        print('request = ', request)
        print('args = ', args)
        print('kwargs = ', kwargs)
        pk = kwargs['pk']
        print('pk = ', pk)
        args = (pk,)
        print('args = ', args)
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('projects_view')


class GroupPermissionDeleteProjectMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

class ProjectDeleteView(GroupPermissionDeleteProjectMixin, LoginRequiredMixin, DeleteView):
    template_name = 'project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('projects_view')


class ProjectDetail(DetailView):
    template_name = 'project.html'
    model = Project