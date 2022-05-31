from django.urls import path, include

urlpatterns = [
    path('search/', include('apps.search.google.urls'))
]
