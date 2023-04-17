from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import request
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView
from django.contrib.auth.models import User

from webapp.forms import SearchForm
from webapp.models.todos import ToDo, StatusChoice


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = ToDo
    context_object_name = 'todos'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.extra_context = {'projects': self.projects}
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = request.user
        self.projects = user.projects.all()
        print('projects =', self.projects)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(text__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'

# class IndexView(View):
#
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.exclude(is_deleted=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'index.html', context=context)
