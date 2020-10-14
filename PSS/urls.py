from django.conf.urls import url
from . import views

app_name = 'PSS'
urlpatterns = [
    url(r'^$',views.Login, name = 'login'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^logout/$', views.Logout, name = 'logout'),
    url(r'^PSS/$', views.homepage, name = 'home'),
    url(r'^PSS/hub/(?P<hub_name>[\w\s.@+-]+)/$', views.hubDetail, name = 'hub-detail'),
    url(r'^PSS/hub/(?P<hub_name>[\w\s.@+-]+)/load_delete/(?P<load_name>[\w\s.@+-]+)/$', views.loadDelete, name = 'load-delete'),
    url(r'^PSS/hub/(?P<hub_name>[\w\s.@+-]+)/panel_delete/(?P<panel_name>[\w\s.@+-]+)/$', views.panelDelete, name = 'panel-delete'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/yeardata/$', views.hubYearData, name = 'hub-year-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/monthdata/$', views.hubMonthData, name = 'hub-month-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/daydata/$', views.hubDayData, name = 'hub-day-data'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^payment/(?P<amount>[0-9]+)/$', views.payment, name='payment'),
    url(r'^payment/success/(?P<amount>[0-9]+)/$', views.paymentSuccess, name='payment-success'),
    url(r'^charge/$', views.charge, name='charge'),
    url(r'^PSS/hub/(?P<hub_name>[\w\s.@+-]+)/load/(?P<load_name>[\w\s.@+-]+)/$', views.loadDetail, name = 'load-detail'),
    url(r'^PSS/hub/(?P<hub_name>[\w\s.@+-]+)/panel/(?P<panel_name>[\w\s.@+-]+)/$', views.panelDetail, name = 'panel-detail'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/load/(?P<load_name>[\w\s.@+-]+)/yeardata/$', views.loadYearData, name = 'load-year-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/load/(?P<load_name>[\w\s.@+-]+)/monthdata/$', views.loadMonthData, name = 'load-month-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/load/(?P<load_name>[\w\s.@+-]+)/daydata/$', views.loadDayData, name = 'load-day-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/panel/(?P<panel_name>[\w\s.@+-]+)/yeardata/$', views.panelYearData, name = 'panel-year-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/panel/(?P<panel_name>[\w\s.@+-]+)/monthdata/$', views.panelMonthData, name = 'panel-month-data'),
    url(r'^hub/(?P<hub_name>[\w\s.@+-]+)/panel/(?P<panel_name>[\w\s.@+-]+)/daydata/$', views.panelDayData, name = 'panel-day-data'),
    url(r'^PSSdata/upload/$', views.dataUpload, name = 'data-upload'),
    url(r'^usersinfo/$', views.usersInfo, name = 'users_info'),
]