"""
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path, include
from .views import UserList, ActivateAccount, UserCreate

app_name = 'accounts'
urlpatterns = [
    path('users/', UserList.as_view(), name='account_signup'),
    path('users/create/', UserCreate.as_view(), name='account_create'),  # 新しいエンドポイント
    path('activate/<uid>/<token>', ActivateAccount.as_view()),
]

"""
api/auth/ ^users/$ [name='useraccount-list']
api/auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-list']
api/auth/ ^users/activation/$ [name='useraccount-activation']     ## {uid: uid, token:token}
api/auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-activation']
api/auth/ ^users/me/$ [name='useraccount-me']
api/auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-me']
api/auth/ ^users/resend_activation/$ [name='useraccount-resend-activation']
api/auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-resend-activation']
api/auth/ ^users/reset_password/$ [name='useraccount-reset-password']
api/auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-reset-password']
api/auth/ ^users/reset_password_confirm/$ [name='useraccount-reset-password-confirm']
api/auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-reset-password-confirm']
api/auth/ ^users/reset_username/$ [name='useraccount-reset-username']
api/auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-reset-username']
api/auth/ ^users/reset_username_confirm/$ [name='useraccount-reset-username-confirm']
api/auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-reset-username-confirm']
api/auth/ ^users/set_password/$ [name='useraccount-set-password']
api/auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-set-password']
api/auth/ ^users/set_username/$ [name='useraccount-set-username']
api/auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-set-username']
api/auth/ ^users/(?P<username>[^/.]+)/$ [name='useraccount-detail']
api/auth/ ^users/(?P<username>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='useraccount-detail']
api/auth/ ^$ [name='api-root']
api/auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/auth/ ^jwt/create/? [name='jwt-create']
api/auth/ ^jwt/refresh/? [name='jwt-refresh']
api/auth/ ^jwt/verify/? [name='jwt-verify']
"""

""" djoser.urls
jwt_endpoints -----
（１）access tokenを取得する。有効期限は30分。
http://localhost:8000/api/v1/auth/jwt/create/
urlpatterns = [
    re_path(r"^jwt/create/?", views.TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
]
（２）

authtoken_endpoints -----
urlpatterns = [
    re_path(r"^token/login/?$", views.TokenCreateView.as_view(), name="login"),
    re_path(r"^token/logout/?$", views.TokenDestroyView.as_view(), name="logout"),
]

"""
