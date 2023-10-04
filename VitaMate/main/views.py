from django.shortcuts import render, redirect
from django.db import connection
from .models import Pressure_Data
from .forms import Pressure_Data_form

def index(request):
    if request.method == 'POST':
        form = Pressure_Data_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Pressure_Data_form()

    pale_data = Pressure_Data.objects.all().order_by('date')
    for item in pale_data:
        print(item.__dict__)

    req = {
        'form': form
    }

    query = """
        SELECT date, AVG(systolic_pressure * 1/3 + diastolic_pressure * 2/3) AS avg_pressure
        FROM main_pressure_data
        GROUP BY date;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    data_list = [{'date': row[0], 'average_pressure': round(row[1])} for row in sorted(data, key=lambda x: x[0])]
    return render(request, 'main/template.html', {'data': data_list, 'pale_data': pale_data, 'form': form})
