from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from git_filter_repo import record_id_rename

from  .forms import CustomUserCreationForm
from django.core.mail import send_mail # импортируем метод джанго который служит для того что бы отправлять сообщения

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):# метод используется чтобы добавить функционал после обработки валидации формы
        user = form.save() # получаем его
        self.send_welcom_email(user.email)
        return  super().form_valid(form)

    def send_welcom_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Cпасбо, что зарегистриваролись в нашем сервисе'
        from_email = "MidLNight1@yandex.com" # Поста  с которой будет отслыаться приветсвенное сообщение
        recipted_list = [user_email]
        send_mail(subject, message, from_email, recipted_list)