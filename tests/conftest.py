import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import User, table_registry
from fast_zero.security import get_password_hash
from fast_zero.settings import Settings


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'teste{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@teste.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}321')


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def session():
    engine = create_engine(Settings().DATABASE_URL)
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        session.rollback()

    table_registry.metadata.drop_all(engine)


@pytest.fixture()
def token(client, user):
    response = client.post(
        'auth/token/',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']


@pytest.fixture()
def user(session):
    password = '1234'
    hash_pass = get_password_hash(password)
    user = User(username='Teste', email='teste@teste.com', password=hash_pass)
    # user = UserFactory(password=hash_pass)
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password
    return user


@pytest.fixture()
def user2(session):
    password = '333'
    hash_pass = get_password_hash(password)
    user = User(
        username='Teste2', email='teste2@teste.com', password=hash_pass
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password
    return user


@pytest.fixture()
def other_user(session):
    password = '1234'
    hash_pass = get_password_hash(password)
    # user = User(username='Teste',
    # email='teste@teste.com', password=hash_pass)
    user = UserFactory(password=hash_pass)
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password
    return user
