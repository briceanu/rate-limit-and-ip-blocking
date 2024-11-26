from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

router.register(r'sign_up',views.UserSignUpAPI,basename='signup')
urlpatterns = [
    path('sign_in/', views.UserSingInAPI.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]

urlpatterns += router.urls


# when only using router
# urlpatterns = router.urls
