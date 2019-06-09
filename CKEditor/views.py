from django.http import HttpResponse
from django.conf import settings
import os
import time
import random
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt)
def upload(request):
    file = request.FILES.get("upload")
    name = file.name
    r = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 6)
    ss = ""
    for i in r:
        ss += i
    name = ss + time.strftime('_%Y%m%d%H%M%S', time.localtime()) + os.path.splitext(name)[1]
    with open(os.path.join(settings.CKEDITOR_UPLOAD_PATH, "A" + name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    url = request.build_absolute_uri(settings.CKEDITOR_UPLOAD_URL + "A" + name)
    s = "{\"uploaded\": true,\"url\": \"" + url + "\"}"
    return HttpResponse(s)
