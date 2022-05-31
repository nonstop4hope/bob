from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect, render


class Search(View):

    template_name = 'search/search.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):

        return self.get(request)


def logout_user(request):
    logout(request)
    return redirect('search:login')