from django.urls import path, include
from .views import Search
from .views import logout_user

app_name = 'search'

urlpatterns = [
    path('', Search.as_view(), name='search'),
    path('logout/', logout_user, name='logout'),
    path('search/', include('apps.search.google.urls'))
]
