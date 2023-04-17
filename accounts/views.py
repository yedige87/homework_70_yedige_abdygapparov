from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import LoginForm, CustomUserCreationForm


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        print(request.GET, 'get')
        next = request.GET.get('next')
        if next:
            return redirect('/auth/accounts/create/')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        print(request.POST, 'post')
        print(request.GET, 'get')

        if not form.is_valid():
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('index')
        login(request, user)

        messages.success(request, f'Добро пожаловать, {user.username} !')

        next = request.GET.get('next')
        if next:
            return redirect(next)

        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)

# def register_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
