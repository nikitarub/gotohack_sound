import matplotlib.pyplot as plt
import amplitudelevels as al
import numpy as np

data1 = al.get_all_levels()

data1 = data1[900:42800]

x = [i for i in range(len(data1))]


#norm_data = np.fft.rfft(data1)

print(data1[140:300])


#plt.plot(x,data1)
#plt.show()
