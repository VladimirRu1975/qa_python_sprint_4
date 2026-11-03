import pytest


# ==========================================
# КЛАСС 1: Тесты добавления книг
# ==========================================
class TestBooksCollectorAddBook:

    def test_add_new_book_adds_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre

    @pytest.mark.parametrize("name", [
        '',                                # пустое название
        'Очень длинное название книги, которое точно превышает 40 символов'  # > 40
    ])
    def test_add_new_book_does_not_add_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_does_not_add_duplicate(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')
        assert len(collector.books_genre) == 1


# ==========================================
# КЛАСС 2: Тесты жанров
# ==========================================
class TestBooksCollectorGenre:

    def test_set_book_genre_sets_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.books_genre['Гарри Поттер'] == 'Фантастика'

    def test_set_book_genre_does_not_set_invalid_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Несуществующий жанр')
        assert collector.books_genre['Гарри Поттер'] == ''

    def test_get_book_genre_returns_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_returns_none_for_unknown_book(self, collector):
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
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

    def test_get_books_genre_returns_dictionary(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастика'}

    def test_get_books_for_children_returns_only_safe_books(self, collector):
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
# КЛАСС 3: Тесты избранного
# ==========================================
class TestBooksCollectorFavorites:

    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.favorites

    def test_add_book_in_favorites_does_not_add_duplicate(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.favorites

    def test_delete_book_from_favorites_does_nothing_if_not_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.favorites

    def test_get_list_of_favorites_books_returns_list(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']
        