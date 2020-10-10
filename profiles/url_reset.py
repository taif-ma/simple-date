from django.conf.urls import url
from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import PasswordResetView, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView

urlpatterns = [
    #url('^$', PasswordResetView, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    #url(r'^done/$', PasswordResetDoneView, name='password_reset_done'),
    #url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView,
    #    {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    #url('^complete/$', PasswordResetCompleteView, name="password_reset_complete"),
    
    path('', PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    
    path('', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
