import graphene
from graphene import ObjectType, String, Boolean, ID, Field, Int, List, Mutation

class Student(ObjectType):
    id = ID()
    name = String()

# List view of <any> objects
class Query(ObjectType):
    students = List(Student, id=Int(required=False))
    student = graphene.Field(Student)

    def resolve_students(self, context, **kwargs):
        students = [ { "name": "fix" }, { "name": "me" }]
        return students

class CreateStudent(Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    student = graphene.Field(lambda: Student)

    def mutate(root, info, name):
        student = Student(name=name)
        ok = True
        return CreateStudent(student=student, ok=ok)


class MyMutations(graphene.ObjectType):
    create_student = CreateStudent.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)

def test():
    query = '''
        query students {
            name
        }
    '''
    result = schema.execute(query)
    print(f"result={result}")
