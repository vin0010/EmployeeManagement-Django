from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		#fields generates a list of all editable fields of Student model
		fields = [f.name for f in Student._meta.get_fields() if not f.name in ["created","modified"]]
