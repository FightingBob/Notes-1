from orm import IntegerField, Model, StringField


class User(Model):
    requestd = IntegerField()
    name = StringField()


if __name__ == "__main__":
    user = User(id=1, name='name')
    print(user)
    print(user.name)
    print(user.id)
