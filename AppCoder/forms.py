from django import forms

class AutosFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    motor = forms.FloatField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    encargo = forms.CharField()

# class UsuarioFormulario(forms.Form):

#     email = forms.EmailField()
#     contra1 = forms.CharField(label = 'Contrasena', widget= forms.PasswordInput)
#     contra2 = forms.CharField(label = 'Repita la contrasena', widget= forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email','contra1','contra2']
     
    