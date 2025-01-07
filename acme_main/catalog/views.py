from django.shortcuts import render

acme_products = [
    {
        "id": 0,
        "category": "Tools",
        "title": "ACME Anvil",
        "description": "The classic ACME anvil, perfect for all your\
            cartoonish heavy-duty needs. Guaranteed to cause hilarious\
                mishaps and possibly flatten your toes if not careful,\
                  use wisely!",
        "price": 99.99
    },
    {
        "id": 1,
        "category": "Transportation",
        "title": "ACME Rocket Skates",
        "description": "Experience incredible, cartoon-like speeds and\
            occasional spontaneous combustion with these innovative\
                ACME rocket skates. Not for the faint of heart, or \
                  anyone concerned about their eyebrows. Use at your own risk!",
        "price": 129.99
    },
    {
        "id": 2,
        "category": "Traps",
        "title": "ACME Spring Trap",
        "description": "The most reliable way to capture your elusive quarry, \
          though it may sometimes capture yourself instead. Simple, effective,\
              and often backfires in the most unexpected ways,\
                  beware the recoiling spring!",
        "price": 49.95
    },
     {
        "id": 3,
        "category": "Gadgets",
         "title": "ACME Invisible Paint",
        "description": "Make anything, from yourself to your pets\
            to entire buildings, mostly disappear (from view).\
                Invisibility is not guaranteed to protect from touching things,\
                    remember to still look before you walk,\
                        and always proceed with caution!",
        "price": 79.95
    },
    {
        "id": 4,
        "category": "Food & Snacks",
        "title": "ACME Dehydrated Boulders",
        "description": "Just add water for a surprisingly\
          edible and rock-solid treat. Perfect for creating\
              unexpected rock slides or a quick, portable\
                  snack on the go during adventures, \
                    or even for decorating your garden with edible stones!",
        "price": 14.99
    }
]


# Create your views here.
def product_list(request):
    template_name = 'catalog/product_list.html'
    context = {'products': acme_products}
    return render(request, template_name, context)


def product_detail(request, id):
    template_name = 'catalog/product_detail.html'
    context = {'product': acme_products[id]}
    return render(request, template_name, context)


def category(request, category_name):
    template_name = 'catalog/product_detail.html'
    context = {'category': acme_products[category_name]}
    return render(request, template_name, context)
