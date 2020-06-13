from django.shortcuts import render


def main_page(request):
    '''Main page with top bloggers and top articles'''
    return render(request, 'main_page/main.html', {})
