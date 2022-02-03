from django.http.response import HttpResponseRedirect
import string, random
from django.shortcuts import render
from .models import *
from .forms import *

def make_new_url():
    return str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)))

def create_short_url(request):
    url_form = UrlForm()
    context = {"form":url_form, "new_url":""}

    if request.method == 'POST':
        url_form = UrlForm(request.POST)

        if url_form.is_valid():
            origial_website = url_form.cleaned_data['original_url']
            new_url = make_new_url() # With random and string i made the short url 

            while(len(Url.objects.filter(short_url=new_url)) != 0):
                new_url = make_new_url()

            final_url = Url(original_url=origial_website, short_url=new_url, click_time = 0) # Create new Url model
            final_url.save()

            url_form = UrlForm() # After provide short url the form be empty for the next try.
            context = {"form":url_form, "new_url":final_url.short_url}

    return render(request, "ShortUrl/main.html",context)


def redirect_to_original_url(request, url):

    try:
        url_obj = Url.objects.get(short_url=url)
    except Url.DoesNotExist: # Ready for exepsion if the url we get does not exist in our short url.
        url_obj = None

    if url_obj == None:
        return render(request, 'ShortUrl/pagenotfound.html',{"message":"For that url there is no way home"})
    
    url_obj.click_time += 1 # Hit counter for each use 
    url_obj.save()
    return HttpResponseRedirect(url_obj.original_url) # Redirect to the original url 