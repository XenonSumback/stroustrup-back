# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from serializers import UserSerializer, ProfileSerializer
from forms import RegistrationForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def logout_view(request):
    logout(request)
    content = {
        'redirect': unicode('/login'),
    }
    return Response(content)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def user_auth(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    content = {
        'user': unicode(username),  # `django.contrib.auth.User` instance.
    }
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return Response(content)
    return Response(content)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def registration(request):
    username = request.data.get('username', None)
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    confirm_password = request.POST.get('confirm_password', None)
    form = RegistrationForm(request.data)
    if form.is_valid():
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        content = {
            'redirect': unicode('/login'),
        }
        return Response(content)
    return Response(form.errors.as_json())


@api_view(['GET'])
@permission_classes([])
@csrf_exempt
def whoami_view(request):
    print(request.user)
    if request.user.id is None:
        content = {
            'is_logged_in': False,
            'user': None,
        }
    else:
        user = User.objects.get(username=request.user)
        content = {
                'is_logged_in': True,
                'user': {
                    'username': user.username,
                    'id': user.pk,
                    'email': user.email,
                },
        }
        return Response(content)
    return Response(content)

