from django.shortcuts import render


# Create your views here.
def product_list(request):
    template_name = 'catalog/product_list.html'
    return render(request, template_name)


def product_detail(request, pk):
    template_name = 'catalog/product_detail.html'
    context = {'pk': pk}
    return render(request, template_name, context)
