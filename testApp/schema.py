from graphene_django import DjangoObjectType
import graphene

from .models import User
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField 
from graphene import Field

class UserModel(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username','email','jwt']
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    users = relay.Node.Field(UserModel)
    all_users = DjangoFilterConnectionField(UserModel)

    