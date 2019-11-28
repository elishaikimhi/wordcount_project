from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html') 


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_count = {}
    for word in wordlist:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    context = {'fulltext': fulltext, 'sorted_words': sorted_words}
    return render(request, 'count.html', context)

def about(request):
    return render(request,'about.html')

