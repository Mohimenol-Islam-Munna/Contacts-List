from django.urls import path
from .views import index, create, details, edit, destroy


urlpatterns = [
    path('', index, name='homePage'),
    path('create-contact/', create, name='create-contact'),
    path('contact-details/<int:pk>', details, name='contact-details'),
    path('edit-contact/<int:pk>', edit, name='edit-contact'),
    path('delete-contact/<int:pk>', destroy, name='delete-contact'),
]
