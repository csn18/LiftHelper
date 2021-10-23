from django.urls import path

from CodeWarsHelper.views import main_members, group_detail, member_detail

urlpatterns = [
    path('', main_members, name='main-members'),
    path('group/<int:pk>', group_detail, name='group'),
    path('member/<int:pk>', member_detail, name='member-detail'),
]
