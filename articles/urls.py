from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/<slug:slug>/',
         views.ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>/<slug:slug>/',
         views.ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/<slug:slug>/',
         views.ArticleDeleteView.as_view(), name='article_delete'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('comment/<int:pk>/<slug:slug>/', views.create_comment,
         name='create_comment')
]


