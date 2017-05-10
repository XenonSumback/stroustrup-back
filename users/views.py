from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, response
from rest_framework.response import Response

from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@csrf_exempt
def userAuth(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("{'redirect':'http://google.ru'}")
            # Redirect to a success page.
        else:
            return HttpResponse("errors disabled account")
    # Return a 'disabled account' error message
    else:
        return HttpResponse("errors invalid data")

# Return an 'invalid login' error message.



