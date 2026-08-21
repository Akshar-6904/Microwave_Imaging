# Antenna-Based Bone Crack Detection Using Ansys HFSS

## 1. Project Overview

This project involves switched microstrip patch antenna array design ay **2.4GHz** on a flexible polyimide substrated for the purpose of scanning bones for defects using **Ansys HFSS**.

The main parameters analyzed are **S11, S12 resonant frequency, and electric field distribution**.

---

## 2. Objectives

* Design an antenna array on a flexible substrate.
* Model bone and bone-crack structures.
* Simulate antenna interaction with the bone model.
* Compare intact and cracked bone responses.
* Determine the optimal distance from skin required to detect the crack effectively.
* Analyze changes in S11 and resonant frequency.

---

## 3. Software

* Ansys Electronics Desktop
* Python

---

## 4. Project Structure

```text
Microwave_Imaging/
├── HFSS/
│   ├── Attempted_8x1_Array.aedt
│   ├── BoneCrackTwoAntennaTest.aedt
│   ├── DistanceOpti.aedt
│   ├── DP_1810_3_1.aedt
│   ├── DualAntennaSetup.aedt
│   ├── Failed_4x1_Array
│   ├── FR4_Antenna.aedt
│   ├── limbmodel.aedt
│   ├── MP2.4.aedt
│   ├── MultiAntennaCrack.aedt
│   ├── MultiAntennaDistance.aedt
│   ├── SingleAntenna_All_Solids
│   └── Working_4x1_array.aedt
│
├── images/
│   ├── FOURANTENNA.gif
│   ├── Frequency difference thin.png
│   └── Magnitude difference thin.png
│
├── python/
│   └── Analyze.py
│
├── results/
│   ├── S11.csv
│   ├── S21.csv
│   ├── SingleAntennaCrackDistfromLimb.csv
│   └── SingleAntennaDistfromLimb.csv
│
├── LICENSE
└── README.md
```

```

---

## 5. Iterative Antenna Design

### Microstrip Patch Antenna

* **Operating Frequency:** `2.4GHz`
* **Substrate:** `Polyimide`
* **Substrate Thickness:** `25um`
* **Dimensions:** `l*w(mm) = 34.4*42.6`
* **Feed Type:** `Microstrip Line`
* **File Name** `SingleAntenna_All_Solids.aedt`

**Purpose:**

`This was an initital design for a single flexible antenna. The simulation for this involved modelling the copper as a solid, as it was initially assumed that the thin substrate would require solid copper rather than sheets. Later it was discovered that this wasn't needed.`

---

### 4x1 Microstrip Patch Antenna Array

* **Operating Frequency:** `2.4GHz`
* **Substrate:** `Polyimide`
* **Substrate Thickness:** `25um`
* **Dimensions:** `l*w(mm) = 34.4*42.6`
* **Feed Type:** `Switchable corporate feed`
* **File Name** `Working_4x1_array.aedt`

**Purpose:**

`This design was used to expand the single element and create a wrappable array. The angle of scanning can be adjusted by using RF switches. The proposed switch was HMC1055.`

![A GIF of the second antenna in the array being ON with the rest OFF](images/FOURANTENNA.gif)
---

### FR4 dual rotated antennas

* **Operating Frequency:** `2.4GHz`
* **Substrate:** `FR4`
* **Substrate Thickness:** `1.6mm`
* **Dimensions:** `l*w(mm) = 29.4*38`
* **Feed Type:** `Microstrip Line`
* **File Name** `FR4_Antenna.aedt`

**Purpose:**

`As the design of the 8x1 array failed due to failing matching for the switches, due to time constraints the actually implemented design in hardware were two rotating FR4 antennas pointed at the bone opposed to each other. S11 and S12 parameters were collected from 1.2 to 3.6 GHz for each angle at a resolution of 30 degrees. The results are in the files S11 and S21.csv. At the angles closest to the crack, there was a difference between the intact bone and the bone with a crack in the S11 and S21 parameters.`

---

## 6. Bone Model

For the FR4 antennas, an optimal distance between the bone and antennas for detection was investigated by using a bone model in Ansys HFSS. A crack was also incorporated into the model to compare with the intact model and optimize for detection distance.

### Material Properties

| Material | Relative Permittivity | Conductivity |
| -------- | --------------------: | -----------: |
| Bone     |                `11.4` |      `0.788` |
| Muscle   |                `52.8` |       `1.71` |
| Skin     |                `38.1` |       `1.44` |
| Air      |                   `1` |          `0` |

---

## 7. Crack Model

The crack is modeled as an ellipsoid discontinuity (air gap) inside the bone structure.

| Parameter         |           Value |
| ----------------- | --------------: |
| Crack Length      |          `4 mm` |
| Crack Width       |          `1 mm` |
| Crack Depth       |          `1 mm` |
| Crack Location    |        `Center` |

---

## 8. HFSS Simulation Setup

### Solution Setup

* **Solution Frequency:** `2.4GHz`
* **Frequency Sweep:** `1.2 - 3.6 GHz`
* **Sweep Type:** `Fast (Linear)`
* **Maximum Passes:** `6`
* **Maximum Delta S:** `0.02`

### Excitation

* **Port Type:** `Wave Port`
* **Number of Ports:** `1-2`
* **Port Impedance:** `Zpi (matched with 50)`

### Boundary Conditions

* **Radiation Boundary:** `Yes`
* **PML:** `No`
* **Other:** `Infinite Sphere for radiation patterns`

---

## 10. Results

### S11 Comparison

![Comparison of resonance magnitude in S11](images/Magnitude%20difference%20thin.png)

### Resonant Frequency

![Comparison of frequency of resonance](images/Frequency%20difference%20thin.png)

### Hardware Comparison

The 

---


### Selected Sensitivity Metric

`[Specify the metric used to determine the best antenna.]`

---

## 12. Best Performing Design

**Selected Design:** `[Design XX]`

**Selection Criteria:**

* `[Criterion 1]`
* `[Criterion 2]`
* `[Criterion 3]`

**Result:**

`[Briefly describe why this antenna performed best.]`

---

## 13. Figures

### Antenna Geometry

![Antenna Geometry](figures/antenna_geometry.png)

### Bone Model

![Bone Model](figures/bone_model.png)

### Cracked Bone Model

![Cracked Bone](figures/cracked_bone.png)

### S11 Comparison

![S11 Comparison](figures/s11_comparison.png)

### Electric Field Distribution

![Electric Field](figures/e_field.png)

---

## 14. Future Work

* Test different crack sizes.
* Test different crack orientations.
* Test different crack locations.
* Optimize antenna geometry.
* Test different operating frequencies.
* Use realistic anatomical bone models.
* Include surrounding tissue layers.
* Perform experimental validation.
* Develop an automated crack-detection method.

---

## 15. References

1. Ansys HFSS Documentation
2. `[Reference for antenna design]`
3. `[Reference for bone/tissue electromagnetic properties]`
4. `[Reference for electromagnetic bone-crack detection]`

---

## 16. Project Status

**Status:** `[In Progress / Simulation Complete / Experimental Validation / Completed]`

**Software:** Ansys HFSS

**Number of Antenna Designs:** `[N]`

**Target Application:** Electromagnetic bone-crack detection

<img width="1276" height="498" alt="FOURANTENNA" src="https://github.com/user-attachments/assets/a029b4dd-d4d4-4195-acea-9a4a2d13707b" />
