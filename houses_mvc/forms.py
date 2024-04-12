from django import forms


class MultistoreyBuildingForm(forms.Form):
    fias_code = forms.CharField(max_length=50)
    wall_material = forms.CharField(max_length=50)
    year_built = forms.IntegerField(widget=forms.NumberInput())
    area = forms.FloatField()
    apartments_count = forms.IntegerField(widget=forms.NumberInput())

    def check_area(self):
        input_area = self.cleaned_data["area"]
        return 0 <= input_area <= 10000
