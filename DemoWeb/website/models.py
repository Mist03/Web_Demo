from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(max_length=100, default='')
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"slug": self.category.slug})
    # def get_absolute_url(self):
    # return reverse("service", kwargs={"slug": self.category.slug})


class Our_Services(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    slug = models.SlugField(max_length=100, default='')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Post, through='CartProduct')
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.title



