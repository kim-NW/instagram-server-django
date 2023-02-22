from django.db import models
from common.models import CommonModel

# caption: 댓글 내용

# USER
# FEED


class Review(CommonModel):
    caption = models.CharField(max_length=150)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    def __str__(self) -> str:
      return self.caption
