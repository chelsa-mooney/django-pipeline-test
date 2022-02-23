from django.http import HttpResponse

def status_check(request):
   return HttpResponse(status=200)