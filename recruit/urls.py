from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
    path('res/',views.res,name='res'),
    path('view_all_internships/',views.view_all_internships,name='view_all_internships'),
    path('detail_abt_internship/<int:id>/',views.detail_abt_internship,name='detail_abt_internship'),
    path('IT_cat/',views.IT_cat,name='IT_cat'),
    path('Mech_cat/',views.Mech_cat,name='Mech_cat'),
    path('Ece_cat/',views.Ece_cat,name='Ece_cat'),
    path('Mrk_cat/',views.Mrk_cat,name='Mrk_cat'),
    # path('intern_resume/',views.intern_resume,name='intern_resume'),
    path('congrats/',views.congrats,name='congrats'),
    path('search/',views.search,name='search'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
