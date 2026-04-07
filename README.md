HRTF-DSP-Assignment
A Python implementation of HRTF-based spatial audio rendering using the CIPIC HRTF database. 
This project renders a mono audio signal to different 3D positions by convolving it with subject-specific Head-Related Impulse Responses (HRIRs).

What is this?
Human ears use three cues to localise sound — ITD, ILD, and spectral coloration from the pinna.
The HRTF models all of these effects mathematically. By convolving any mono audio signal with a left and right HRIR pair from the CIPIC database, 
we can synthetically place that sound at any position in 3D space.

Repository Structure
HRTF-dsp-assignment/
│
├── hrtf_spatial_audio.ipynb       # Main implementation notebook
├── stereo_output_1.wav            # TC1 — Front/Center (Az 0°, El 0°)
├── stereo_output_2.wav            # TC2 — Hard Left (Az -80°, El 0°)
├── stereo_output_3.wav            # TC3 — Hard Right (Az +80°, El 0°)
├── stereo_output_4.wav            # TC4 — Above (Az 0°, El +90°)
├── stereo_output_5.wav            # TC5 — Below (Az 0°, El -39°)
└── README.md

Dependencies
bashpip install numpy scipy pydub

Download the CIPIC HRTF database .mat file from CIPIC and place it in the project folder
Open implmentation_of_hrtf.ipynb in Jupyter Notebook or VS Code and run all cells

Reference
Algazi, V. R., Duda, R. O., Thompson, D. M., & Avendano, C. (2001). The CIPIC HRTF Database. IEEE Workshop on Applications of Signal Processing to Audio and Acoustics.
