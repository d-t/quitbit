from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from serializers import UserSerializer, CigaretteSerializer, CommentSerializer
from models import Cigarette, Comment

User = get_user_model()


# API - VIEWS
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAdminUser,)
    # authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100

    def pre_save(self, obj):
        obj.user = self.request.user

    # @action()
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)


class CigaretteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cigarettes to be viewed or edited.
    """
    queryset = Cigarette.objects.all()
    serializer_class = CigaretteSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    # permission_classes = (permissions.IsAdminUser,)
    # authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100

    def pre_save(self, obj):
        obj.user = self.request.user

    # owner = serializers.Field(source='owner.username')
    # def pre_save(self, obj):
    #     obj.owner = self.request.user


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    paginate_by = 100