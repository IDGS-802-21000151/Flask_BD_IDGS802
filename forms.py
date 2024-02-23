from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre = StringField("Ingresa el nombre", [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    primerApellido = StringField("Ingresa el primer apellido")
    segundoApellido = StringField("Ingresa el segundo apellido")
    edad = IntegerField("Ingresa tu edad", [
        validators.number_range(min=1, max=20, message="Valor no valido")
    ])
    correo = EmailField("Ingresa tu correo", {
        validators.Email(message="Ingresa un correo valido")
    })
    
class DiccionarioForm(Form):
    palabraIngles = StringField("Palabra en ingles", [
        validators.DataRequired(message="El campo palabra ingles es requerido")
    ])
    palabraEspaniol = StringField("Palabra en español", [
        validators.DataRequired(message="El campo palabra español es requerido")
    ])
    
class consultarForm(Form):
    palabraTraducir = StringField("Ingresa la palabra a traducir", [
        validators.DataRequired(message="El campo palabra a traducir es requerido")
    ])
    idiomaConsultar = RadioField("Selecciona idioma a consultar", choices=[('1', 'Ingles'), ('0', 'Español')], default='1')