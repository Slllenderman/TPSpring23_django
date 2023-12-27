from django import forms
from askPupkin_models.models import Question, Tag
from django.core.exceptions import ValidationError

class AddQuestionForm(forms.Form):
    name = forms.CharField(
        label='Название вопроса',
        required=True,
        widget=forms.TextInput( 
            attrs = {
                'class': 'form-control fs-5'
            }
        )
    )
    short_description = forms.CharField(
        label='Краткое описание',
        required=True,
        widget=forms.Textarea( 
            attrs = {
                'class': 'form-control fs-5',
                'rows': '5',
                'maxlenght':'300'
            }
        )
    )
    description = forms.CharField(
        label='Полное описание',
        required=True,
        widget=forms.Textarea( 
            attrs = {
                'class': 'form-control fs-5',
                'rows': '10'
            }
        )
    )
    tags = forms.CharField(
        label='Тэги',
        required=True,
        widget=forms.TextInput( 
            attrs = {
                'class': 'form-control fs-5',
                'pattern': '([a-z]{2,7},?\s*)+'
            }
        )
    )

    def add_question(self, request):
        if self.is_valid():
            name = self.cleaned_data["name"]
            short_description = self.cleaned_data["short_description"]
            description = self.cleaned_data["description"]
            tags = self.cleaned_data["tags"].split(',')
            author = request.user.profile
            if len(short_description) >= 300:
                self.fields['short_description'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                self.add_error("short_description", ValidationError("Длина краткого описания не должна превышать 300 символов"))
                return None
            question = Question.objects.create(title=name, description=short_description, content=description, author=author)
            for tagname in tags:
                tag = Tag.objects.get_or_create(name=tagname)[0]
                question.tags.add(tag.id)
            return question.id
            