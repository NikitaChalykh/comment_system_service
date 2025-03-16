from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Article Title'  # Translation
    )
    text = models.TextField(
        verbose_name='Article Text'  # Translation
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Article Author'  # Translation
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Article Creation Date'  # Translation
    )

    class Meta:
        verbose_name = "Article"  # Translation
        verbose_name_plural = "Articles"  # Translation

    def __str__(self):
        return self.name[:15]


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Comment Text'  # Translation
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Comment Author'  # Translation
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Article'  # Translation
    )
    main_comment = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        related_name='nested_comments',
        verbose_name='Main Comment'  # Translation
    )
    nested_level = models.PositiveIntegerField(
        default=0,
        verbose_name='Comment Nesting Level'  # Translation
    )

    class Meta:
        verbose_name = "Comment"  # Translation
        verbose_name_plural = "Comments"  # Translation

    def __str__(self):
        return self.text
