import graphene
import graphAPI.schema


class Query(graphAPI.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphAPI.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
