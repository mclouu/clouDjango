from django.shortcuts import render

from blog import model_helpers
from blog import navigation
from blog.models import Post


def post_list(request, category_name=model_helpers.post_category_all.slug()):
    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'category': category,
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/post_list.html', context)


def home(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_HOME),
    }
    return render(request, 'blog/home.html', context)


def dev(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_DEV),
    }
    return render(request, 'blog/dev.html', context)


def service(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_SERVICE),
    }
    return render(request, 'blog/service.html', context)


def contact(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CONTACT),
    }
    return render(request, 'blog/contact.html', context)
