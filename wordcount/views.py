from django.shortcuts import render
import operator
import regex as re


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    countdict = {}
    for word in wordlist:
        if word in countdict:
            countdict[word] += 1
        else:
            countdict[word] = 1
    sorteddict = sorted(countdict.items(),
                        key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'wordlist': len(wordlist), 'countdict': sorteddict})


def about(request):
    return render(request, 'about.html')
