from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('ivtPage', views.ivtPage),

    path('fiitPage', views.fiitPage),

    path('kbPage', views.kbPage),

    path('piPage', views.piPage),

    path('moaisPage',views.moaisPage),

    path('siPage',views.siPage)
]
