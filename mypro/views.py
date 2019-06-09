from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def show(request):
    context = {}
    content = request.POST.get('content')
    context['content'] = content
    return render(request, 'show.html', context)


def UEditor(request):
    return render(request, 'UEditor/UEditor.html')


def wangEditor(request):
    return render(request, 'wangEditor/wangEditor.html')


def CKEditor(request):
    return render(request, 'CKEditor/CKEditor.html')
