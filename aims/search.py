def search_by_category(items, category):
    return [item for item in items if category.lower() in item.category.lower()]

def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
