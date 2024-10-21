# Vulnerable Task Manager

from django.urls import path

from taskManager import views

urlpatterns = [
                       path('', views.index, name='index'),

                       # User details
                       path('view_all_users/',
                           views.view_all_users, name='view_all_users'),

                       # File
                       path('download/<int:file_id>/',
                           views.download, name='download'),
                       path('<int:project_id>/upload/',
                           views.upload, name='upload'),
                       path('downloadprofilepic/<int:user_id>/',
                           views.download_profile_pic, name='download_profile_pic'),

                       # Authentication & Authorization
                       path('register/', views.register, name='register'),
                       path('login/', views.login, name='login'),
                       path('step3/', views.step3, name='step3'),
                       path('step5/', views.step5, name='step5'),
                       path('logout/', views.logout_view, name='logout'),
                       path('manage_groups/', views.manage_groups,
                           name='manage_groups'),
                       path('profile/', views.profile, name='profile'),
                       path('change_password/', views.change_password,
                           name='change_password'),
                      path('forgot_password/', views.forgot_password,
                           name='forgot_password'),
                      path('reset_password/', views.reset_password,
                           name='reset_password'),
                       path('profile/<int:user_id>',
                           views.profile_by_id, name='profile_by_id'),
                       path('profile_view/<int:user_id>',
                           views.profile_view, name='profile_view'),

                       # Projects
                       path('project_create/', views.project_create,
                           name='project_create'),
                       path('<int:project_id>/edit_project/',
                           views.project_edit, name='project_edit'),
                       path('manage_projects/', views.manage_projects,
                           name='manage_projects'),
                       path('<int:project_id>/project_delete/',
                           views.project_delete, name='project_delete'),
                       path('<path:project_id>/project_details/',
                           views.project_details, name='project_details'),
                       path('project_list/', views.project_list,
                           name='project_list'),

                       # Tasks
                       path('<int:project_id>/task_create/',
                           views.task_create, name='task_create'),
                       path('<int:project_id>/<int:task_id>/',
                           views.task_details, name='task_details'),
                       path('<int:project_id>/task_edit/<int:task_id>',
                           views.task_edit, name='task_edit'),
                       path('<int:project_id>/task_delete/<int:task_id>',
                           views.task_delete, name='task_delete'),
                       path('<int:project_id>/task_complete/<int:task_id>',
                           views.task_complete, name='task_complete'),
                       path('task_list/', views.task_list, name='task_list'),
                       path('<int:project_id>/manage_tasks/',
                           views.manage_tasks, name='manage_tasks'),


                       # Notes
                       path('<int:project_id>/<int:task_id>/note_create/',
                           views.note_create, name='note_create'),
                       path('<int:project_id>/<int:task_id>/note_edit/<int:note_id>',
                           views.note_edit, name='note_edit'),
                       path('<int:project_id>/<int:task_id>/note_delete/<int:note_id>',
                           views.note_delete, name='note_delete'),

                       path('dashboard/', views.dashboard, name='dashboard'),
                       path('search/', views.search, name='search'),

                       # Settings - DEBUG
                       path('settings/', views.tm_settings, name='settings'),
                       path('view_img/', views.view_img, name='view_img'),
                       path('ping/', views.ping, name='ping'),
                      ]
