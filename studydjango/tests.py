from django.test import TestCase

# Create your tests here.
def application(env,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return [b"hello world"]


