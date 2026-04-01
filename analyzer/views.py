from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ml_model import analyze_resume

@login_required
def upload_resume(request):
    if request.method == 'POST':
        file = request.FILES.get('resume')

        if not file:
            return render(request, 'analyzer/upload.html', {
                'error': 'Please upload a file'
            })

        score, skills, jobs, chart, suggestions = analyze_resume(file)

        return render(request, 'analyzer/result.html', {
            'score': score,
            'skills': skills,
            'jobs': jobs,
            'chart': chart,
            'suggestions': suggestions
        })

    return render(request, 'analyzer/upload.html')


