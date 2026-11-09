# BooksCollector - Юнит-тесты

Проект содержит набор юнит-тестов для класса `BooksCollector`, который управляет коллекцией книг, их жанрами и избранным.

## Реализованные тесты

### Метод `add_new_book`

- `test_add_new_book_adds_book` — проверяет успешное добавление книги.
- `test_add_new_book_does_not_add_invalid_name` (параметризованный) — проверяет, что пустые названия и названия длиннее 40 символов не добавляются.
- `test_add_new_book_does_not_add_duplicate` — проверяет, что дубликаты не добавляются.

### Метод `set_book_genre`

- `test_set_book_genre_sets_genre` — проверяет установку валидного жанра.
- `test_set_book_genre_does_not_set_invalid_genre` — проверяет, что невалидный жанр не устанавливается.

### Метод `get_book_genre`

- `test_get_book_genre_returns_genre` — проверяет возврат жанра для существующей книги.
- `test_get_book_genre_returns_none_for_unknown_book` — проверяет возврат `None` для неизвестной книги.

### Метод `get_books_with_specific_genre`

- `test_get_books_with_specific_genre_returns_correct_books` — проверяет фильтрацию книг по жанру.

### Метод `get_books_genre`

- `test_get_books_genre_returns_dictionary` — проверяет возврат словаря книг с жанрами.

### Метод `get_books_for_children`

- `test_get_books_for_children_returns_only_safe_books` — проверяет, что возвращаются только книги без возрастного рейтинга.

### Методы `add_book_in_favorites`, `delete_book_from_favorites`, `get_list_of_favorites_books`

- `test_add_book_in_favorites_adds_book` — проверяет добавление в избранное.
- `test_add_book_in_favorites_does_not_add_duplicate` — проверяет, что дубликаты не добавляются.
- `test_delete_book_from_favorites_removes_book` — проверяет удаление из избранного.
- `test_delete_book_from_favorites_does_nothing_if_not_in_favorites` — проверяет, что удаление несуществующей книги не вызывает ошибок.
- `test_get_list_of_favorites_books_returns_list` — проверяет возврат списка избранных книг.

## Запуск тестов

```bash
pytest -v tests.py
