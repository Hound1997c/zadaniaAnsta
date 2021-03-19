from django.conf.urls import url
from django.views.generic import RedirectView, TemplateView
#
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete_contact/(?P<pk>\d+)/$', views.deleteContact, name='deleteContact'),
    url(r'^newContact', views.newContact, name='newContact'),
    url(r'^add_email/(?P<osoba_pk>\d+)$', views.addEmail, name='addEmail'),
    url(r'^add_phone/(?P<osoba_pk>\d+)$', views.addPhone, name='addPhone'),
    url(r'^edit_contact/(?P<osoba_pk>\d+)$', views.editContact, name='editContact'),
    url(r'^find_contact$', views.findContact, name='findContact'),
    #     # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]