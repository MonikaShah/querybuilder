from django import forms
 
class SearchForm(forms.Form):
    d = forms.ModelChoiceField(
                queryset=School1617Codes.objects.values_list('distname'), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getBlock()'})
                )
 
    b = forms.ModelChoiceField(
                queryset=School1617Codes.objects.values_list('block_name'), 
                empty_label='Not Specified'
                )