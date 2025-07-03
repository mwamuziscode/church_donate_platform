from django.contrib import admin
from donations.models import Blog, Donation, Comment, Like, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    #search_fields = ('name', 'descriptions')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email')

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('update', 'name', 'created_at')
    search_fields = ('name', 'comment')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('update', 'ip_address', 'created_at')
    search_fields = ('ip_address',)
