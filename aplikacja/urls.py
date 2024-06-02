from django.urls import path

import aplikacja.views
from aplikacja import views

app_name = 'aplikacja'
urlpatterns = [
    path('', views.NoteListView.as_view(),name='note-list'),
    path('<int:year>/<int:month>/<int:day>/<int:notatkaid>/',
         views.note_detail,
         name='note_detail'),
    path('create/', views.create_note, name='create'),
    path('edit/<int:notatkaid>', views.edit_note, name='edit_note'),
]