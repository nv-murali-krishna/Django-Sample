from django import  forms
from fifthapp.models import student

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','roll','branch','year','email','password']

    def clean_student(self, *args, **kwargs):
        #run the standard clean method first
        inputdata = self.cleaned_data.get('student')
        print('validating form')


        return inputdata
