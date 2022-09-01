'''
请您安装manimlib、librosa、ffmpeg
控制台使用

manimgl show_song_wav.py show_song_wav -ow  --uhd 

编译
----------------------------
--low_quality
-l
使用低质量渲染(默认 480p15)
--medium_quality
-m
使用中等质量渲染(默认 720p30)
--hd
使用高质量渲染(默认 1080p30)
--uhd
使用 4K 质量渲染

'''


from manimlib import *
import librosa

dir = 'wav_dir'

class show_song_wav(Scene):
    def construct(self):
        WAVE_FILE,FS = librosa.load(dir+'/Example01_BreakAndColumn.wav')
        SUM_NUM = len(WAVE_FILE) #number of discrete point
        WAVE_TIME = SUM_NUM/FS #Aduio Clip Last Time (s)
        SAMPLE_DENSITY = 1 #the density of point ___ 1 is MAX
 
        wave_show = WAVE_FILE[::SAMPLE_DENSITY]
        len_wave_show = len(wave_show)

        print(str(len_wave_show)+'/'+str(SUM_NUM)+'\n'+"SAMPLE_DENSITY:"+str(len_wave_show/SUM_NUM))

        ax,graph = self.get_graph(wave_show,len_wave_show)#得到图像与坐标
        

#################show_part##################
        self.camera.frame.save_state()
#1-show wave
        self.show_wave(ax,graph)
        
#2-zoom camera
        new_axes, graph_snippet = self.show_zoom_camera(axes=ax,graph=graph,zoom_start=0.5,zoom_rect_dims=(14+2/9, 8))
        print(len(graph_snippet.get_anchors())) #--selected 7214 points

        #new_axes, graph_snippet = self.show_zoom_camera(axes=new_axes,graph=graph_snippet,zoom_start=0.5,zoom_rect_dims=(0.1, 8))
        #print(len(graph_snippet.get_anchors())) #--then , selected 102 points


#################end_animate#################



    def get_graph(self,wave_show,len_wave_show):
        ax = Axes(
            x_range=[0, len_wave_show,len_wave_show],
            y_range=[-1, 1, 1],

        )
        xs = np.arange(len_wave_show)
        points = ax.c2p(xs, wave_show)
        graph = VMobject()
        #graph.set_points_as_corners(points)
        graph.set_points_smoothly(points)
        
        return ax,graph

    def get_ax_label(self,axes):
        x_label = Text("Time(1/44100 s)").next_to(axes,RIGHT).shift(UL+LEFT*2).scale(0.8)
        y_label = Text("Intensity").next_to(axes,UL).shift(RIGHT).scale(0.8)
        return VGroup(x_label,y_label)

    def show_wave(self,ax,graph):
        labels = self.get_ax_label(ax)
        self.play(Write(ax))
        self.add(labels)
        self.play(Write(graph),
            run_time=0.1,
            rate_func=squish_rate_func(linear, 0.05, 1))
        self.wait()
        self.remove(labels)        

    def show_zoom_camera(self, axes, graph, zoom_start,zoom_rect_dims,run_time = 1):
        point = graph.point_from_proportion(zoom_start) * RIGHT
        zoom_rect = Rectangle(*zoom_rect_dims)
        zoom_rect.move_to(point)
        zoom_rect.set_stroke(BLUE, 2)

        graph_snippet = VMobject()
        graph_points = graph.get_anchors()
        lx = zoom_rect.get_left()[0]
        rx = zoom_rect.get_right()[0]
        xs = graph_points[:, 0]
        snippet_points = graph_points[(xs > lx) * (xs < rx)]
        graph_snippet.set_points_as_corners(snippet_points)
        graph_snippet.match_style(graph)
        point = graph_snippet.get_center().copy()
        point[1] = axes.get_origin()[1]
        zoom_rect.move_to(point)

        movers = [axes, graph, graph_snippet, zoom_rect]

        frame = self.camera.frame
        for mover in movers:
            mover.save_state()
            mover.generate_target()
            mover.target.stretch(frame.get_width() / zoom_rect.get_width(), 0, about_point=point)
            mover.target.stretch(frame.get_height() / zoom_rect.get_height(), 1, about_point=point)
            mover.target.shift(-point)
        graph_snippet.target.set_stroke(width=3)
        zoom_rect.target.set_stroke(width=0)
        axes.target.set_stroke(opacity=0)

        new_axes = Axes((0,int(len(snippet_points)),int(len(snippet_points))),(-1,1,), width=14+2/9)

        self.play(Write(zoom_rect))
        self.play(
            *map(MoveToTarget, movers),
            FadeIn(new_axes),
            run_time=run_time,
        )
        self.remove(graph, axes)

        # Swap axes

        # if fade_in_new_axes:
        #     self.play(FadeIn(new_axes))

        self.original_graph = graph
        self.original_axes = axes
        self.ax = new_axes
        self.graph = graph_snippet

        return new_axes, graph_snippet
    
