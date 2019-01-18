from django.urls import path
from .views import kickstarter_list

urlpatterns = [
    path('', kickstarter_list, name='home'),
    path('<int:pk>', kickstarter_list, name='kickstarter_list')
]
