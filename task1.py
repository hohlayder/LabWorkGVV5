class Book:
    title = author = year = None

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'


b = Book()
b.title = 'Последнее желание'
b.author = 'Анджей Сапковский'
b.year = 1993
print(b.get_info())