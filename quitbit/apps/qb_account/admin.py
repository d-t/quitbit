from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm as BaseChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm as BasePasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from apps.qb_main.models import Cigarette, Comment
# from apps.qb_account.models import SmokingHabit
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CommentAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user", "parent_comment", "created", "modified"]
    readonly_fields = ("created","modified",)

class CigaretteAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user", "cigarette_date", "cigarette_time"]
    readonly_fields = ("cigarette_date","cigarette_time",)


# --- User management forms --- #
# See: http://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
class CustomUserChangeForm(BaseChangeForm):
    class Meta(BaseChangeForm.Meta):
        model = UserModel


class CustomUserCreationForm(BaseCreationForm):
    class Meta(BaseCreationForm.Meta):
        model = UserModel

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = BaseUserAdmin.fieldsets + (
        [
            _('Personal info'), {
                'fields': [
                    'birth_date', 'address', 'city', 'country',
                    'gender', 'about'
                ]
            },
        ],
        [
            _('Smoking info'), {
                'fields': [
                    'years_smoked', 'cigarettes_per_day', 'packet_cost', 'cigarette_brand', 'cigarette_type', 'money_saved', 'last_cigarette',
                ]
            },

        ],
     )


admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(Cigarette, CigaretteAdmin)
admin.site.register(Comment, CommentAdmin)
