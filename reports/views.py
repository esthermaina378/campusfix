from django.shortcuts import render

def home(request):
    return render(request, 'reports/index.html')


def report_issue(request):
    return render(request, 'reports/report.html')


def view_reports(request):
    return render(request, 'reports/reports.html')
