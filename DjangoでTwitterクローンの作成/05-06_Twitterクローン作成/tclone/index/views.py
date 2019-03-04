from django.shortcuts import render, redirect
from .forms import *
from .models import *

def index(request):
    id_list = NewTweet.objects.values_list('id', flat=True)
    tweet_list = NewTweet.objects.values_list('tweet', flat=True)
    tweets = zip(id_list, tweet_list)
    tweets = list(tweets)
    f = {
        'tweets': tweets
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
        new_tweet = new_tweet.as_table()
        f = {
            'new_tweet': new_tweet,
            }
        return render(request, 'index/new.html', f)

# deleteを追加
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