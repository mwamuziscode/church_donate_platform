from django.urls import path
from .views import BlogListView, DonationView, LikeView, CommentCreateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('donate/', DonationView.as_view(), name='donate'),
    path('like/<int:pk>/', LikeView.as_view(), name='like'),
    path('comment/<int:blog_id>/', CommentCreateView.as_view(), name='comment'),
]




urlpatterns += [
    path('home', views.HomeView.as_view(), name='home'),
    path('teachings/', views.BibleTeachingsView.as_view(), name='teachings'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('about/', views.AboutUsView.as_view(), name='about'),
]

