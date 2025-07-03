from django.views.generic import ListView, FormView, View
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Blog, HeadLine, Like, Comment, Topic
from .forms import DonationForm, CommentForm
import stripe 
stripe.api_key = 'your_stripe_secret_key'



class BlogListView(ListView):
    model = Blog
    template_name = 'donations/home.html'
    context_object_name = 'blogs'

class DonationView(FormView):
    template_name = 'donations/donate.html'
    form_class = DonationForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        charge = stripe.Charge.create(
            amount=int(data['amount'] * 100),
            currency='usd',
            description='Church Donation',
            source=data['stripe_token']
        )
        donation = form.save(commit=False)
        donation.stripe_charge_id = charge.id
        donation.save()

        send_mail(
            "Donation Receipt",
            f"Thank you for donating ${donation.amount}",
            'your-email@example.com',
            [donation.email],
        )
        return super().form_valid(form)

class LikeView(View):
    def get(self, request, pk):
        update = get_object_or_404(Blog, pk=pk)
        Like.objects.create(
            update=update, 
            ip_address=request.META['REMOTE_ADDR'])
        return redirect('home')




class CommentCreateView(FormView):
    form_class = CommentForm

    def form_valid(self, form):
        blog_id = self.kwargs['blog_id']
        comment = form.save(commit=False)
        comment.blog_id = blog_id
        comment.save()
        return redirect('home')
    

from django.views.generic import TemplateView

BUTTON_HTML = '<p><a href="/" style="text-decoration:none;padding:8px 12px;background:#0077aa;color:white;border-radius:5px;">Go Home</a></p>'


# MultiModelView to display multiple models on the same page
class MultiModelView(TemplateView):
    template_name = 'donations/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # first first newest 5 blogs
        context['blogs'] = Blog.objects.all().order_by('-created_at')[:4]
        context['topics'] = Topic.objects.all().order_by('-created_at')[:8]
        context['headlines'] = HeadLine.objects.all().order_by('-created_at')[:5]
        return context



class BibleTeachingsView(TemplateView):
    template_name = "donations/bible_teachings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "<h2>Welcome to Bible Teachings</h2>" + BUTTON_HTML
        return context

class LibraryView(TemplateView):
    template_name = "donations/photo_library.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "<h2>Welcome to the Library</h2>" + BUTTON_HTML
        return context

class NewsView(TemplateView):
    template_name = "donations/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "<h2>Latest News and Updates</h2>" + BUTTON_HTML
        return context

class AboutUsView(TemplateView):
    template_name = "donations/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "<h2>About Us</h2>" + BUTTON_HTML
        return context


