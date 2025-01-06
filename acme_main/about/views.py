from django.shortcuts import render


# Create your views here.
def about(request):
    template_name = 'about/description.html'
    return render(request, template_name)
