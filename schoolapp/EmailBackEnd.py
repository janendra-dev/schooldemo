from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

#  Authenticates against settings.AUTH_USER_MODEL.
class EmailBackEnd(ModelBackend):
    def authenticate(self,username=None, password=None, **kwargs):
        UserModel=get_user_model()#object to fetch username
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                # user hold different Customuser fields
                # print([user.user_type])
                return user#object
        return None