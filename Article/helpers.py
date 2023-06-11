class ARTICLE_STATUS:
    DRAFT = "draft"
    PUBLISH = "publish"
    DONE = "done"
    CHOICES = (
        (DRAFT, "پیش نویس"),
        (PUBLISH, "انتشار"),
        (DONE, "پایان انتشار"),
    )


class ArticleStatusStatusArticle:
    DRAFT = "draft"
    PUBLISH = "publish"
    DONE = "done"
    CHOICES = (
        (DRAFT, 'warning'),
        (PUBLISH, 'success'),
        (DONE, 'danger'),
    )