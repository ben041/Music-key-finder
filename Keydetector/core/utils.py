import librosa
import numpy as np
from .models import AudioFile

class AudioAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.waveform = None
        self.sr = None
        self.load_audio()
        
    def load_audio(self):
        try:
            self.waveform, self.sr = librosa.load(self.file_path)
        except Exception as e:
            raise Exception(f"Error loading audio file: {str(e)}")
            
    def analyze(self):
        analyzer = Tonal_Fragment(self.waveform, self.sr)
        
        return {
            'key': analyzer.key,
            'correlation': analyzer.bestcorr,
            'alternative_key': analyzer.altkey,
            'alternative_correlation': analyzer.altbestcorr,
            'chroma_values': analyzer.chroma_vals
        }

class Tonal_Fragment:
    def __init__(self, waveform, sr):
        self.waveform = waveform
        self.sr = sr
        self.chroma_vals = self.get_chroma_values()
        self.key, self.bestcorr, self.altkey, self.altbestcorr = self.detect_key()
    
    def get_chroma_values(self):
        chromograph = librosa.feature.chroma_cqt(y=self.waveform, sr=self.sr, bins_per_octave=24)
        return [np.sum(chromograph[i]) for i in range(12)]

    def detect_key(self):
        maj_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        min_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
        pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        best_key = None
        best_corr = -1
        alt_key = None
        alt_corr = -1

        for i in range(12):
            rotated_chroma = [self.chroma_vals[(i + j) % 12] for j in range(12)]
            maj_corr = np.corrcoef(maj_profile, rotated_chroma)[1, 0]
            min_corr = np.corrcoef(min_profile, rotated_chroma)[1, 0]
            
            for key, corr in [(pitches[i] + ' Major', maj_corr), (pitches[i] + ' Minor', min_corr)]:
                if corr > best_corr:
                    alt_key, alt_corr = best_key, best_corr
                    best_key, best_corr = key, corr
                elif corr > alt_corr:
                    alt_key, alt_corr = key, corr

        return best_key, best_corr, alt_key, alt_corr
