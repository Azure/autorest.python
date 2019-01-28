# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------



class Animal(Model):
    """The animal model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Animal name
    :vartype name: str
    :ivar age: Animal age
    :vartype age: str
    """

    _validation = {
        'name': {'required': True, 'readonly': True},
        'age': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'age': {'key': 'age', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Animal, self).__init__(**kwargs)
        self.name = None
        self.age = None


class Rock(Model):
    """The rock model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Rock name
    :vartype name: str
    :ivar rock_type: Type of rock
    :vartype rock_type: str
    """

    _validation = {
        'name': {'required': True, 'readonly': True},
        'rock_type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'rock_type': {'key': 'rockType', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Rock, self).__init__(**kwargs)
        self.name = None
        self.rock_type = None


class Cat(Animal):
    """Cat resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Animal name
    :vartype name: str
    :ivar age: Animal age
    :vartype age: str
    :ivar breed: Name of cat breed
    :vartype breed: str
    """

    _validation = {
        'name': {'required': True, 'readonly': True},
        'age': {'readonly': True},
        'breed': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'age': {'key': 'age', 'type': 'str'},
        'breed': {'key': 'breed', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Cat, self).__init__(**kwargs)
        self.breed = None


class Dog(Animal):
    """Dog resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Animal name
    :vartype name: str
    :ivar age: Animal age
    :vartype age: str
    :ivar breed: Name of dog breed
    :vartype breed: str
    """

    _validation = {
        'name': {'required': True, 'readonly': True},
        'age': {'readonly': True},
        'breed': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'age': {'key': 'age', 'type': 'str'},
        'breed': {'key': 'breed', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Dog, self).__init__(**kwargs)
        self.breed = None


class Puppy(Dog):
    """Puppy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Animal name
    :vartype name: str
    :ivar age: Animal age
    :vartype age: str
    :ivar breed: Name of dog breed
    :vartype breed: str
    :ivar mother: Name of mother
    :vartype mother: str
    """

    _validation = {
        'name': {'required': True, 'readonly': True},
        'age': {'readonly': True},
        'breed': {'readonly': True},
        'mother': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'age': {'key': 'age', 'type': 'str'},
        'breed': {'key': 'breed', 'type': 'str'},
        'mother': {'key': 'mother', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Puppy, self).__init__(**kwargs)
        self.mother = None
