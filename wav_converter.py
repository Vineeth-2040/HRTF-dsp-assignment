# This file takes a WAV file, converts it into a .h array, and saves it
# in the same directory with the same name but with a .h extension.
from pydub import AudioSegment
import wave
import numpy as np      
import os



# Take a WAV file, cut 2 seconds from it, and save the cut audio.
def cut_wav(wav_file, output_file='2_sec_1.wav', start_ms=2000, duration_ms=2000):
    audio = AudioSegment.from_wav(wav_file)
    audio=audio.set_frame_rate(44100).set_channels(1)
    audio=audio.normalize()
    end_ms = min(start_ms + duration_ms, len(audio))
    audio[start_ms:end_ms].export(output_file, format='wav')
    return output_file



def wav_to_header(wav_file):
    # Open the WAV file
    with wave.open(wav_file, 'rb') as wav:
        # Get parameters
        n_channels = wav.getnchannels()
        n_frames = wav.getnframes()
        sample_width = wav.getsampwidth()
        
        # Read audio data
        audio_data = wav.readframes(n_frames)
        
        # Convert audio data to numpy array
        if sample_width == 1:  # 8-bit audio
            audio_array = np.frombuffer(audio_data, dtype=np.uint8) - 128
        elif sample_width == 2:  # 16-bit audio
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
        else:
            raise ValueError("Unsupported sample width: {}".format(sample_width))
        
        # Create header file name
        header_file = os.path.splitext(wav_file)[0] + '.h'
        
        # Write to header file
        with open(header_file, 'w') as header:
            header.write('#ifndef AUDIO_DATA_H\n')
            header.write('#define AUDIO_DATA_H\n\n')
            header.write('#include <stdint.h>\n\n')
            header.write('const int16_t audio_data[] = {\n')
            for i in range(len(audio_array)):
                header.write('    {},\n'.format(audio_array[i]))
            header.write('};\n\n')
            header.write('#endif // AUDIO_DATA_H\n')
        return header_file


if __name__ == '__main__':
    input_file = 'sample_audio.wav'
    wav_to_header(input_file)
    print(os.path.getsize(input_file))

    cut_file = cut_wav(input_file)
    wav_to_header(cut_file)
    print(os.path.getsize(cut_file))
