from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import CustomUserCompleteDetails, PaymentForm
from .models import Branch, Vehicle, Model, RentalOffer, CarRental, CustomUser
import datetime

User = get_user_model()


def home(request):
    vehicles = Vehicle.objects.all()
    ctx = {'vehicles': vehicles}

    return render(request, "car_rent/home.html", context=ctx)


class AccountDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)

        account = [user.first_name, user.last_name, user.street, user.house_number,
                   user.zip_code, user.city, user.credit_card_nr, user.mobile]
        count = 0
        for i in account:
            if len(str(i)) is 0 or i is None:
                count += 1
        if count > 0:
            ctx = {'user': user, 'count': count}
        else:
            ctx = {'user': user}
        return render(self.request, "car_rent/account_details.html", context=ctx)


class AdminPanel(View):
    def get(self, request, *args, **kwargs):
        return render(request, "admin")


class ListOfBranches(View):
    def get(self, request, *args, **kwargs):
        list_of_branches = Branch.objects.all()
        ctx = {'list_of_branches': list_of_branches}
        return render(self.request, 'car_rent/list_of_branches.html', context=ctx)


class ListOfRentalOffers(View):
    def get(self, request, *args, **kwargs):
        list_of_offers = RentalOffer.objects.all()
        vehicles = Vehicle.objects.all()
        user = CustomUser.objects.get(id=request.user.id)
        car_rentals = CarRental.objects.filter(customer_id=user.id)
        car_rental_availability = CarRental.objects.filter(is_rented=True)
        branch = Branch.objects.all()
        list = []

        for a in car_rental_availability:
            list.append(a.rental_offer_id.id)

        if list:
            print("List")
        else:
            print("No list")
        ctx = {'list_of_offers': list_of_offers, 'branch': branch,
               'vehicles': vehicles, 'car_rental_availability': list}

        for customer_record in car_rentals:
            if customer_record.is_rented:
                ctx['rented'] = customer_record.rental_offer_id.id
                return render(request, "car_rent/list_of_offers.html", context=ctx)

        return render(self.request, 'car_rent/list_of_offers.html', context=ctx)


class RentalOfferView(View):
    def get(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
            vehicles = Vehicle.objects.all()
            ctx = {"rental_offer": rental_offer, 'vehicles': vehicles}
        except RentalOffer.DoesNotExist:
            ctx = {'rental_offer_id': id}
        return render(request, "car_rent/offer.html", context=ctx)


class ModelList(View):
    def get(self, request, *args, **kwargs):
        model = Model.objects.all()
        ctx = {'model': model}

        return render(self.request, "car_rent/model_list.html", context=ctx)


class CarRentalDetails(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)

        except RentalOffer.DoesNotExist:
            return HttpResponse("This offer does not exist")

        date = datetime.date.today()
        '''Take loged user'''
        user = CustomUser.objects.get(id=request.user.id)
        '''Take all record for user who rent any car'''
        car_rentals = CarRental.objects.filter(customer_id=user.id)

        for customer_record in car_rentals:
            '''
            If the user is still renting any car then return rented is True then not have option to rent
            '''
            if customer_record.is_rented:
                ctx = {"offer": offer, "date": date, 'rented': True}
                return render(request, "car_rent/car_rental.html", context=ctx)

        ctx = {"offer": offer, "date": date}
        return render(request, "car_rent/car_rental.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)
            user = CustomUser.objects.get(id=request.user.id)

        except RentalOffer.DoesNotExist:
            return HttpResponse("This offer does not exist")

        date = datetime.date.today()
        ctx = {'offer': offer, "date": date, 'user': user}

        user_details = [user.street, user.house_number, user.zip_code, user.city,
                        user.credit_card_nr, user.expiration, user.CVV, user.mobile]

        car_rentals = CarRental.objects.filter(rental_offer_id=offer.id, is_rented=True)


        if None not in user_details:
            if user.balance - offer.Deposit >= 0:
                if car_rentals:
                    messages.info(self.request, "Someone already rented this car")
                    return render(self.request, "car_rent/car_rental.html", context=ctx)
                else:
                    user.balance -= offer.Deposit
                    car_rental = CarRental.objects.create(customer_id=user, rental_offer_id=offer, is_rented=True)
                    user.save()
                    car_rental.save()

                    return render(request, "car_rent/car_rental_succusfull.html", context=ctx)

            else:
                messages.info(self.request, "You haven't enough cash to pay deposit for car, on your account. ")
                return render(self.request, "car_rent/car_rental.html", context=ctx)
        else:
            messages.info(self.request, "Before renting, please enter your address and payment method")
            return render(self.request, "car_rent/car_rental.html", context=ctx)


def date_counter(date_of_rent):
    """Date Counter when car is returned"""
    today = datetime.date.today()
    time_rent = today - date_of_rent
    return time_rent.days + 1


class ReturnCar(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)

        except RentalOffer.DoesNotExist:
            return HttpResponse("This offer does not exist")

        user = CustomUser.objects.get(id=request.user.id)
        car_rental = CarRental.objects.get(customer_id=user, rental_offer_id=offer, is_rented=True)
        date = datetime.date.today()
        total_price = date_counter(car_rental.date_of_rent) * offer.Price_per_day

        ctx = {"offer": offer, "date": date, 'total_price': total_price}
        return render(request, "car_rent/car_rental_return.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)

        except RentalOffer.DoesNotExist:
            return HttpResponse()


        user = CustomUser.objects.get(id=request.user.id)
        car_rental = CarRental.objects.get(customer_id=user, rental_offer_id=offer, is_rented=True)
        total_price = date_counter(car_rental.date_of_rent) * offer.Price_per_day
        car_rental.is_rented = False
        car_rental.total_price = total_price

        user.balance += offer.Deposit
        user.balance -= total_price

        user.save()
        car_rental.save()

        ctx = {"offer": offer, 'user': user, 'total_price': total_price}
        return render(request, "car_rent/car_rental_return_successful.html", context=ctx)


class CompleteDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCompleteDetails()
        ctx = {"form": form}
        return render(request, "car_rent/account_complete_details.html", context=ctx)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        form = CustomUserCompleteDetails(data=request.POST)
        ctx = {"form": form, "user": user}
        if form.is_valid():
            user.street = form.cleaned_data["street"]
            user.house_number = form.cleaned_data["house_number"]
            user.zip_code = form.cleaned_data["zip_code"]
            user.city = form.cleaned_data["city"]
            user.credit_card_nr = form.cleaned_data["credit_card_nr"]
            user.expiration = form.cleaned_data["expiration"]
            user.CVV = form.cleaned_data["CVV"]
            user.mobile = form.cleaned_data["mobile"]

            user.save(update_fields=["street", "house_number", "zip_code", "city",
                                     "credit_card_nr", 'expiration', 'CVV', 'mobile'])

            ctx['good_message'] = True
            messages.info(self.request, "You finished complete your details")
            return render(request, "car_rent/account_complete_details.html", context=ctx)
        messages.info(self.request, "Phone must be +00 123 345 678")
        return render(request, "car_rent/account_complete_details.html", context=ctx)


class AccountPayment(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = PaymentForm()
        ctx = {'form': form, 'user': user}
        return render(request, "car_rent/account_payment.html", context=ctx)

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['credit_card_nr'] == user.credit_card_nr:
                if authenticate(username=user.email, password=form.cleaned_data['password']):
                    user.balance = user.balance + form.cleaned_data['balance']
                    user.save()
                    messages.info(request, f"Excellent !!! The amount {form.cleaned_data['balance']} has been paid")
                    return render(self.request, "car_rent/account_payment.html",
                                  context={'form': form, 'good_message': True})
                else:
                    messages.info(self.request, 'Password is not correct')
                    return render(self.request, "car_rent/account_payment.html", context={'form': form})

            else:
                messages.info(request, 'Credit card is not correct')
                return render(request, "car_rent/account_payment.html", context={'form': form})
        else:
            messages.info(request, 'Oops, some problem try again or come back later')
            return render(request, "car_rent/account_payment.html", context={'form': form})
