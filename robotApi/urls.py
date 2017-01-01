from django.conf.urls import url
from robotApi import views

urlpatterns = [
    url(r'^api/component/list/$', views.componentList),
    url(r'^api/component/create/$', views.createComponent),
    url(r'^api/component/addSubcomponent/$', views.addSubcomponent),
    url(r'^api/component/addConnection/$', views.addConnection),
    url(r'^api/component/make/$', views.make),
    url(r'^api/component/svg/$', views.getSVG),
    url(r'^api/component/download/svg/$', views.downloadSVG),
    url(r'^api/component/fixEdgeInterface/$', views.fixEdgeInterface),
    url(r'^api/component/constrainParameter/$', views.constrainParameter),
    url(r'^api/component/download/yaml/$', views.downloadYaml),
    url(r'^api/component/addParameter/$', views.addParameter)
]