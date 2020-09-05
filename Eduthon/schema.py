import graphene

import testApp.schema
import indv.schema
import group.schema

class Query(testApp.schema.Query, indv.schema.Query, group.schema.Query ,graphene.ObjectType):
    pass

class Mutation(indv.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation)