from django.db import models
from django.contrib.auth import get_user_model

# アプリ名
APPNAME = (
    ("", "選択してください"),
    ("Tinder", "Tinder"),
    ("Tapple", "Tapple"),
    ("With", "With"),
    ("Pairs", "Pairs"),
    ("Omiai", "Omiai"),
    ("Cross Me", "Cross Me"),
    ("Marrish", "Marrish"),
    ("Poyboy", "Poyboy"),
    ("Eve Eve", "Eve Eve")
)

# 年齢
AGE = (
    ("", "選択してください"),
    ("十代後半", "10代後半"),
    ("二十代前半", "20代前半"),
    ("二十代後半", "20代後半"),
    ("三十代前半", "30代前半"),
    ("三十代後半", "30代後半"),
    ("四十代前半", "40代前半"),
    ("四十代後半", "40代後半"),
    ("五十代前半", "50代前半"),
    ("五十代後半", "50代後半"),
    ("六十代以上", "60代以上")
)

# 住み
LIVE = (
    ("", "選択してください"),
    ("北海道", "北海道"),
    ("青森県", "青森県"),
    ("岩手県", "岩手県"),
    ("宮城県", "宮城県"),
    ("秋田県", "秋田県"),
    ("山形県", "山形県"),
    ("福島県", "福島県"),
    ("茨城県", "茨城県"),
    ("栃木県", "栃木県"),
    ("群馬県", "群馬県"),
    ("埼玉県", "埼玉県"),
    ("千葉県", "千葉県"),
    ("東京都", "東京都"),
    ("神奈川県", "神奈川県"),
    ("新潟県", "新潟県"),
    ("富山県", "富山県"),
    ("石川県", "石川県"),
    ("福井県", "福井県"),
    ("山梨県", "山梨県"),
    ("長野県", "長野県"),
    ("岐阜県", "岐阜県"),
    ("静岡県", "静岡県"),
    ("愛知県", "愛知県"),
    ("三重県", "三重県"),
    ("滋賀県", "滋賀県"),
    ("京都府", "京都府"),
    ("大阪府", "大阪府"),
    ("兵庫県", "兵庫県"),
    ("奈良県", "奈良県"),
    ("和歌山県", "和歌山県"),
    ("鳥取県", "鳥取県"),
    ("島根県", "島根県"),
    ("岡山県", "岡山県"),
    ("広島県", "広島県"),
    ("山口県", "山口県"),
    ("徳島県", "徳島県"),
    ("香川県", "香川県"),
    ("愛媛県", "愛媛県"),
    ("高知県", "高知県"),
    ("福岡県", "福岡県"),
    ("佐賀県", "佐賀県"),
    ("長崎県", "長崎県"),
    ("熊本県", "熊本県"),
    ("大分県", "大分県"),
    ("宮崎県", "宮崎県"),
    ("鹿児島県", "鹿児島県"),
    ("沖縄県", "沖縄県")
)


# <-------------以下モデル------------------->


# AI判別した画像の保存先
class PhotoModel(models.Model):
    image = models.ImageField(upload_to="images/")


# 投稿に関するモデル
class PersonModel(models.Model):
    app = models.CharField(
        max_length=20, 
        blank=False,
        null=False,
        verbose_name="アプリ名",
        choices=APPNAME
    )
    
    name = models.CharField(
        max_length=100,
        blank=False, 
        null=False,
        verbose_name="名前"
    )
    
    age = models.CharField(
        max_length=50,
        blank=False, 
        null=False,
        verbose_name="年齢",
        choices=AGE
    )
    
    live = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="住み",
        choices=LIVE
    )
    
    body = models.TextField(
        verbose_name="感想"
    )
    
    person_image = models.ImageField(
        upload_to="people/",
        blank=False,
        null=False,
        verbose_name="写真"
    )

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="投稿者"
    )
    
    created = models.DateTimeField(
        auto_now_add=True, 
        editable=False,
        blank=False,
        null=False
    )

    updated = models.DateTimeField(
        auto_now=True, 
        editable=False,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name