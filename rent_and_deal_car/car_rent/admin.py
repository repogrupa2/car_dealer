from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .apps import CarRentConfig
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Branch, Model, RentalOffer, BranchCarAvailability, Brand, Vehicle, CarRental




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Branch)
admin.site.register(BranchCarAvailability)
admin.site.register(RentalOffer)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(CarRental)




