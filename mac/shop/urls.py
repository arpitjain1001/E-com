from django.urls import path
from . import views


urlpatterns = [
  path('admin/',views.admin),
  path('index/',views.index),
  path('about/',views.about),
  path('contactus/',views.contact),
  path('tracker/',views.tracker),
  path('search/',views.search),
  path('products/<int:myid>',views.prodview),
  path('checkout/',views.checkout),
]
