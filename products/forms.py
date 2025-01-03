from django import forms
from .models import Review, Product, Category, Order

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'max': 5,
                    'step': 0.1,
                    'placeholder': 'Please rate us (1 to 5)',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Please comment here...',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' mb-3'

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['courseName', 'instructor', 'courseUrl', 'imageUrl', 'description', 'category', 'rating', 'reviews', 'duration', 'lectures', 'level', 'price', 'students']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Course description'}),
            'price': forms.NumberInput(attrs={'min': 0}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['courseName', 'instructor', 'courseUrl', 'imageUrl', 'description', 'category', 'rating', 'reviews', 'duration', 'lectures', 'level', 'price', 'students']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Course description'}),
            'price': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=[
                ('Pending', 'Pending'),
                ('Completed', 'Completed'),
                ('Cancelled', 'Cancelled'),
            ])
        }