from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .apiviews import PollViewSet, ChoiceList, CreateVote, CreateUser, LoginView


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote', CreateVote.as_view(), name='create_vote'),
    path('users', CreateUser.as_view(), name='user_create'),
    path('login', views.obtain_auth_token, name='login'),
]

urlpatterns += router.urls
