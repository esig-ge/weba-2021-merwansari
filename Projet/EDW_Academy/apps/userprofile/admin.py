# Register your models here.
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class UserCreationForm(forms.ModelForm):
    # Formulaire de création users
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Vérifie si les deux entrées mdp sont semblables
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Sauvegarde de mdp sous forme de hash
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # Form qui met à jour les users, et remplace le mdp par le hash

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'is_active', 'is_admin')

    def clean_password(self):

        return self.initial["password"]


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    # Champs affichés pour le User Model

    list_display = ('username', 'email', 'is_superadmin', 'is_admin', 'is_coach')
    list_filter = ('is_admin', 'is_coach')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Account info', {'fields': ('username',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date')}),
        ('Permissions', {'fields': ('is_superadmin', 'is_admin', 'is_coach')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'birth_date', 'is_admin', 'password1',
                       'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
