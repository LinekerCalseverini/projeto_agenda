from django.shortcuts import render


def create(request):
    if request.method == 'POST':
        request.POST.get('first_name')
        request.POST.get('last_name')

    context = {}

    return render(
        request,
        'contact/create.html',
        context
    )
