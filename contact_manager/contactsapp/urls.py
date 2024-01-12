from django.urls import path
# from .views import ContactView,ContactCreateView
from .import views

urlpatterns = [
    path('get_all/', views.get_all),
    path('add_contact/', views.add_contact),
    path('edit_contact/<int:pk>/', views.edit_contact),
    path('delete_contact/<int:pk>/', views.delete_contact),
    path('search/', views.search),
]



# for class based views

# urlpatterns = [
#     path('method/', ContactView.as_view(), name='contact-list'),
#     path('method/<int:pk>/', ContactView.as_view(), name='contact-detail'),
#     path('method/', ContactView.as_view(), name='contact-create'),
#     path('method/<int:pk>/', ContactView.as_view(), name='contact-update'),
#     path('method/<int:pk>/', ContactView.as_view(), name='contact-delete'),
#     path('search/', ContactCreateView.as_view(), name='search'),
# ]