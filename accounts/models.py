from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models import UniqueConstraint, Q


phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("phone is required.!")

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class UserType(models.TextChoices):
        """Register vaqtida foydalanuvchi tanlaydi — faqat 2 ta"""
        USER = 'user', 'User'
        BUSINESS = 'business', 'Business Owner'

    class StaffRole(models.TextChoices):
        """Biznes egasi o'z xodimlariga beradi"""
        RECEPTIONIST = 'receptionist', 'Receptionist'
        CASHIER = 'cashier', 'Cashier'
        MANAGER = 'manager', 'Manager'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    user_type  = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.USER
    )
    staff_role = models.CharField(
        max_length=20,
        choices=StaffRole.choices,
        blank=True,  # oddiy user uchun bo'sh
        null=True
    )

    # For PermissionMixin
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_set'  
    )
    # groups and user_permissions


    # --- Asosiy fieldlar ---
    phone = models.CharField(max_length=13, unique=True,
                                    db_index=True, validators=[phone_validator])

    status = models.CharField(max_length=20, choices=Status.choices)

    # --- Shaxsiy ma'lumotlar ---
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=5,
                                    choices=[('uz','UZ'),('ru','RU'),('en','EN')],
                                    default='uz')
    image = models.ImageField(upload_to='images/', blank=True)

    # --- Biznes egasi uchun qo'shimcha ---
    company = models.CharField(max_length=150, blank=True, db_index=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    stir = models.CharField(max_length=20, blank=True, null=True)
    legal_address= models.CharField(max_length=255, blank=True)

    # --- Tizim fieldlari ---
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deletion_requested_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')
        constraints = [
            # NULL bo'lmagan INN lar unique bo'lsin
            UniqueConstraint(
                fields=['inn'],
                condition=Q(inn__isnull=False) & ~Q(inn=''),
                name='unique_non_null_inn'
            ),
            UniqueConstraint(
                fields=['stir'],
                condition=Q(stir__isnull=False) & ~Q(stir=''),
                name='unique_non_null_stir'
            ),
        ]

    def __str__(self):
        return f"{self.phone} ({self.get_user_type_display()})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_business(self):
        return self.user_type == self.UserType.BUSINESS

    @property
    def is_approved(self):
        return self.status == self.Status.APPROVED