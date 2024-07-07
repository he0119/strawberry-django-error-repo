from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Topic(models.Model):
    """话题"""

    id = models.AutoField("ID", primary_key=True, auto_created=True)
    title = models.CharField("标题", max_length=200)

    class Meta:
        verbose_name = "话题"
        verbose_name_plural = "话题"


class Comment(MPTTModel):
    """评论"""

    id = models.AutoField("ID", primary_key=True, auto_created=True)
    body = models.TextField("内容")
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="comments", verbose_name="话题"
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="属于",
    )

    class Meta:  # type: ignore
        verbose_name = "评论"
        verbose_name_plural = "评论"
