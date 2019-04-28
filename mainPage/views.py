from django.shortcuts import render


def mainPage(request):
    '''Main page with top bloggers and top articles'''
    print(request.META['REMOTE_ADDR'])
    return render(request, 'mainPage\main.html', {})
