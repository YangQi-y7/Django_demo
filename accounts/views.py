from django.shortcuts import render, redirect
from . import forms, models
from recreation.models import Article, Video
# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    article_num = Article.objects.count()
                    video_num = Video.objects.count()
                    image = user.image
                    request.session['article_num'] = article_num
                    request.session['video_num'] = video_num
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['image'] = image
                    return redirect('/')
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在"
        else:
            message = login_form.errors
    else:
        login_form = forms.LoginForm()
    return render(request, 'accounts/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == "POST":
        register_form = forms.UserForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['name']
            password = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password != password2:
                message = "两次输入的密码不同！"
                return render(request, 'accounts/register.html', locals())
            else:
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱'
                    return render(request, 'accounts/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/')
        else:
            message = register_form.errors
    else:
        register_form = forms.UserForm()
    return render(request, 'accounts/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    request.session.flush()
    return redirect('/')


def my_space(request):
    context = {}
    user_id = request.session.get('user_id')
    my_article_num = Article.objects.filter(publisher=user_id).count()
    my_video_num = Video.objects.filter(publisher=user_id).count()
    user = models.User.objects.get(id=user_id)
    context["user_id"] = user_id
    context["my_article_num"] = my_article_num
    context["my_video_num"] = my_video_num
    context["user"] = user

    # request.session['image'] = user.image
    return render(request, 'accounts/my_space.html', context)
