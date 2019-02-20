from django.urls import reverse_lazy

NAV_POSTS = 'Posts'

NAV_HOME = 'Home'
NAV_DEV = 'Dev'
NAV_SERVICE = 'Service'
NAV_CONTACT = 'Contact'

NAV_ITEMS = (
    (NAV_HOME, reverse_lazy('home')),
    (NAV_DEV, reverse_lazy('dev')),
    (NAV_SERVICE, reverse_lazy('service')),
    (NAV_CONTACT, reverse_lazy('contact')),

    (NAV_POSTS, reverse_lazy('blog')),

)


def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })
    return items
