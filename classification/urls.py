from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='acceuil'),
    path('liste_med/',views.search,name='liste_med'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('inscription/',views.inscritPage,name='inscription'),
    path('connecter/',views.conxPage,name='connecter'),
    path('logout/',views.logoutUser,name='logout'),
    path('profile/createcomnt/<str:pk>/',views.createcomnt,name='createcomnt'),
    path('pro_med/',views.pro_med,name='pro_med'),
    path('modifier/',views.modifier,name='modifier'),
    path('contact/',views.contact,name='contact'),
    path('propos/',views.propos,name='propos'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('rest_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
