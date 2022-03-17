from wtforms import Form, StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import Length, EqualTo, NumberRange, Regexp, URL, UUID, ValidationError, InputRequired


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message='用戶名長度需3~10')])
    password = StringField(validators=[Length(min=6, max=10, message='密碼長度需6~10')])
    password_repeat = StringField(validators=[Length(min=3, max=10, message='密碼需相同'), EqualTo('password')])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(12, 100)])
    # phone = StringField(validators=[Regexp(r'1[38745]\d{9}')])
    # homepage = StringField(validators=[URL()])
    # uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(4,4)])
    def validate_captcha(self,field):
        if field.data != '1234':
            raise ValidationError('驗證碼錯誤')

class SettingsForm(Form):
    username = StringField("用户名：",validators=[InputRequired()])
    age = IntegerField("年龄：",validators=[NumberRange(10,100)])
    remember = BooleanField('记住我：')
    tags = SelectField('标签',choices=[('1','python'),('2','ios')])