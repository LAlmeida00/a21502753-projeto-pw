from django.db import models

class User(models.Model):
    user = models.CharField(max_length=50)
    image_profile =  models.ImageField(upload_to='profile/', null=True)

    def __str__(self):
        return self.user

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class PostImage(models.Model):
    image_post = models.ImageField(upload_to='post_image/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images', null=True)

    def __str__(self):
        return str(self.image_post)

class Comment(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='ratings', null=True)

    MUITO_MAU = 1
    MAU = 2
    BOM = 3
    MUITO_BOM = 4
    EXCELENTE = 5

    RATING_CHOICES = [
        (MUITO_MAU, '⭐'),
        (MAU, '⭐⭐'),
        (BOM, '⭐⭐⭐'),
        (MUITO_BOM, '⭐⭐⭐⭐'),
        (EXCELENTE, '⭐⭐⭐⭐⭐'),
    ]

    rate_value = models.IntegerField(choices=RATING_CHOICES, default=1, blank=True, null=True)

    def __str__(self):
        return dict(self.RATING_CHOICES)[self.rate_value]
