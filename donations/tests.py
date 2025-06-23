from django.test import TestCase
from .models import Blog, Comment, Like

class BlogTests(TestCase):
    def test_create_update(self):
        blog = Blog.objects.create(title="Test", content="Test content")
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(blog.title, "Test")



class CommentTests(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(title="Test", content="Test content")

    def test_create_comment(self):
        comment = Comment.objects.create(update=self.blog, name="User", comment="Test comment")
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.update, self.blog)
        self.assertEqual(comment.name, "User")
        self.assertEqual(comment.comment, "Test comment")



class LikeTests(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(title="Test", content="Test content")

    def test_create_like(self):
        like = Like.objects.create(update=self.blog, ip_address="127.0.0.1")
        self.assertEqual(Like.objects.count(), 1)

