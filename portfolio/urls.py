from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_page_view, name='index'),
    path('resume/', views.resume_page_view, name='resume'),
    path('portfolio/', views.portfolio_page_view, name='portfolio'),

    # login e logout
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    # CRUD
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('edit-resume/', views.edit_resume_view, name='edit_resume'),
    path('edit-portfolio/', views.edit_portfolio_view, name='edit_portfolio'),
    path('portfolio/delete-project/<int:project_id>/', views.delete_project, name='delete_project'),


    # recovery password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='portfolio/registration/password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='portfolio/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='portfolio/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='portfolio/registration/password_reset_complete.html'), name='password_reset_complete'),
]