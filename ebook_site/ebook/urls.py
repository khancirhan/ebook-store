from django.urls import path
from ebook import views

app_name = 'ebook'

urlpatterns = [
    path('', views.index, name='index'),
    path('ebooks/<int:category>/<int:subject_id>', views.ebooks, name='ebooks'),
    path('ebooks/<int:category>/ebook/<int:ebook_id>', views.ebook, name='ebook'),
    path('search', views.search, name='search'),
    path('subjects', views.subjects, name='subjects'),
    path('preview/<int:ebook_id>',views.preview, name='preview'),
    path('download/<int:ebook_id>',views.download, name='download'),
]
