from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .models import AudioFile
from .forms import AudioFileForm
from .utils import AudioAnalyzer
from django.urls import reverse_lazy

class AudioUploadView(CreateView):
    model = AudioFile
    form_class = AudioFileForm
    template_name = 'upload.html'
    success_url = reverse_lazy('audio_analyzer:result')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        try:
            analyzer = AudioAnalyzer(self.object.file.path)
            results = analyzer.analyze()
            
            self.object.key = results['key']
            self.object.correlation = results['correlation']
            self.object.alternative_key = results['alternative_key']
            self.object.alternative_correlation = results['alternative_correlation']
            self.object.save()
            
        except Exception as e:
            self.object.delete()
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
        return response

class ResultView(DetailView):
    model = AudioFile
    template_name = 'result.html'
    context_object_name = 'audio_file'
    
    def get_object(self):
        return AudioFile.objects.latest('uploaded_at')
