from django.shortcuts import render


def mainPage(request):
    '''Main page with top bloggers and top articles
    Make it with List View!'''
    return render(request, 'mainPage\main.html',
                  {'login': request.user.is_authenticated})
