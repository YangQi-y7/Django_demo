from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Video
from django.views import generic
from django.conf import settings
from django.http import HttpResponse
from . import forms, models
from accounts.models import User
import os


# def upload_image(request):
#     new_image_file = request.FILES.get('new_image', None)
#     if not new_image_file:
#         message = "无上传文件!"
#     else:
#         image_url = os.path.join(settings.MEDIA_ROOT, "image", new_image_file.name)
#         destination = open(image_url, 'wb+')
#         for chunk in new_image_file.chunks():
#             destination.write(chunk)
#         destination.close()
#
#         user = User.objects.get(id=request.session.get('user_id'))
#         user.image = new_image_file.name
#         user.save()
#         return redirect('accounts:my_space')
#     return render(request, 'accounts/my_space.html', locals())


def upload_article(request):
    if request.method == "POST":
        article_form = forms.ArticleForm(request.POST)
        message = article_form.errors
        if article_form.is_valid():
            new_article = models.Article()
            new_article.publisher = User.objects.get(id=request.session.get('user_id'))
            new_article.title = article_form.cleaned_data['title']
            new_article.description = article_form.cleaned_data['description']
            new_article.part_1 = article_form.cleaned_data['part_1']
            new_article.part_2 = article_form.cleaned_data['part_2']
            new_article.part_3 = article_form.cleaned_data['part_3']
            new_article.save()
            request.session['article_num'] = Article.objects.count()
            return redirect('accounts:my_space')
    else:
        article_form = forms.ArticleForm()
    return render(request, 'recreation/article_upload.html', locals())


def upload_video(request):
    if request.method == 'POST':
        video_form = forms.VideoForm(request.POST)
        message = video_form.errors
        if video_form.is_valid():
            new_video = models.Video()
            new_video.publisher = User.objects.get(id=request.session.get('user_id'))
            new_video.title = video_form.cleaned_data['title']
            new_video.description = video_form.cleaned_data['description']
            new_video.url = video_form.cleaned_data['url']
            new_video.save()

            request.session['video_num'] = Video.objects.count()
            return redirect('accounts:my_space')
    else:
        video_form = forms.VideoForm(request.POST)
    return render(request, 'recreation/video_upload.html', locals())


class ArticleView(generic.ListView):
    template_name = 'recreation/article.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Article.objects.order_by('-publish_time')


class MyArticleView(generic.ListView):
    template_name = 'recreation/article.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Article.objects.filter(publisher=user_id).order_by('-publish_time')


def my_article_details(request, pk):
    context = {}

    obj = get_object_or_404(Article, id=pk)
    article_form = forms.ArticleForm(request.POST or None, instance=obj)

    if article_form.is_valid():
        article_form.save()
        return redirect('recreation:myarticle')

    context["article_form"] = article_form
    return render(request, "recreation/article_change.html", context)


def my_article_delete(request, pk):
    context = {}
    obj = get_object_or_404(Article, id=pk)
    obj.delete()

    return redirect('recreation:myarticle')


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'recreation/article_details.html'




class VideoView(generic.ListView):
    template_name = 'recreation/video.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Video.objects.order_by('-publish_time')


class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'recreation/video_details.html'


class MyVideo(generic.ListView):
    template_name = 'recreation/video.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Video.objects.filter(publisher=user_id).order_by('-publish_time')


def update_video(request, pk):
    context = {}

    obj = get_object_or_404(Video, id=pk)
    video_form = forms.VideoForm(request.POST or None, instance=obj)

    if video_form.is_valid():
        video_form.save()
        return redirect('recreation:my_video')

    context["video_form"] = video_form
    return render(request, "recreation/video_update.html", context)


def delete_video(request, pk):
    obj = get_object_or_404(Video, id=pk)
    obj.delete()

    return redirect('recreation:my_video')
