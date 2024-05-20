from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    def create_new_user(self, email: str, full_name: str, phone_number: str, password=None, group: list=None):

        if not email:
            raise ValueError("The given email must be set")

        if not full_name:
            raise ValueError("The given full name must be set")

        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model.objects.create(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
        )

        # user.save(using=self._db)

        print("setting group")
        if group is not None:
            user.group.set(group)
        else:
            user.group.set([])

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()  # Generate a unusable password

        user.save(using=self._db)
        return user