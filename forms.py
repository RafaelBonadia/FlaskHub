from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('User namee', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Create an account')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('This email already exist, try another one')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Remember data')
    botao_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Profile update', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_powerbi = BooleanField('Power BI')
    curso_python = BooleanField('Python')
    curso_ppt = BooleanField('Apresentations')
    curso_sql = BooleanField('SQL')
    botao_submit_editarperfil = SubmitField('Confirm edition')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('This email already exist, try another one.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Post title', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Write your post here', validators=[DataRequired()])
    botao_submit = SubmitField('Create a post')