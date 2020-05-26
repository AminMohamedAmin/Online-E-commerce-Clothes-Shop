from django import forms

class CouponApplyForm(forms.Form):
	# TODO: Define form fields here
	code = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
		}
	))