from django.urls import path
from django.urls.conf import include
from App.api.views  import QuestionVS,UserSelectedCategory
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', QuestionVS, basename='QuestionVS')


urlpatterns = [
    path('', include(router.urls)),
    path('category/<str:type>', UserSelectedCategory.as_view()),
]