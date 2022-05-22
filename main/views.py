from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404
import time
# Create your views here.
class IndexView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        context = self.prepare_context(request)

        # basic authentication(todo)
        # if "auth" in request.GET:

        self.sleep(request)

        # websocket(todo)
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        context = self.prepare_context(request)
        self.sleep(request)
        self.post_sleep(request)
        context['post'] = request.POST

        return render(request, 'index.html', context)

    def prepare_context(self, request):
        context = dict()
        context['clientip'] = request.META['REMOTE_ADDR']
        context['serverport'] = request.META['SERVER_PORT']
        context['path'] = request.path
        context['method'] = request.method
        context['headers'] = dict(request.headers)
        print(context['headers'])

        return context

    def sleep(self, request):
        if "sleep" in request.GET:
            print("Sleep option")
            sleep_val_str = request.GET.get("sleep")
            if sleep_val_str.isdigit():
                sleep_value = int(sleep_val_str)
                if sleep_value > 0:
                    print("Sleep ", sleep_value, "seconds")
                    time.sleep(sleep_value)

    def post_sleep(self, request):
        if "sleep" in request.POST:
            print("POST Sleep option")
            sleep_val_str = request.POST.get("sleep")
            if sleep_val_str.isdigit():
                sleep_value = int(sleep_val_str)
                if sleep_value > 0:
                    print("Sleep ", sleep_value, "seconds")
                    time.sleep(sleep_value)

class PageNotFoundView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        raise Http404

