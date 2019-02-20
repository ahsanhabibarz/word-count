from django.shortcuts import render

def home(request):
    return render (request, 'home.html')


def count(request):

    fulltext = request.GET['fulltext']

    wordcount = fulltext.split();

    worddic = {}

    for word in wordcount:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1

    return render (request, 'count.html',{'text':fulltext,'wordcount':len(wordcount),'worddic':worddic.items})
