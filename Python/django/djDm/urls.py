"""djDm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import view, testdb, search, search2

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^search$', search.search),
    url(r'^search_form$', search.search_form),
    url(r'^search-post$', search2.search_post),
    url(r'^$', testdb.testdb),
    url(r'^insert$', testdb.insert),
    url(r'^update$', testdb.update),
    url(r'^delete$', testdb.delete),
    url(r'^find$', testdb.find),
]
