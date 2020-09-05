import graphene

import testApp.schema
import indv.schema

class Query(testApp.schema.Query, indv.schema.Query, graphene.ObjectType):
    pass

class Mutation(indv.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation)