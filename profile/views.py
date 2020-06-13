from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def profile(request):  # TODO split
    '''Page with statistic for the user and links to content generators'''
    if request.method == 'POST':
        # Как удалять ненужные аватарки?
        form = forms.AvatarsForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            # Попробуй вызывать account с request.method = 'GET'
        return render(request, 'profile/profile.html', {'form': form})
    else:
        form = forms.AvatarsForm()
    return render(
        request,
        'profile/profile.html',
        {'form': form, 'avatar': request.user.profile.avatar}
    )
