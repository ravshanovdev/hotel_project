import faker
from factory.django import DjangoModelFactory
from accounts.models import CustomUser, UserSession
import factory


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    phone = factory.Sequence(lambda x: f"+998901234{str(x).zfill(3)}")
    first_name = faker.Faker().first_name()
    last_name = faker.Faker().last_name()
    user_type = CustomUser.UserType.USER
    status = CustomUser.Status.PENDING
    inn = faker.Faker().bothify(text='##########')
    stir = faker.Faker().bothify(text='##########')
    legal_address = faker.Faker().address()
    is_active = False
    is_staff = False


class UserSessionFactory(DjangoModelFactory):
    class Meta:
        model = UserSession

    user = factory.SubFactory(CustomUserFactory)
    device_id = factory.Sequence(lambda x: f"{x}")
    jti = factory.Sequence(lambda x: f"{x}")



