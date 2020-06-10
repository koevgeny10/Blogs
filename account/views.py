from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def account(request):
    '''Page with statistic for the user and links to content generators'''
    if request.method == 'POST':
        # Как удалять ненужные аватарки?
        instance = models.Profile.objects.get(username=request.user.username)
        form = forms.AvatarsForm(
            request.POST,
            request.FILES,
            instance=instance
        )
        if form.is_valid():
            form.save()
            # Попробуй вызывать account с request.method = 'GET'
        return render(request, 'account/account.html', {'form': form})
    else:
        form = forms.AvatarsForm()
        avatar = models.Profile.objects.get(
            username=request.user.username
        ).picture
    return render(
        request,
        'account/account.html',
        {'form': form, 'avatar': avatar}
    )
