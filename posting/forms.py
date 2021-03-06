from django import forms
from .models import Contact, Subscribe, Commentaire, Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "level", "status","img_link", "intro",  "body"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class":"form-control mb-3",
        })

        self.fields['title'].label = "Titre du Cour "
        self.fields['level'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['level'].label = "Le Niveau"
        self.fields['status'].widget.attrs.update({
            "class":"form-control mb-3",
        })


        self.fields['intro'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['intro'].label = "Petite intro"

        self.fields['img_link'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['img_link'].label = "URL de d'un Image "
        

        self.fields['body'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['body'].label = "Le Corps du Cour "
class ContanctForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NewLetter(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "placeholder":"votre nom",
            'class':"btmspace-15",
        })
        self.fields['email'].widget.attrs.update({
            "placeholder":"votre email",
            'class':"btmspace-15",
        })


class CommentsForms(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['comments']

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comments"].widget.attrs.update({
            "id":"comments",
        })
