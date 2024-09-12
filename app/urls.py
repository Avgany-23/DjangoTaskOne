from datetime import datetime
from django.urls import path
from .views import HomeView, WorkdirView, WorkdirDetail
from django.views.generic import TemplateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('time/', TemplateView.as_view(template_name='app/time_now.html',
                                       extra_context={'time_now': datetime.now().time()}), name='time'),
    path('workdir/', WorkdirView.as_view(), name='workdir'),
    path('workdir/detail/<str:name_file>', WorkdirDetail.as_view(), name='workdir_detail')
]
