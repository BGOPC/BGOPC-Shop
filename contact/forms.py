from django import forms


class ContactForm(forms.Form):
    title = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=300)
    name = forms.CharField(max_length=300)
    message = forms.CharField(widget=forms.Textarea)
