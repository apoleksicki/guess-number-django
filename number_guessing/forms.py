'''
Created on 02/10/2013

@author: Antek
'''
from django import forms

class GuessForm(forms.Form):
    def __init__(self, *args, **kwargs):
        num_choices = kwargs.pop('num_choices')
        super(GuessForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.TypedChoiceField(coerce=int,
                                                       widget=forms.RadioSelect,
                                                       choices=[(str(x), str(x)) for x in xrange(num_choices)],
                                                       error_messages={'required': 'Please select a number'},
                                                       label='Make your guess:')
