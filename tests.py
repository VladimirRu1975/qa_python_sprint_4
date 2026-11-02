import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Фикстура создаёт новый объект для каждого теста."""
    return BooksCollector()


# ==========================================
# Тесты для метода add_new_book
# ==========================================

def test_add_new_book_adds_book(collector):
    collector.add_new_book('Гарри Поттер')
    assert 'Гарри Поттер' in collector.books_genre


@pytest.mark.parametrize("name", [
    '',                                # пустое название
    'Очень длинное название книги, которое точно превышает 40 символов'  # > 40
])
def test_add_new_book_does_not_add_invalid_name(collector, name):
    collector.add_new_book(name)
    assert name not in collector.books_genre


def test_add_new_book_does_not_add_duplicate(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')
    assert len(collector.books_genre) == 1


# ==========================================
# Тесты для метода set_book_genre
# ==========================================

def test_set_book_genre_sets_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert collector.books_genre['Гарри Поттер'] == 'Фантастика'


def test_set_book_genre_does_not_set_invalid_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Несуществующий жанр')
    assert collector.books_genre['Гарри Поттер'] == ''


# ==========================================
# Тесты для метода get_book_genre
# ==========================================

def test_get_book_genre_returns_genre(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


def test_get_book_genre_returns_none_for_unknown_book(collector):
    assert collector.get_book_genre('Неизвестная книга') is None


# ==========================================
# Тесты для метода get_books_with_specific_genre
# ==========================================

def test_get_books_with_specific_genre_returns_correct_books(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.add_new_book('Властелин колец')
    collector.set_book_genre('Властелин колец', 'Фантастика')
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')

    books = collector.get_books_with_specific_genre('Фантастика')
    assert len(books) == 2
    assert 'Гарри Поттер' in books
    assert 'Властелин колец' in books


# ==========================================
# Тесты для метода get_books_genre
# ==========================================

def test_get_books_genre_returns_dictionary(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастика'}


# ==========================================
# Тесты для метода get_books_for_children
# ==========================================

def test_get_books_for_children_returns_only_safe_books(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')  # Есть возрастной рейтинг
    collector.add_new_book('Том и Джерри')
    collector.set_book_genre('Том и Джерри', 'Мультфильмы')

    books = collector.get_books_for_children()
    assert 'Гарри Поттер' in books
    assert 'Том и Джерри' in books
    assert 'Шерлок Холмс' not in books


# ==========================================
# Тесты для методов работы с избранным
# ==========================================

def test_add_book_in_favorites_adds_book(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert 'Гарри Поттер' in collector.favorites


def test_add_book_in_favorites_does_not_add_duplicate(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert len(collector.favorites) == 1


def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.delete_book_from_favorites('Гарри Поттер')
    assert 'Гарри Поттер' not in collector.favorites


def test_delete_book_from_favorites_does_nothing_if_not_in_favorites(collector):
    collector.add_new_book('Гарри Поттер')
    collector.delete_book_from_favorites('Гарри Поттер')
    assert 'Гарри Поттер' not in collector.favorites


def test_get_list_of_favorites_books_returns_list(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert collector.get_list_of_favorites_books() == ['Гарри Поттер']