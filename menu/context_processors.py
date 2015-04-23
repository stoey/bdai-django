def menu(request):
    context = dict(
        menu_items=[
            dict(
                name="Bleeding Disorders",
                target="/bleeding-disorders",
                active=False,
            ),
            dict(
                name="Upcoming Events",
                target="/events/",
                active=False,
            ),
            dict(
                name="Support Us",
                target="/support-bdai",
                active=False,
            ),
            dict(
                name="Camp",
                target="/camp/",
                active=False,
            ),
            dict(
                name="What We Do",
                target="/support/",
                active=False,
                children=[
                    dict(
                        name="Assistance Programs",
                        target="/support/assistance/",
                    ),
                    dict(
                        name="Community Support",
                        target="/support/community/",
                    ),
                    dict(
                        name="Advocacy",
                        target="/support/advocacy",
                    ),
                    dict(
                        name="Education",
                        target="/support/education",
                    ),
                ]
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
        if request.path.startswith(menu_item['target']):
            menu_item['active'] = True
    return context
