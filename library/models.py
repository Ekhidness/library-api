from django.db import models

class Author(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    biography = models.TextField("Биография", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField("Год публикации")
    genre = models.CharField("Жанр", max_length=100)
    CATEGORY_CHOICES = [
        ('fiction', 'Художественная литература'),
        ('textbook', 'Учебник'),
    ]
    category = models.CharField("Категория", max_length=20, choices=CATEGORY_CHOICES)
    publisher = models.CharField("Издательство", max_length=100)
    cover_image = models.ImageField("Обложка", upload_to='covers/', blank=True, null=True)
    book_file = models.FileField("Файл книги", upload_to='books/')

    def __str__(self):
        return f"{self.title} ({self.author})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author', 'publication_year', 'publisher'],
                name='unique_book_edition'
            )
        ]
        ordering = ['title']