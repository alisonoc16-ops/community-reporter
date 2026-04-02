from django.shortcuts import render
from django.shortcuts import render
import uuid

# Create your views here.
def home_view(request):
    # This view shows the home screen with the 4 category tiles
    return render(request, 'home.html')

def submit_report_view(request):
    # This view handles the report submission form
    ref_number = None
    
    if request.method == 'POST':
        # When the form is submitted, generate a unique reference number
        # uuid4() creates a random unique ID, we take the first 8 characters
        ref_number = 'KIM-' + str(uuid.uuid4())[:8].upper()
    
    # Pass the ref_number to the template (it will be None if not submitted yet)
    return render(request, 'submit_report.html', {
        'ref_number': ref_number,
        'category': request.GET.get('category', 'Issue')
    })