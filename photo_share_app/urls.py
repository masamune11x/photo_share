from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [


    #ホーム画面
    path('', views.home, name = 'home'),

    #写真フォルダーログイン
    path('photos_share_login', views.photos_share_login, name ='photos_share_login'),

    #オーナー用のsign out, sign in, logout
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('logout/', views.logout_user, name = 'logout'),

    #オーナー専用画面、写真フォルダ一覧、写真フォルダ作成、写真フォルダ削除
    path('owner_platform/', views.owner_platformview, name='owner_platform'),
    path('owner_add_platform/', views.owner_platform_add_photos, name='owner_add_platform'),
    path('owner_delete_platform/<int:pk>', views. owner_platform_deleteview, name='owner_delete_platform'),    

    #写真プラットフォーム
    path('photo_platform/', views.platformview, name='photo_platform'),
    path('photo_add_platform/', views.photo_add, name='photo_add_platform'),
    #pkにall_picturesテーブルのidを格納
    path('photo_delete_platform/<int:pk>', views.platform_deleteview, name='photo_delete_platform'),
    
]\
+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
