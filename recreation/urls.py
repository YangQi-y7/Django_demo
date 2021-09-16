from django.urls import path
from . import views

app_name = 'recreation'
urlpatterns = [
    path('article/', views.ArticleView.as_view(), name="article"),
    path('myarticle/', views.MyArticleView.as_view(), name="myarticle"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view()),
    path('myarticle/<int:pk>/', views.my_article_details, name="update_article"),
    path('myarticle/<int:pk>/delete/', views.my_article_delete, name="delete_article"),

    path('video/', views.VideoView.as_view(), name="video"),
    path('video/<int:pk>/', views.VideoDetailView.as_view()),
    path('my_video/', views.MyVideo.as_view(), name="my_video"),
    path('my_video/<int:pk>/', views.update_video, name="update_video"),
    path('my_video/<int:pk>/delete/', views.delete_video, name="delete_video"),

    path('upload_article/', views.upload_article, name="upload_article"),
    path('upload_video/', views.upload_video, name="upload_video"),
    # path('upload_image', views.upload_image, name="upload_image"),
]
