from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from ..forms import RegisterForm, RegisterUpdateForm


def register(request):

    form = RegisterForm()

    #messages.info(request,'Um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )


def user_update(request):

    form  = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )

    form = RegisterUpdateForm(data = request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )

    form.save()

    return redirect('contact:user_update')


def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':

        form  = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')

            return redirect('contact:index')

        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )


def logout_view(request):
    print('WE')
    auth.logout(request)
    return redirect('contact:login')