import numpy as np
def bian(sound_arry,factor):
    indices=np.round(np.arange(0,len(sound_arry),factor))
    indices=indices[indices<len(sound_arry)].astype(int)
    return sound_arry[indices.astype(int)]