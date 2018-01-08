import sys              # Fetch argv from system
import soundfile        # Read sound file
from scipy import fft   # FFT


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

        print(fft_signal)
    else:
        print('>> LOOSER << You mast set filename as parameter')


if __name__ == '__main__':
    main()
