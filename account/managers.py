from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,email, password, **extra_args ):
        if not email:
            raise ValueError("Email is an required field")
        
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email, password, **extra_args):

        extra_args.setdefault('is_staff',True)
        extra_args.setdefault('is_active',True)
        extra_args.setdefault('is_superuser',True)

        if extra_args.get('is_staff') is not True:
            raise ValueError("user must be staff")
        if extra_args.get('is_superuser') is not True:
            raise ValueError("user must be super user")
        return self.create_user(email, password,**extra_args)