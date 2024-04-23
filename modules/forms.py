from django.contrib.auth.forms import UserCreationForm
from modules.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('Email', 'First_Name', 'Last_Name', 'password', 'Re_type_Your_password', 'Terms_Privacy_Policy')


