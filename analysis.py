import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from numpy import fft as dft        #Too lazy to use np.fft.fft() so i will write dft.fft() 
#soundfile library for .wav file processing 

def to_mono(channel_number, audio): #this function sums of channels in given audio channel_number is number of channels of the audio
    return np.dot(audio,np.ones(channel_number))/2
    
#frequency domain x axis in Hz
freq = np.linspace(-7999,8000,160000)

# Load audio file
test1, sample_rate = sf.read('abnormal3.wav')
test3, sample_rate = sf.read('abnormal4.wav')
test2, sample_rate = sf.read('normal3.wav')
test4, sample_rate = sf.read('normal4.wav')

#lowpass filter 
filter = [-0.023843401827792862, -0.016680281485447243, 0.037367268070131514, 0.134655108680450136, 0.231982032564785584,
           0.273038547995745617, 0.231982032564785584, 0.134655108680450136, 0.037367268070131514, -0.016680281485447243,
          -0.023843401827792862]

#Sample rate is equal to 16000 in our current dataset and it is 8 channel audio so to change it to mono we will take average of channels
test1 = to_mono(8,test1)
test2 = to_mono(8,test2)
test3 = to_mono(8,test3)
test4 = to_mono(8,test4)

test1 = np.convolve(test1,filter)
test2 = np.convolve(test2,filter)
test3 = np.convolve(test3,filter)
test4 = np.convolve(test4,filter)

#fft's uncomment to use
# test1_fft = dft.fftshift(abs(dft.fft(test1)))
# test3_fft = dft.fftshift(abs(dft.fft(test3)))
# test2_fft = dft.fftshift(abs(dft.fft(test2)))
# test4_fft = dft.fftshift(abs(dft.fft(test4)))

# #plotting uncomment to see plots
# fig = plt.figure()

# plt.subplot(2, 2, 1)
# plt.plot(freq,test1_fft)
# plt.title("abnormal_3")

# plt.subplot(2, 2, 2)
# plt.plot(freq,test2_fft)
# plt.title("normal_3")

# plt.subplot(2, 2, 3)
# plt.plot(freq,test3_fft)
# plt.title("abnormal_4")

# plt.subplot(2, 2, 4)
# plt.plot(freq,test4_fft)
# plt.title("normal_4")

# plt.show()

#Spectogram plots , uncomment to use
# fig = plt.figure()
# plt.subplot(2, 2, 1)
# plt.specgram(test1,1024,16000)
# plt.title("abnormal_3")

# plt.subplot(2, 2, 2)
# plt.specgram(test2,1024,16000)
# plt.title("normal_3")

# plt.subplot(2, 2, 3)
# plt.specgram(test3,1024,16000)
# plt.title("abnormal_4")

# plt.subplot(2, 2, 4)
# plt.specgram(test4,1024,16000)
# plt.title("normal_4")

# plt.show()

