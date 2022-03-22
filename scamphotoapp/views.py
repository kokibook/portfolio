import os
import shutil
from PIL import Image
from django.db.models.fields import IntegerField
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import PhotoModel, PersonModel
from .forms import PhotoForm
from .face_cut import face_cut
from .predict import predict


# トップ画面
def index(request):
    return redirect('login')


# ログイン画面
class Login(LoginView):
    template_name = "login.html"


# アカウント作成画面
class Signup(TemplateView):
    template_name = "signup.html"


# アカウント作成
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            email = ""
            user = User.objects.create_user(username, email, password)
            return render(request, "signup_complate.html")

        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザー名はすでに登録されています。"})

    return render(request, "signup.html")


# マイページ画面
class Mypage(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "mypage.html"
    paginate_by = 12

    def get_queryset(self):
        current_user = self.request.user
        return PersonModel.objects.filter(created_by = current_user).order_by('-created')


# 投稿一覧画面
class Share(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "share.html"
    model = PersonModel
    paginate_by = 12

    def get_queryset(self):
        return PersonModel.objects.order_by('-created')


# 判定画面
@login_required
def judge(request):
    context = {
        'form': PhotoForm(),
    }
    return render(request, "judge.html", context)


# 結果画面
@login_required
def result(request):
    # GETメソッド
    if not request.method == "POST":
        return redirect('judge')

   # POSTメソッド
    else:
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError("ファイルが不正です。")

        else:
            # 画像ディレクトリを初期化
            images_dir = "media/images"
            shutil.rmtree(images_dir)
            os.makedirs(images_dir, exist_ok=True)

            # 画像を保存
            photo = PhotoModel()
            uploaded_filename = request.FILES['image'].name
            image = form.cleaned_data['image']
            photo.image = image
            photo.save()

            # 画像のパスを取得
            filepath = os.path.join(images_dir, uploaded_filename)

            # 顔部分の検出
            try:
                face_image = face_cut(filepath, uploaded_filename)
            except Exception:
                context = {
                    'form': form,
                    'message': '顔の検出に失敗しました'
                }
                return render(request, "judge.html", context)
           
           # 予測
            females, classes, percentage = predict(face_image)

    context = {
        'form': form,
        'females': females,
        'classes': classes,
        'percentage': percentage,
        'face_image': face_image,
    }
    return render(request, "result.html", context)


# 新規作成画面
class Create(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "create.html"
    model = PersonModel
    fields = ('app', 'name', 'age', 'live', 'body', 'person_image')
    success_url = reverse_lazy('mypage')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# 削除画面
class DeleteComfirm(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    template_name = "delete-confirm.html"
    model = PersonModel
    success_url = reverse_lazy('mypage')


# 更新画面
class Update(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    template_name = "update.html"
    model = PersonModel
    fields = ('app', 'name', 'age', 'live', 'body', 'person_image')
    success_url = reverse_lazy('mypage')


# 詳細画面
class Detail(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = "detail.html"
    model = PersonModel

    context_object_name = "person"

