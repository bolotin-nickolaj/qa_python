from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_set_genre_for_book(self):
        collector = BooksCollector()
        collector.add_new_book('Жук в муравейнике')
        collector.set_book_genre('Жук в муравейнике', 'Фантастика')
        assert collector.get_book_genre('Жук в муравейнике') == 'Фантастика'

    def test_get_book_genre_get_genre_of_book(self):
        collector = BooksCollector()
        collector.add_new_book('Стажеры')
        collector.set_book_genre('Стажеры', 'Фантастика')
        assert collector.get_book_genre('Стажеры') == 'Фантастика'

    def test_get_books_with_specific_genre_get_books_by_genre(self):
        collector = BooksCollector()
        for i in 'Жук в муравейнике', 'Волны гасят ветер', 'Хромая судьба', 'Стажеры':
            collector.add_new_book(i)
            collector.set_book_genre(i,'Фантастика')
        collector.add_new_book('Мальтийский сокол')
        collector.set_book_genre('Мальтийский сокол', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Жук в муравейнике', 'Волны гасят ветер', 'Хромая судьба', 'Стажеры']

    def test_get_books_genre_get_list_of_books(self):
        collector = BooksCollector()
        for i in 'Хромая судьба', 'Стажеры':
            collector.add_new_book(i)
            collector.set_book_genre(i,'Фантастика')
        collector.add_new_book('Мальтийский сокол')
        collector.set_book_genre('Мальтийский сокол', 'Детективы')
        assert collector.get_books_genre() == {'Хромая судьба': 'Фантастика', 'Стажеры': 'Фантастика', 'Мальтийский сокол': 'Детективы'}

    def test_get_books_for_children_list_not_exist_age_rating_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мальтийский сокол')
        collector.set_book_genre('Мальтийский сокол', 'Детективы')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула','Ужасы')
        assert not 'Дракула' in collector.get_books_for_children() and not 'Мальтийский сокол' in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Жук в муравейнике')
        collector.set_book_genre('Жук в муравейнике', 'Фантастика')
        collector.add_book_in_favorites('Жук в муравейнике')
        assert collector.get_list_of_favorites_books() == ['Жук в муравейнике']

    def test_delete_book_from_favorites_delete_one_book_from_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Жук в муравейнике')
        collector.set_book_genre('Жук в муравейнике', 'Фантастика')
        collector.add_book_in_favorites('Жук в муравейнике')
        collector.delete_book_from_favorites('Жук в муравейнике')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_get_list_of_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Жук в муравейнике')
        collector.set_book_genre('Жук в муравейнике', 'Фантастика')
        collector.add_book_in_favorites('Жук в муравейнике')
        collector.add_new_book('Стажеры')
        collector.set_book_genre('Стажеры', 'Фантастика')
        collector.add_book_in_favorites('Стажеры')
        assert collector.get_list_of_favorites_books() == ['Жук в муравейнике', 'Стажеры']

    @pytest.mark.parametrize('name, genre', [['Хромая судьба', 'Фантастика'], ['Дракула','Ужасы'], ['Мальтийский сокол','Детективы'], ['38 попугаев','Мультфильмы'], ['Веселые ребята','Комедии']])
    def test_add_new_book_add_book_and_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

