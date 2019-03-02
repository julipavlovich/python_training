import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    # инициализация созд-я фикстуры
    fixture = Application()
    # указ-е на то, как рвзрушить фикстуру
    request.addfinalizer(fixture.destroy)
    return fixture
