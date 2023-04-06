from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path("", views.index, name="index"),

    path("headline/", views.headlines, name = "headlines"),

    path("headline/<int:headline_id>/", views.detail,name = 'detail'), 
    #this name can be use in the html file for dynamic reference to this url
    #To access this url from html templates files uses: <a href = "{% url 'detail' %}"> ...<a/>
    path("add/", views.add_HL, name = 'add_HL'),

    #update link path
    path('update/<int:id>/',views.update_HL,name = "update_HL"),
    path('delete/<int:id>/',views.delete_HL, name='delete_HL'),
    path('srs_download', views.srs_download, name='srsdownloadfile'),
    
]
