from django.urls import path
from .views import BlogListView, DonationView, LikeView, CommentCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('donate/', DonationView.as_view(), name='donate'),
    path('like/<int:pk>/', LikeView.as_view(), name='like'),
    path('comment/<int:update_id>/', CommentCreateView.as_view(), name='comment'),
]
