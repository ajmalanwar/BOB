from django import forms
from .models import UserForm, Branch


class Form(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'material_provided': forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id=int(self.data.get('district'))
                self.fields['branch'].queryset=Branch.objects.filter(district_id=district_id).order_by()
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset=self.instance.district.branch_set.order_by('name')

