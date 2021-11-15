# -*- coding: utf-8 -*-
#%%
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
#%%
def get_frequency(note,octave):
    expo = (octave- 4 ) * 12 + (note-10)
    return 440*((2**(1/12)) ** expo)
#%%
def set_wave(dur, amp, note, octa):
    sr = 44100
    t = np.linspace(0,dur/1000,int(sr*dur/1000))
    freq = get_frequency(note,octa) #440hz
    wave = amp*(np.sin(2*np.pi * freq * t))
    plt.scatter(freq, amp)
    return wave
#%%
def sinfonia(long):
    l = long
    waves = (set_wave(dur = np.random.randint(100,3000), amp= np.random.random(), note = np.random.randint(1,36), octa = 3) for n in range(l))
    for w in waves:
        print(w)
        sd.play(w, 44100)
        sd.wait()
#%%