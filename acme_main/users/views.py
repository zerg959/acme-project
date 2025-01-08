from django.shortcuts import render

# Create your views here.
acme_users = [
]


def users_list(request):
    template_name = 'users/users_list.html'
    context = {'acme_users': acme_users}
    return render(request, template_name, context)


# def user_profile(request):
#     template_name = 'users/user_profile.html'
#     context = {'user_profile': acme_users[id]}
#     return render(request, template_name, context)
