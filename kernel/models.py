from django.db import models


# Create your models here.
class Lang(models.Model):
    def __str__(self):
        return self.short_name

    class Meta:
        db_table = 'lang'

    short_name = models.CharField(max_length=4)
    full_name = models.CharField(max_length=16)


class PostType(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'post_type'

    name = models.CharField(max_length=30)
    description = models.TextField()


class PostData(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post_data'

    title = models.CharField(max_length=60, null=False)
    image = models.ImageField()
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=20, blank=True, null=True)
    post_type = models.ForeignKey(PostType)
    post_lang = models.ForeignKey(Lang)


class Hashtag(models.Model):
    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'hashtag'

    tag = models.CharField(max_length=30)
    connects = models.ManyToManyField(PostData)


class Dictonary(models.Model):
    def __str__(self):
        return self.word

    class Meta:
        db_table = 'dictonary'

    word = models.CharField(max_length=100)
    mean = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    lang = models.ForeignKey(Lang)


class Comment(models.Model):
    def __str__(self):
        return self.com_user

    class Meta:
        db_table = "comm"

    com_user = models.CharField(max_length=50, verbose_name='')
    com_mail = models.EmailField()
    com_data = models.TextField()
    com_arnold = models.ForeignKey(PostData)
