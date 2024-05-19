from django.urls import path

import aplikacja.views
from aplikacja import views

app_name = 'aplikacja'
#
# urlpatterns = [
#     path('', views.note_list, name='note_list')
# ]
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.NoteListView.as_view(),name='note-list'),
    path('<int:year>/<int:month>/<int:day>/',
         views.note_detail,
         name='note_detail'),
    path('create/', views.create_note, name='create'),
    path('edit/<int:note_id>', views.edit_note, name='edit_note'),
]