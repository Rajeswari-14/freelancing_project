from django.shortcuts import render
from sklearn.naive_bayes import GaussianNB
from .models import ClientRequest
import numpy as np
def index(request):
    return render(request, 'freelance_app/index.html')
def budget_prediction(request):
    if request.method == 'POST':
        # Get inputs from the form
        project_complexity = float(request.POST['project_complexity'])
        project_duration = float(request.POST['project_duration'])
        # Combine features into a 2D array for the model
        features = np.array([[project_complexity, project_duration]])
        # Sample training data (replace with real data in a production system)
        model = GaussianNB()
        X_train = np.array([[1, 2], [3, 4], [5, 6], [8, 12], [10, 20]])  # Example data
        y_train = np.array([100, 300, 500, 1000, 2000])  # Example budget values
        model.fit(X_train, y_train)
        # Predict budget based on user input
        predicted_budget = model.predict(features)
        client_request = ClientRequest(
            name=request.POST.get('name', 'Client Name'),  # Using default value if name is not provided
            project_complexity=project_complexity,
            project_duration=project_duration,
            predicted_budget=predicted_budget[0]
        )
        client_request.save()
        # Render the result
        return render(request, 'freelance_app/result.html', {'budget': predicted_budget[0]})
    # Render the input form if not POST
    return render(request, 'freelance_app/form.html')
