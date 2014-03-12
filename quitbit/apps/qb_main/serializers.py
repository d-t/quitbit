from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from apps.qb_main.models import Cigarette, Comment

User = get_user_model()

# An HyperlinkedModelSerializer does not include the pk field by default.
# It includes a url field, using HyperlinkedIdentityField.
# Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # When we need to access "reserve" foreign key relations (my_related_model is the related_name)
    # my_related_model = serializers.PrimaryKeyRelatedField(many=True)
    # cigarettes = serializers.HyperlinkedRelatedField(many=True, view_name='user_cigarettes')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', )


class CigaretteSerializer(serializers.HyperlinkedModelSerializer):

    # user = serializers.Field(source='user.username')


    class Meta:
        model = Cigarette
        fields = ('url', 'user', 'cigarette_date', 'cigarette_time', )


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('url', 'user', 'content', 'parent_comment', )