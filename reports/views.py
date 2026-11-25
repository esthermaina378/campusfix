from django.shortcuts import render, redirect
from .models import Report

def home(request):
    return render(request, 'reports/index.html')


def report_issue(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')

        Report.objects.create(
            title=title,
            category=category,
            location=location,
            description=description
        )

        return redirect('reports')

    return render(request, 'reports/report.html')


def view_reports(request):
    reports = Report.objects.all().order_by('-date_reported')
    return render(request, 'reports/reports.html', {'reports': reports})