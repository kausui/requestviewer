from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import Http404
from django.conf import settings
import base64
import time
COOKIE_KEY = 'REQUEST_VIEWER_COOKIE'
COOKIE_VALUE = 'cookie-12345'
COOKIE_AGE_SECOND = 1800
BASIC_AUTH_PATH = 'basicauth/'
# Create your views here.
class IndexView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        context = self.prepare_context(request)
        status_code = 200

        # Basic authentication
        if BASIC_AUTH_PATH in request.path:
            if 'HTTP_AUTHORIZATION' in request.META:
                print("Basic auth start.")
                authentication = request.META['HTTP_AUTHORIZATION']
                (authmeth, auth) = authentication.split(' ', 1)
                if 'basic' != authmeth.lower():
                    return self.unauthed()
                print(auth.strip())
                auth = base64.b64decode(auth.strip()).decode()
                print(auth)
                username, password = auth.split(':', 1)
                if username == settings.BASICAUTH_USERNAME and password == settings.BASICAUTH_PASSWORD:
                    print("Basic auth OK.")
                    pass
                else:
                    print("Basic auth FAIL.")
                    return HttpResponse('Unauthorized', status=401)
            else:
                return self.unauthed()

        self.sleep(request)

        if "status" in request.GET:
            print("Status Code option")
            status_val_str = request.GET.get("status")
            if status_val_str.isdigit():
                status_value = int(status_val_str)
                if status_value > 0:
                    print("Status code: ", status_value)
                    status_code = status_value

        # websocket(todo)
        response = render(request, 'index.html', context, status=status_code)

        if "no-content-type" in request.GET:
            print("No content-type option")
            del response["Content-Type"]
        # Set cookie
        try:
            cookie_value = request.COOKIES[COOKIE_KEY]
            print("Cookie: ", cookie_value)
        except KeyError:
            response.set_cookie(COOKIE_KEY, COOKIE_VALUE, COOKIE_AGE_SECOND)

        return response

    def post(self, request, *args, **kwargs):
        context = self.prepare_context(request)
        self.sleep(request)
        self.post_sleep(request)
        status_code = 200
        status_code = self.post_status(request)
        context['post'] = request.POST

        return render(request, 'index.html', context, status=status_code)

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

    def post_status(self, request):
        if "status" in request.POST:
            print("POST Status option")
            status_val_str = request.POST.get("status")
            if status_val_str.isdigit():
                status_value = int(status_val_str)
                if status_value > 0:
                    print("Status Code: ", status_value)
                    return status_value

    def unauthed(self):
        response = HttpResponse("<html><title>Auth required</title><body><h1>Authorization Required</h1></body></html>", content_type="text/html")
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        response.status_code = 401
        return response

class PageNotFoundView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        raise Http404
