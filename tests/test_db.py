from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='bento', email='teste@teste.com', password='1234')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'bento'))

    assert user.username == 'bento'
