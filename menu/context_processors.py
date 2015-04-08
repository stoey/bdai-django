def menu(request):
    context = dict(
        menu_items=[
            dict(
                name="Bleeding Disorders", 
                target="/bleeding-disorders",
                active=False
            ),
            dict(
                name="Upcoming Events", 
                target="/events/",
                active=False
            ),
            dict(
                name="Support Us", 
                target="/support-bdai",
                active=False
            ),
        ],
    )
    if request.user.is_staff:
        context['menu_items'].append(dict(
            name="Admin", 
            target="/admin/",
            active=False
        ))
    for menu_item in context['menu_items']:
        if request.path == menu_item['target']:
            menu_item['active'] = True
    return context