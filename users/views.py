# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['POST'])
@csrf_exempt
def user_auth(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    }
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return Response(content)
            # Redirect to a success page.)
    # Return a 'disabled account' error message
    return Response(content)

# Return an 'invalid login' error message.


@api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
@authentication_classes([])
@permission_classes([])
def example_view(request):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)
