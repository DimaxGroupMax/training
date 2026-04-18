import re
from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ('0', 'False'),
            ('1', 'True'),
        ]
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices = [
            ('0', 'False'),
            ('1', 'True'),
        ]
    )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        # Регулярное выражение уже проверяет и наличие +, и количество цифр (от 10 до 12)
        pattern = re.compile(r'^\+?[0-9]{9,12}$')

        if not pattern.match(data):
            raise forms.ValidationError('Неверный формат номера. Допустимы только цифры и "+" (от 9 до 12 знаков)')

        return data



