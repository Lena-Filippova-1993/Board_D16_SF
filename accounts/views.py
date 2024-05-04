import random

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import *
from django.core.mail import send_mail
import random


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/posts'
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=SignUpForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        return redirect('code', request.POST['username'])

class GetCode(CreateView):
    template_name='registration/code.html'

    def get_context_data(self, **kwargs):
        name_user=self.kwargs.get('user')
        if not OneTimeCode.objects.filter(user=name_user).exists():
            code = ''.join(random.sample('abracadabra1993', 8))
            OneTimeCode.objects.create(user=name_user, code=code)
            user = User.objects.get(username=name_user)
            send_mail(
                subject=f'Код активации',
                message=f'{code}',
                from_email='lena-filippova-93@mail.ru',
                recipient_list=[user.email],
            )


    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user=request.path.split('/')[-1]
            if OneTimeCode.objects.filter(code=request.POST['code'], user=user).exists():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code'], user=user).delete()
            else:
                return render(self.request, 'registration/invalid_code.html')
        return redirect('login')



