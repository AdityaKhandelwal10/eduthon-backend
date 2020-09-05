from graphene_django import DjangoObjectType
import graphene

from .models import GroupTasks, TeamModel
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField 
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import TeamForm, GroupTasksForm

#queries here

class TeamPortfolio(DjangoObjectType):
    class Meta:
        model = TeamModel
        filter_fields = ['members', 'name']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    teams = relay.Node.Field(TeamPortfolio)
    all_teams = DjangoFilterConnectionField(TeamPortfolio)


#mutations

class TeamModelType(DjangoObjectType):
    class Meta:
        model = TeamModel


class IndvTaskMutation(DjangoModelFormMutation):
    ent = Field(TeamPortfolio)

    class Meta:
        form_class = TeamForm

class Mutation(graphene.ObjectType):
    createTeam = IndvTaskMutation.Field()