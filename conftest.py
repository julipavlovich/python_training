import pytest
from fixture.application import Application


# задали глобальную переменную
fixture = None


@pytest.fixture
def app(request):
    # объявили глобальную переменную
    global fixture
    if fixture is None:
        # инициализация созд-я фикстуры
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    # указ-е на то, как рaзрушить фикстуру
    request.addfinalizer(fin)
    return fixture
