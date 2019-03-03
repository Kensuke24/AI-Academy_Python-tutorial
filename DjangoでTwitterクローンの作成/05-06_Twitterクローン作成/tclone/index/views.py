from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    tweets = NewTweet .objects.values_list('tweet', flat=True)
    f = {
        'tweets': tweets,
    }
    return render(request, 'index/index.html', f)

def new(request):
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
        new_tweet = new_tweet.cleaned_data
        new_tweet = new_tweet['tweet']
        tweet = NewTweet(tweet=new_tweet)
        tweet.save()
        return redirect('/')
    else:
        new:tweet = new_tweet.as_table()
        f = {
            'new_tweet': new_tweet,
        }
    return render(request, 'index/new.html')


