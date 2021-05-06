from kartify.category.models import Category


def category_links(request):
    return dict(category_links=Category.objects.all())
