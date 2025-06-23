from django import forms
from .models import Donation, Comment

class DonationForm(forms.ModelForm):
    stripe_token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'stripe_token']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
