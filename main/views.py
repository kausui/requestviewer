from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404
import time
# Create your views here.
class IndexView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        print(request.META['REMOTE_ADDR'])
        print(request.META['SERVER_PORT'])
        print(request.method)
        print(request.path)
        print(request.headers)

        context = dict()
        context['clientip'] = request.META['REMOTE_ADDR']
        context['serverport'] = request.META['SERVER_PORT']
        context['path'] = request.path
        context['method'] = request.method
        context['headers'] = dict(request.headers)
        print(context['headers'])

        # basic authentication
        # if "auth" in request.GET:

        # Sleep
        if "sleep" in request.GET:
            print("Sleep option")
            sleep_val_str = request.GET.get("sleep")
            if sleep_val_str.isdigit():
                sleep_value = int(sleep_val_str)
                if sleep_value > 0:
                    print("Sleep ", sleep_value, "seconds")
                    time.sleep(sleep_value)

        # websocket(todo)
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        print(request.META['REMOTE_ADDR'])
        print(request.META['SERVER_PORT'])
        print(request.method)
        print(request.path)
        print(request.headers)

        context = dict()
        context['clientip'] = request.META['REMOTE_ADDR']
        context['serverport'] = request.META['SERVER_PORT']
        context['path'] = request.path
        context['method'] = request.method
        context['headers'] = dict(request.headers)
        print(context['headers'])

        # Sleep
        if "sleep" in request.GET:
            print("Sleep option")
            sleep_val_str = request.GET.get('sleep')
            if sleep_val_str.isdigit():
                sleep_value = int(sleep_val_str)
                if sleep_value > 0:
                    print("Sleep ", sleep_value, "seconds")
                    time.sleep(sleep_value)

        return render(request, 'index.html', context)

class PageNotFoundView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        raise Http404

