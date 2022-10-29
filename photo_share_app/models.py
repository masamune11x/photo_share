import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class PictureFolder(models.Model):
    #外部キー
    ownerID = models.ForeignKey(
        User, 
        #オーナーが削除されると写真フォルダーも連動して削除
        on_delete=models.CASCADE,
        null=True
        )

    picture_folder_name = models.CharField(
        max_length=100,
        )

    piture_folder_password = models.CharField(
        max_length=100,
        unique=True
        )

    created_date = models.DateTimeField(
        auto_now_add=True
        )

    # #これで管理画面にレコード名をフォルダー名で表示
    # def __str__(self):
    #     return self.picture_folder_name

class AllPictures(models.Model):
    #外部キー
    picture_folderID = models.ForeignKey(
        PictureFolder,
        #写真フォルダーが削除されるとフォルダー内の写真も連動して削除
        on_delete=models.CASCADE,
        )
        # upload_toはどこのディレクトリに画像をアップロードするかの設定
    images = models.ImageField(upload_to='media')




class PictureComment(models.Model):
    #外部キー
    pictureID = models.ForeignKey(
        AllPictures, 
        #フォルダー内の写真が削除されると写真コメントも連動して削除
        on_delete=models.CASCADE
        )

    comment = models.TextField()


