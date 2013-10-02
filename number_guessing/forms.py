'''
Created on 02/10/2013

@author: Antek
'''
from django import forms

class GuessForm(forms.Form):
    choice = forms.TypedChoiceField(coerce = int, 
                                    widget = forms.RadioSelect, 
                                    choices = [(str(x), str(x)) for x in xrange(5)], 
                                    error_messages={'required': 'Please select a number'})
    