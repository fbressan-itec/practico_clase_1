from django import forms
from .models import Spot

class SpotForm(forms.ModelForm):

    class Meta:
        model = Spot
        fields = [
            "numero",
            "estado",
            "responsable",
            "vehiculo"
            ]
    
    # aplicamos estilos a los campos del form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border border-gray-300 rounded-xl p-2.5 bg-slate-50 focus:border-orange-400',
                'placeholder': f'Ingrese {field.label.lower()}',
            })

