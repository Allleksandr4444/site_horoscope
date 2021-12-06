from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type', views.type_window),
    path('type/<str:element>', views.type_element, name='element-name'),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope-name'),
]