from django import forms
from askPupkin_models.models import Answer

class AddAnswerForm(forms.Form):
    answer = forms.CharField(
        label='Краткое описание',
        required=True,
        initial='',
        widget=forms.Textarea( 
            attrs = {
                'class': 'form-control fs-5',
                'rows': '5'
            }
        )
    )

    def create_answer(self, request, question_id):
        if self.is_valid():
            text = self.cleaned_data["answer"]
            author = request.user.profile
            answer = Answer.objects.create(content=text, author=author, question_id=question_id)
            return True