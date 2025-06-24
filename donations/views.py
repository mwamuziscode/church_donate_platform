from django.views.generic import ListView, FormView, View
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Blog, Like, Comment
from .forms import DonationForm, CommentForm
#import stripe = 1

#stripe = 1
#stripe.api_key = 'your_stripe_secret_key'

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
    




# ---------------------------------------------


from django.http import HttpResponse
from django.views import View

BUTTON = '<p><a href="/" style="text-decoration:none;padding:8px 12px;background:#0077aa;color:white;border-radius:5px;">Go Home</a></p>'

class HomeView(View):
    def get(self, request):
        return HttpResponse("<h2>Welcome to the Home Page!</h2>" + BUTTON)

class BibleTeachingsView(View):
    def get(self, request):
        return HttpResponse("<h2>Welcome to Bible Teachings</h2>" + BUTTON)

class LibraryView(View):
    def get(self, request):
        return HttpResponse("<h2>Welcome to the Library</h2>" + BUTTON)

class NewsView(View):
    def get(self, request):
        return HttpResponse("<h2>Latest News and Updates</h2>" + BUTTON)

class AboutUsView(View):
    def get(self, request):
        return HttpResponse("<h2>About Us</h2>" + BUTTON)

