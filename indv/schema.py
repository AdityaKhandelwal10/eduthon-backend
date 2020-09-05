from graphene_django import DjangoObjectType
import graphene

from .models import IndvTask, ProgressModel
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField 
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import  IndvTaskForm,ProgressForm, UpdateProgressForm

#queries here
class IndvTaskModel(DjangoObjectType):
    class Meta:
        model = IndvTask
        filter_fields = ['user','task', 'desc', 'prog']
        interfaces = (relay.Node,)


class ProgressModelObject(DjangoObjectType):
    class Meta:
        model = ProgressModel
        filter_fields = ['user','task', 'progress']
        interfaces = (relay.Node,)



class Query(graphene.ObjectType):
    indvtasks = relay.Node.Field(IndvTaskModel)
    all_indvtasks = DjangoFilterConnectionField(IndvTaskModel)

    progress = relay.Node.Field(ProgressModelObject)
    all_progressModel = DjangoFilterConnectionField(ProgressModelObject)

#Mutations here :
class IndvTaskType(DjangoObjectType):
    class Meta:
        model = IndvTask


class IndvTaskMutation(DjangoModelFormMutation):
    ent = Field(IndvTaskType)

    class Meta:
        form_class = IndvTaskForm


class ProgressModelType(DjangoObjectType):
    class Meta:
        model = ProgressModel


class ProgressModelMutation(DjangoModelFormMutation):
    ent = Field(ProgressModelType)

    class Meta:
        form_class = ProgressForm

class UpdateProgressModelType(DjangoObjectType):
    class Meta:
        model = ProgressModel

        
class updateProgress(DjangoModelFormMutation):
    ent = Field(UpdateProgressModelType)

    class Meta:
        form_class = UpdateProgressForm


class Mutation(graphene.ObjectType):
    createIndvTask = IndvTaskMutation.Field()
    addProgress = ProgressModelMutation.Field()
    updateProgress = updateProgress.Field()