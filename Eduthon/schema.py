import graphene

import testApp.schema

class Query(testApp.schema.Query, graphene.ObjectType):
    pass