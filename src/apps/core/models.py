from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    title = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='core/products_image', blank=True, null=True)

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/blog_images")
    author = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

