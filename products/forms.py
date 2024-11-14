from django import forms
from .models import Review, Product, Category

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['courseName', 'instructor', 'courseUrl', 'imageUrl', 'description', 'category', 'rating', 'reviews', 'duration', 'lectures', 'level', 'price', 'students']
        
        # Optional: Add custom widgets for better UI
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Course description'}),
            'price': forms.NumberInput(attrs={'min': 0}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom placeholders or CSS classes if necessary
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['courseName', 'instructor', 'courseUrl', 'imageUrl', 'description', 'category', 'rating', 'reviews', 'duration', 'lectures', 'level', 'price', 'students']
        
        # Optional: Add custom widgets for better UI
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Course description'}),
            'price': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom placeholders or CSS classes if necessary
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']  # We will allow the admin to edit the status of the order
        widgets = {
            'status': forms.Select(choices=[
                ('Pending', 'Pending'),
                ('Completed', 'Completed'),
                ('Shipped', 'Shipped'),
                ('Cancelled', 'Cancelled'),
            ])
        }