from django.conf import settings
from django import forms
from django.db import models


# Create your models here.
# class Store(models.Model):
#     choices = (('g','grocery'),
#     ('i','equipment'),
#     ('s','sport'))
#     name = models.CharField(max_length=25)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=2)
#     options = models.CharField(max_length=5 ,choices=choices)

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         ordering = ['-city']



class Contact(models.Model):
    name = models.CharField(max_length=25,blank=True)
    email = models.EmailField(default='null@gmail.com')
    comment = models.CharField(max_length=250)

    class Meta:
        default_permissions=('add',)
        permissions = (('can comment','user can comment'),('can edit','usr can edit comment'))

    def __str__(self) -> str:
        return self.name

 
def validate_comment(value):
        if len(value)<5:
            raise forms.ValidationError('comment should be more than 5 characters')

def validate_age(value):
    if value < 18:
        raise forms.ValidationError('you have to be up to 18 to comment')

class ContactForm(forms.ModelForm):
    age = forms.IntegerField(validators=[validate_age])
    comment = forms.CharField(widget=forms.Textarea,validators=[validate_comment])
    class Meta:
        model = Contact
        fields = '__all__'
        help_texts = {
            'comment':'provide details of yoyr issue here'
        }
        labels = {
            'comment':'issue'
        }

        localized_fields=  ['comment']


# class StoreForm(forms.ModelForm):
   
#     class Meta:
#         model = Store()
#         fields='__all__'

