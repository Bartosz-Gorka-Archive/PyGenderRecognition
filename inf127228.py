import sys                          # Fetch argv from system
import soundfile                    # Read sound file
from scipy import fft               # FFT
import matplotlib.pyplot as plt     # Plot


def main():
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

        # Show plot
        plt.plot(fft_abs)
        plt.show()
        
    else:
        print('>> LOOSER << You mast set filename as parameter')


if __name__ == '__main__':
    main()
