"""
class User(Model):
    __tablename__ = 'u'
    id = IntegerField()
    name = StringField()
    email = StringField()

u = User(id=1, name='b', email=c)
source = u.save()
source = 'insert into user (id, name, email) values(1, 'b', 'c')'
"""


class Field(object):

    def __init__(self, column_type: str):
        self.column_type = column_type


class IntegerField(Field):

    def __init__(self):
        super(IntegerField, self).__init__('int')


class StringField(Field):

    def __init__(self):
        super(StringField, self).__init__('str')


class ModelMetaClass(type):

    def __new__(cls, name: str, bases: tuple, attrs: dict):
        """__new__

        :param name: class name
        :type name: str
        :param bases: bases class
        :type bases: tuple
        :param attrs: attributes
        :type attrs: dict
        """
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # get Use class
        mappings = dict()
        # save attributes in mappings
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__tablename__'] = mappings[
            '__tablename__'] if '__tablename__' in mappings.keys(
        ) else name.lower()
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        """__init__

        judge the key is in the user's class define
        :param **kwargs: dict initialize
        """
        for key in kwargs.keys():
            if key not in self.__mappings__.keys():
                raise AttributeError(
                    f"'{self.__tablename__}' Model not define {key}")
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key: str):
        """__getattr__

        :param key: class attribute
        :type key: str
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(
                f"'{self.__tablename__}' Model has no attribute {key}")

    def save(self):
        """save
        return sql statement
        """
        fields = []
        params = []
        for k, v in self.__mappings__.items():
            if isinstance(k, int):
                fields.append(k)
            else:
                fields.append("'" + k + "'")
            params.append(str(self[k]))
        sql = 'insert into {} ({}) values ({})'.format(
            self.__tablename__, ', '.join(fields), ', '.join(params))
        return sql
