from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Branch, Model, RentalOffer, Brand, Vehicle, CarRental


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'balance', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'balance', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('id',)


class CarRentalAdmin(admin.ModelAdmin):
    model = CarRental
    list_display = ('customer_id', 'rental_offer_id', 'total_price',
                    'date_of_rent', 'is_rented')
    list_filter = ('is_rented',)
    fieldsets = (
        (None)
    )

    def has_add_permission(self, request):
        return False


class RentalOfferAdmin(admin.ModelAdmin):
    # form = RentalOffer
    model = RentalOffer
    list_display = ('Vehicle_Id', 'Categories', 'Deposit', 'Price_per_day')

    # fieldsets = (
    #     (None, {'fields': ('Vehicle_Id', 'BranchCarAvailability_Id',
    #                        'Categories', 'Deposit', 'Price_per_day',)}),
    #     'Permissions'
    # )


# Connect view site in admin to homepage
admin.site.site_url = "/"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Branch)
admin.site.register(RentalOffer, RentalOfferAdmin)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(CarRental, CarRentalAdmin)
