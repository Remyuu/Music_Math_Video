from manim import *
import scipy
import librosa
import numpy as np

class EPIC_SCENE_JUMPING(Scene):
    def construct(self):
        x_limit = 6000
        ax = Axes(
            x_range=[0, int(x_limit), 1000],
            y_range=[0, 150, 30],
            tips=True,
            axis_config={"include_numbers": True},
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        n_o = 0
        f_size = 2048
        n_hop = f_size / 2
        N_fft = f_size * 2
        move_step = 1
        yy44,fs44 = librosa.load('wav_dir/Example01_BreakAndColumn.wav')
        
        _MAX_SAFE_STEP = (np.round(len(yy44))-np.round(len(yy44))%n_hop)/n_hop-1
        _SONG_TIME = len(yy44)/fs44
        n1 = int(n_o + n_hop*int(move_step))
        n2 = int(n_o + n_hop*int(move_step) + f_size)

        x_i = yy44[n1:n2]#The length of x_i is f_size

        X_i = np.abs(scipy.fft.rfft(x_i * np.hanning(len(x_i))))
        xf = scipy.fft.rfftfreq(f_size,1/44100)

        graph = ax.plot_line_graph(
                x_values = xf,
                y_values = X_i,
                #line_color=GOLD_E,
                add_vertex_dots = False,
                vertex_dot_style=dict(stroke_width=5),
                stroke_width = 2,
            )
        self.add(ax,graph)