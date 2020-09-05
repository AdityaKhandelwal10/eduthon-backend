from graphene_django import DjangoObjectType
import graphene

from .models import IndvTask
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField 
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import  IndvTaskForm

#queries here
class IndvTaskModel(DjangoObjectType):
    class Meta:
        model = IndvTask
        filter_fields = ['user','task', 'desc', 'prog']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    indvtasks = relay.Node.Field(IndvTaskModel)
    all_indvtasks = DjangoFilterConnectionField(IndvTaskModel)



#Mutations here :
class IndvTaskType(DjangoObjectType):
    class Meta:
        model = IndvTask


class IndvTaskMutation(DjangoModelFormMutation):
    ent = Field(IndvTaskType)

    class Meta:
        form_class = IndvTaskForm

class Mutation(graphene.ObjectType):
    createIndvTask = IndvTaskMutation.Field()