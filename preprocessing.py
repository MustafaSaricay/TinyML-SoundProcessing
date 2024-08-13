from os import walk
from analysis import to_mono
import soundfile as sf
import numpy as np

#This lines will create two matrices for audio names in dataset 
#In these lines it is important to correctly write path of dataset as parameter of walk function
filenames_abnormal = next(walk("..\\archive (1)\\abnormal"), (None, None, []))[2]
filenames_normal = next(walk("..\\archive (1)\\normal"), (None, None, []))[2]


#Decimation method
#For abnormal 
for audio_path in filenames_abnormal:
    audio_8d,sample_rate = sf.read("..\\archive (1)\\abnormal\\"+audio_path)
    audio = to_mono(8,audio_8d)                                                     #Mono conversion
    points = np.arange(1,len(audio),2)                                              #Getting odd indeces
    dec_aud = audio[points]                                                         #keeping only odd indeces
    sf.write("..\\dataset_decimated\\abnormal\\"+audio_path,dec_aud,sample_rate)

#For normal
for audio_path in filenames_normal:
    audio_8d,sample_rate = sf.read("..\\archive (1)\\normal\\"+audio_path)
    audio = to_mono(8,audio_8d)                     
    points = np.arange(1,len(audio),2)
    dec_aud = audio[points]
    sf.write("..\\dataset_decimated\\normal\\"+audio_path,dec_aud,sample_rate)
    

#Lowpass filtering

filter = [-0.023843401827792862, -0.016680281485447243, 0.037367268070131514, 0.134655108680450136, 0.231982032564785584,
           0.273038547995745617, 0.231982032564785584, 0.134655108680450136, 0.037367268070131514, -0.016680281485447243,
          -0.023843401827792862]        #Fir lowpass filter created from fiir.com

#For abnormal 
for audio_path in filenames_abnormal:
    audio_8d,sample_rate = sf.read("..\\archive (1)\\abnormal\\"+audio_path)       
    audio = to_mono(8,audio_8d)                                                    #Mono conversion
    filt_aud = np.convolve(audio,filter)                                           #filter appliance
    sf.write("..\\dataset_filtered\\abnormal\\"+audio_path,filt_aud,sample_rate)
   
#For normal 
for audio_path in filenames_normal:
    audio_8d,sample_rate = sf.read("..\\archive (1)\\normal\\"+audio_path)
    audio = to_mono(8,audio_8d)
    filt_aud = np.convolve(audio,filter)
    sf.write("..\\dataset_filtered\\normal\\"+audio_path,filt_aud,sample_rate)
    