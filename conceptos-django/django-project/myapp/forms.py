from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField( label="Task Title", max_length=200, required=True )
    description = forms.CharField( label="Task Description", widget=forms.Textarea )

class CreateNewProject( forms.Form ):
    name = forms.CharField( label="Project Name", max_length=200, required=True )
    