from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection


class ContactFrom(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your E-mail Address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


def contact(request):
    submitted = False
    print(request.method)
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #------- Showing Email in Console, Change this for production use Later ! --------#
            con = get_connection(
                'django.core.mail.backends.console.EmailBackend')
            #------- What is the content of the Mail? --------#
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['siteowner@arbisoft.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactFrom()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'eventapp/contact.html', {'form': form, 'submitted': submitted})


def about_us(request):
    return render(request, 'eventapp/about.html', {'page_title': "About Us"})
