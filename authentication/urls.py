from django.urls import path

from . import views

urlpatterns = [

        path('',views.get_login_page),

        path('sign-up/',views.get_sign_up_page)
]
