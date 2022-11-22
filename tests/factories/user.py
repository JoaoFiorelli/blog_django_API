from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    name = 'User Teste'
    email = 'teste_user@gmail.com'
    password = '123456'

    class Meta:
        model = 'user.UserProfile'
