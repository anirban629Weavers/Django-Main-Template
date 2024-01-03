from django.urls import path
from accounts.views import RegisterAPI, LoginAPI
from rest_framework.routers import SimpleRouter
from accounts.views import UserApi

router = SimpleRouter()
urlpatterns = [
    path("", RegisterAPI.as_view({'post': 'create'}), name="login"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("custom/test/", UserApi.as_view(), name="lasdogin"),

]

# router.register("custom/test", UserApi, basename="Custom Testing")
urlpatterns += router.urls
