import sys                              # Fetch argv from system
import warnings                         # Warnings
import soundfile                        # Read sound file
from scipy import fft                   # FFT
import matplotlib.pyplot as plt         # Plot
from scipy.signal import decimate       # Decimate - FFT signal
from scipy.fftpack import fftfreq       # FFT frequences

# Disable warnings in code
warnings.filterwarnings("ignore")

def main():
    thresh = 700

    # Check filename in argv
    if len(sys.argv) > 1:
        # Read file
        signal, sample_rate = soundfile.read(sys.argv[1], dtype='int16')

        # Eliminate file to only one dimension
        if len(signal.shape) == 2:
            signal = [s[0] for s in signal]

        # FFT
        fft_signal = signal.copy()
        fft_signal = fft(fft_signal)

        # Reduce data to first half
        fft_half = fft_signal[1 : int(len(fft_signal) / 2)]

        # ABS
        fft_abs = fft_half.copy()
        fft_abs = abs(fft_abs) * 2 / len(signal)

        # Prepare decimate from fft signal
        decimate_2 = fft_abs.copy()
        decimate_2 = decimate(decimate_2, 2, n = 8)

        decimate_3 = fft_abs.copy()
        decimate_3 = decimate(decimate_3, 3, n = 8)

        decimate_4 = fft_abs.copy()
        decimate_4 = decimate(decimate_4, 4, n = 8)

        decimate_5 = fft_abs.copy()
        decimate_5 = decimate(decimate_5, 5, n = 8)

        # Calculate length of shortest decimate result
        decimate_len = len(decimate_5)

        # Merge results
        result = fft_abs[:decimate_len] * decimate_2[:decimate_len] * decimate_3[:decimate_len] * decimate_4[:decimate_len] * decimate_5[:decimate_len]

        # Clear data
        result[0 : 100] = 0

        maxAmp = max(result)
        check = 0
        for i in range(len(result)):
            if result[i] == maxAmp:
                check = i
                break

        if check > thresh:
            print('F')
        else:
            print('M')

    else:
        print('>> LOOSER << You mast set filename as parameter')


if __name__ == '__main__':
    main()
