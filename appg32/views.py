import os  # Add this line to import the os module

from django.shortcuts import render, HttpResponseRedirect
from .forms import DatasetUploadForm  # Make sure to import your form if not already imported
from django.conf import settings

def landing_page(request):
    return render(request, 'landing_page.html')

def upload_data(request):
    # Handle GET request to render the upload form
    if request.method == 'GET':
        return render(request, 'upload_form.html')

    # Handle POST request to process the uploaded data
    elif request.method == 'POST':
        # Process the uploaded data here
        # This could involve validating the data, saving it to the database, etc.
        # Redirect the user to a different page after processing the data
        return HttpResponseRedirect('/success/')  # Redirect to a success page

def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset_file = form.cleaned_data['dataset']
            file_path = os.path.join(settings.MEDIA_ROOT, dataset_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in dataset_file.chunks():
                    destination.write(chunk)
            return HttpResponseRedirect('/dataset-success/')
        else:
            return render(request, 'upload_dataset_form.html', {'form': form})
    else:
        form = DatasetUploadForm()
        return render(request, 'upload_dataset_form.html', {'form': form})

def explore_datasets(request):
    # Your logic for exploring datasets goes here
    return render(request, 'explore_datasets.html')


def upload_success(request):
    return render(request, 'upload_success.html')