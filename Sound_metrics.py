# Add MOSQITO to the Python path
import sys
sys.path.append('..')

# Import numpy
import numpy as np
# Import plot function
import matplotlib.pyplot as plt
# Import spectrum computation tool
from scipy.fft import fft, fftfreq
# Import mosqito functions
from mosqito.utils import load
from mosqito.sq_metrics import loudness_zwst
from mosqito.sq_metrics import loudness_zwst_perseg
from mosqito.sq_metrics import loudness_zwst_freq
from mosqito.sq_metrics import roughness_dw, roughness_dw_freq
from mosqito.sq_metrics import loudness_zwst_perseg
from mosqito.sq_metrics import sharpness_din_st
from mosqito.sq_metrics import sharpness_din_perseg
from mosqito.sq_metrics import sharpness_din_from_loudness
from mosqito.sq_metrics import sharpness_din_freq
from  scipy.io import wavfile 
import soundfile as sf
# Import MOSQITO color sheme [Optional]
from mosqito import COLORS

path = "audio_ver1.wav"

sig, fs = load(path, wav_calib=2 * 2 **0.5)

t = np.linspace(0, (len(sig) - 1) / fs, len(sig))
plt.figure(1)
plt.plot(t, sig * 0.05, color=COLORS[0])
plt.xlabel('Time [s]')
plt.ylabel('Acoustic pressure [Pa]')
plt.show()
N, N_specific, bark_axis = loudness_zwst(sig * 0.05, fs, field_type="free")
r, r_spec, bark, time = roughness_dw(sig * 0.05, fs, overlap=0)
sharpness = sharpness_din_st(sig, fs, weighting="din")
print("Sharpness = {:.1f} acum".format(sharpness) )
print("N_zwst = {:.1f} sone".format(N))
plt.figure(2)
plt.plot(time, r, color=COLORS[0])
plt.ylim(0,1.1)
plt.xlabel("Time [s]")
plt.ylabel("Roughness [Asper]")
plt.show()

output_file_path = "output_audio1.wav"
sf.write(output_file_path, np.array(sig) * 0.05, fs)