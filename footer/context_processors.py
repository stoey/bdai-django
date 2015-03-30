from collections import defaultdict

from pages.models import Directory
from pages.models import Page

def footer(request):
    page_counts = defaultdict(int)
    pages = Page.objects.filter(footer_link=True)
    for page in pages:
        page_counts[page.path.partition('/')[0]] += 1
    columns = ([], [])
    total=0
    for dir_name, count in sorted(page_counts.items()):
        column = columns[0] if total < pages.count() / 2 else columns[1]
        column.append(Directory.objects.get(name=dir_name))
        total += count
    return dict(
        footer_columns=columns,
    )
