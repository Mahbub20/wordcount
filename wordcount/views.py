
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['fulltextarea']
    wordlist = data.split()
    list_length = len(wordlist)
    wordDictionary = {}
    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sorted_list = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': data, 'words': list_length, 'wordDictionary': sorted_list})

def about(request):
    return  render(request, 'about.html')