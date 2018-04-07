from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere': 'this is me'})

def count(request):
    fulltext = request.GET['fulltext']
    worddictionary = {}
    wordlist = fulltext.split()
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedcount = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'count':len(wordlist), 'fulltext':fulltext, 'sortedcount':sortedcount})

def about(request):
    return render(request, 'about.html')
