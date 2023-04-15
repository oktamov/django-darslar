from blog.models import Category


def head_categories(request):
    return {"head_categories": Category.objects.order_by("id")}
