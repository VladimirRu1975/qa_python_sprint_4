import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Фикстура создаёт новый объект для каждого теста."""
    return BooksCollector()
