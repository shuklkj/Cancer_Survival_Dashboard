# from django.shortcuts import render
# import pandas as pd
# import json

# def cancer_types_view(request):
#     # Load your data - this should be the path to your .csv file
#     cancer_data = pd.read_csv("/Users/kajalshukla/Documents/UCHICAGO/Quarter-4/DS in Healthcare/healthcare/Assignment_2/cancer_analysis_project/cancer_analysis_data.csv")

#     cancer_type_counts = cancer_data['cancer_type'].value_counts().to_dict()

#     # Convert the data to JSON to pass to the template
#     chart_data = json.dumps(list(cancer_type_counts.items()), ensure_ascii=False)

#     # Get unique cancer types
#     unique_cancer_types = cancer_data['cancer_type'].unique()
    
#     # Combine 'chart_data' and 'cancer_types' into one context dictionary
#     context = {
#         'chart_data': chart_data,
#         'cancer_types': unique_cancer_types,
#     }
    
#     return render(request, 'charts_app/cancer_types.html', context)

from django.shortcuts import render
import pandas as pd
import json

# Assuming 'final_data' is already loaded and available for views
# This should ideally be placed outside the view functions if it's large and static,
# so it's only loaded once when the module is imported.
final_data = pd.read_csv("/Users/kajalshukla/Documents/UCHICAGO/Quarter-4/DS in Healthcare/healthcare/Assignment_2/cancer_analysis_project/cancer_analysis_data.csv")

def cancer_types_view(request):
    # Calculate the cancer type counts
    cancer_type_counts = final_data['cancer_type'].value_counts().to_dict()

    # Convert the data to JSON to pass to the template
    cancer_chart_data = json.dumps(list(cancer_type_counts.items()), ensure_ascii=False)
    
    context = {
        'chart_data': cancer_chart_data,
        'cancer_types': final_data['cancer_type'].unique(),
    }
    
    return render(request, 'charts_app/cancer_types.html', context)

def censoring_data_view(request):
    # Calculate the censor counts
    censor_counts = final_data['censored'].value_counts().to_dict()

    # Prepare the data for the pie chart
    censor_chart_data = {
        'labels': ['Not Censored (Event Observed)', 'Censored (Alive or Lost to Follow-up)'],
        'data': [censor_counts.get(False, 0), censor_counts.get(True, 0)]
    }

    # Convert the data to JSON to pass to the template
    censor_chart_data_json = json.dumps(censor_chart_data)

    # The key 'chart_data' is expected in the template
    context = {
        'chart_data': censor_chart_data_json,
    }

    return render(request, 'charts_app/censoring_data.html', context)
