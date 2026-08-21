import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("X:\\AnsysEM\\Projects\\MultiAntennaDist.csv")
mask = df['d [mm]'] == 18
df = df[~mask]

df_crack = pd.read_csv("X:\\AnsysEM\\Projects\\MultiAntennaCrackDist4.csv")
res = df.groupby('d [mm]').idxmin()["dB(S(1,1)) []"]
mag_res = df["dB(S(1,1)) []"][res]
freqz_res = df["Freq [GHz]"][res]
res_crack = df_crack.groupby('d [mm]').idxmin()["dB(S(1,1)) []"]
mag_res_crack = df_crack["dB(S(1,1)) []"][res_crack]
freqz_res_crack = df_crack["Freq [GHz]"][res_crack]
d_arr = df['d [mm]'].unique() - 1.6
plt.plot(d_arr,np.abs(mag_res.to_numpy()-mag_res_crack.to_numpy()))
plt.title("Radius of crack = 4 mm")
plt.xlabel("Distance (mm)")
plt.ylabel("Difference in magnitude of resonance (dB)")
plt.savefig("X:\\AnsysEM\\Projects\\Magnitude difference 4mm.png")
plt.clf()
plt.plot(d_arr,np.abs(freqz_res.to_numpy()-freqz_res_crack.to_numpy()))
plt.title("Radius of crack = 4 mm")
plt.xlabel("Distance (mm)")
plt.ylabel("Difference in frequency of resonance (GHz)")
plt.savefig("X:\\AnsysEM\\Projects\\Frequency difference 4mm.png")