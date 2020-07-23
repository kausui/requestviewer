from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404

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

        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        pass


class PageNotFoundView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        raise Http404

