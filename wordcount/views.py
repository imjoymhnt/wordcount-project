from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

textdict = {}

def count(request):
    text = request.GET['fulltext']
    wordNo = text.split()
    for word in wordNo:
        if word in textdict:
            textdict[word] +=1
        else:
            textdict[word] = 1

    sortedtext = sorted(textdict.items(), key = operator.itemgetter(1), reverse=True)

    
    return render(request, 'count.html', {'text':text, 'wordNo': len(wordNo), 'sortedtext':sortedtext})
    

def about(request):
    return render(request, 'about.html')