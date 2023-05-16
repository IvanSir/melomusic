from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'is_staff', 'id']

    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        (_('Personal Info'), {'fields' : ('name', 'picture', 'username', 'friends', )}),
        (
            _('Permissions'),
            {'fields' : ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields' : ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Save the user instance
        obj.save()

        # Check if any friends have been added in the admin panel
        friends = form.cleaned_data.get('friends')
        if friends:
            for friend in friends:
                # Add the user as a friend of each selected friend
                friend.friends.add(obj)
        
        # Save the user instance again to update the friendships
        obj.save()

admin.site.register(User, UserAdmin)