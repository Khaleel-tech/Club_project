from django import forms
from .models import Student

from django import forms
from .models import Student

class InitialStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'role', 'training_type']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'training_type': forms.Select(attrs={'class': 'form-select'}),
        }

class CompleteProfileForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [
            'name', 'mobile_number', 'email', 'branch', 'year',
            'residence', 'girls_hostel', 'hostel_boys_campus',
            'hostel_boys_in_campus', 'hostel_boys_outside_campus',
            'transport', 'bus_route', 'date_of_birth', 'gender',
            'cluster', 'country', 'state', 'password'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'residence': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'cluster': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'girls_hostel': forms.Select(attrs={'class': 'form-select'}),
            'hostel_boys_campus': forms.Select(attrs={'class': 'form-select'}),
            'hostel_boys_in_campus': forms.Select(attrs={'class': 'form-select'}),
            'hostel_boys_outside_campus': forms.Select(attrs={'class': 'form-select'}),
            'transport': forms.Select(attrs={'class': 'form-select'}),
            'bus_route': forms.Select(attrs={'class': 'form-select'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        residence = cleaned_data.get('residence')
        gender = cleaned_data.get('gender')
        transport = cleaned_data.get('transport')
        
        # Validate hostel-related fields
        if residence == 'Hostel':
            if gender == 'Female' and not cleaned_data.get('girls_hostel'):
                self.add_error('girls_hostel', 'This field is required for female hostel residents')
            elif gender == 'Male':
                if not cleaned_data.get('hostel_boys_campus'):
                    self.add_error('hostel_boys_campus', 'This field is required for male hostel residents')
                
        # Validate transport-related fields
        if residence == 'Day Scholar':
            if not cleaned_data.get('transport'):
                self.add_error('transport', 'This field is required for day scholars')
            if transport == 'College Bus' and not cleaned_data.get('bus_route'):
                self.add_error('bus_route', 'This field is required for college bus users')
                
        return cleaned_data

class StudentForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices=Student.Role_choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_role'
        })
    )

    class Meta:
        model = Student
        fields = [
            'username', 
            'name', 
            'mobile_number', 
            'password',
            'email',
            'role',
            'branch', 
            'year', 
            'training_type',
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'training_type': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise forms.ValidationError("Enter a valid 10-digit mobile number.")
        return mobile_number



from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # role = forms.ChoiceField(choices=[
    #     ("Student", "Student"),
    #     ("Super Admin", "Super Admin"),
    #     ("Club incharge", "Club Incharge"),
    #     ("Report Manager", "Report Manager"),
    # ], label="Role", widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=128, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

