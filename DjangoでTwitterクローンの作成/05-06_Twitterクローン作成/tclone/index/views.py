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


def delete(request, tweet_id):
    NewTweet.objects.filter(id=tweet_id).delete()
    return redirect('/')


def update(request, tweet_id):
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
        new_tweet = new_tweet.cleaned_data['tweet']
        old_tweet = NewTweet.objects.get(id=tweet_id)
        old_tweet.tweet = new_tweet
        old_tweet.save()
        return redirect('/')
    else:
        new_tweet = new_tweet.as_table()
        f = {
            'new_tweet': new_tweet,
            }
        return render(request, 'index/update.html', f)

