from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()  # Get the custom User model

# Check if the User model is registered before trying to unregister it
if admin.site.is_registered(User):
    admin.site.unregister(User)

class CustomUserAdmin(BaseUserAdmin):
    # Customize the fields that show in the user detail view
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'created_at', 'updated_at')}),
    )
    
    # Customize the fields that show in the user creation view
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    
    # Customize the list view for users
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    
    # Optionally, add search fields if needed
    search_fields = ('username', 'email', 'user_type')
    
    # Optionally, add filters if needed
    list_filter = ('user_type',)

# Register the custom User admin
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(FacultyMember)
admin.site.register(StudentMember)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(ApprovalStage)
admin.site.register(Event)
admin.site.register(EventProof)
admin.site.register(Review)
admin.site.register(EventHistory)