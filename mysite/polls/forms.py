from django import forms

class VoteForm(forms.Form):
    CHOICES = [(1, 'Yes'), (0, 'No')]
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
