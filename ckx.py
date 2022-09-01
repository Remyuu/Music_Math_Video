#REmoo的优化任务
#1、把公式统一写在外面
#2、坐标轴参数统一化
#3、整理每段Video Clip的animation部分
#4、提高代码重用性


from manim import *
import librosa
import numpy as np
class ContinuousFourier(Scene):
    def construct(self):
        second = 3
        a = TAU/second*0.5
        Da = DecimalNumber(a)
        
        values = VGroup(*[
            Tex(f"{t}=",tex_to_color_map={f"{t}":color}).scale(1.3)
            for t,color in zip(["a","b","c"],[RED,BLUE,GREEN])
        ])
        #*[a,b,c] -- a,b,c

        values.arrange(DOWN,aligned_edge=LEFT,buff=1.2)
        values.align_to(Da,LEFT)

        axes = Axes(
            x_range=[0 , second , 1],
            y_range=[0, 1.1, 1],
            x_length=(7+1/9)*2*1.8,
            y_length=4*3/4,
            axis_config={"include_numbers": True},
        )

        f = lambda x: 0.5*np.cos(3*2*PI*x)+0.5
        normal_graph = axes.plot(f,color=YELLOW)
        group1 = VGroup(axes,normal_graph)
        group1.scale(0.5).to_edge(UP)
        
        axes_label = axes.get_axis_labels()
        
        polar_axix = PolarPlane(radius_max=1,size=5)
        polar_graph = polar_axix.plot_parametric_curve(
            lambda t : [
                +np.cos(a*t) * (f(t)),
                -np.sin(a*t) * (f(t)),
                0
            ],
            t_range=[0,second],
            color=BLUE
        )

        upfunc = lambda obj : obj.become(polar_axix.plot_parametric_curve(
            lambda t : [
                +np.cos(Da.get_value()*t) * (f(t)),
                -np.sin(Da.get_value()*t) * (f(t)),
                0
            ],
            t_range=[0,second],
            color=BLUE
        ))
        polar_graph.add_updater(upfunc)

        group2 = VGroup(polar_axix,polar_graph)
        group2.to_edge(DL)


        self.play(Write(values))
        self.play(Write(Da))
        self.add(axes,polar_axix,axes_label)
        self.add(normal_graph)
        self.play(ReplacementTransform(normal_graph,polar_graph),
            run_time=3.5,
            path_arc = -TAU*2/3)
        self.wait() 
        self.play(ChangeDecimalToValue(Da,5),runtime=3)
        self.wait()


class PlotDots(Scene):
    def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))

        for x in range(_len_sample):
            dots_set.append(Dot(stroke_width=3))
            dots_set[x].move_to(axes.c2p(x,sample[x]))
            self.add(dots_set[x])
            Vg.add(dots_set[x])
            #self.play(FadeIn(dots_set[x]),run_time=run_time/_len_sample)
        return dots_set

    def construct(self):
        # WAVE_FILE, SAM_RATE = librosa.load(r'003.wav')
        # NUM_DOTS = len(WAVE_FILE)  # number of discrete point
        # DURATION = NUM_DOTS/SAM_RATE  # duration of the audio (second)
        # SAMPLE_DENSITY = 1 / 1 # the density of point

        # data = WAVE_FILE[1000:1030:int(1/SAMPLE_DENSITY)]
        #len_data = len(data)
########################################################
#                       GOT SAMPLE                     #
########################################################
        sample = [1.50000000000000,-0.154508497187473,-1.21352549156242,0.404508497187473,0.463525491562423,-0.500000000000000,0.463525491562420,0.404508497187476,-1.21352549156242,-0.154508497187479,1.50000000000000,-0.154508497187468,-1.21352549156242,0.404508497187468,0.463525491562424,-0.500000000000000,0.463525491562415,0.404508497187478,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187460,-1.21352549156243,0.404508497187464,0.463525491562427,-0.500000000000000,0.463525491562410,0.404508497187484,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187451,-1.21352549156243,0.404508497187463,0.463525491562426,-0.500000000000000,0.463525491562409,0.404508497187488,-1.21352549156241,-0.154508497187491,1.50000000000000,-0.154508497187450,-1.21352549156243,0.404508497187455,0.463525491562433,-0.500000000000000,0.463525491562405,0.404508497187493,-1.21352549156241,-0.154508497187499,1.50000000000000,-0.154508497187462,-1.21352549156242,0.404508497187471,0.463525491562430,-0.500000000000000,0.463525491562419,0.404508497187469,-1.21352549156242,-0.154508497187472,1.50000000000000,-0.154508497187482,-1.21352549156242,0.404508497187487,0.463525491562417,-0.500000000000000,0.463525491562411,0.404508497187473,-1.21352549156241,-0.154508497187480,1.50000000000000,-0.154508497187454,-1.21352549156244,0.404508497187457,0.463525491562431,-0.500000000000000,0.463525491562404,0.404508497187478,-1.21352549156242,-0.154508497187488,1.50000000000000,-0.154508497187480,-1.21352549156243,0.404508497187473,0.463525491562418,-0.500000000000000,0.463525491562397,0.404508497187487,-1.21352549156242,-0.154508497187496,1.50000000000000,-0.154508497187472,-1.21352549156243,0.404508497187468,0.463525491562446,-0.500000000000000,0.463525491562390,0.404508497187492,-1.21352549156241,-0.154508497187510]
        sample_len = len(sample)
        axes = Axes(x_range=(0,sample_len,100),y_range=(min(sample),max(sample),1))
        self.add(axes)#Add coordinates()

        ax_TOTAL = VGroup(axes)
        dots_set = self.Create_Dot_Set(axes,sample,ax_TOTAL,run_time=1)

        formula_004 = MathTex(
            r"\left[\begin{array}{l}\
            f_{0} \\\
            f_{1} \\\
            f_{2} \\\
            f_{3} \\\
            f_{4} \\\
            f_{5} \\\
            f_{6} \\\
            f_{7} \\\
            f_{8} \\\
            f_{9} \\\
            \end{array}\right]"
        ).to_edge(LEFT).scale(0.5)
        
        self.play(Write(formula_004),ax_TOTAL.animate.next_to(formula_004,RIGHT))
        _tc = 0 #temp Int_counter
        _ts=[] #temp Animation_set
        for dot in dots_set:
            if _tc <= 9 * 2:
                _ts.append(Transform(dot,formula_004[0][18+_tc:20+_tc]))
            _tc = _tc +2
        self.play(*_ts,run_time=3)
        self.wait()


class ShowFormula2(Scene):
    def construct(self):
        formula_002 = MathTex(
            r"\hat{f}_{k}=\sum_{j=0}^{n-1} f_{j} e^{-i 2 \pi k j / n}"
            # ,substrings_to_isolate="x"
        ).shift(UP)
        formula_003 = MathTex(
            r"k=0,1,2,...,n-1"
        ).next_to(formula_002, DOWN)

        formula_002[0][11:13].color=YELLOW 
        self.add(formula_002,formula_003) 
        self.play(Write(formula_002), Write(formula_003), run_time=2)
        self.play(formula_002[0][11:13].animate.set_color(YELLOW))
        self.play(Wiggle(formula_002[0][11:13]))
        self.play(Indicate(formula_002[0][11:13]))  
        self.wait()

class Calculation(Scene):
#极坐标
    def Create_Dot_Set(self,axes,sample,Vg,freq=1,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        ani_set=[]
        for x in range(_len_sample):
            dots_set.append(Dot(stroke_width=0.5))

            dots_set[x].move_to(axes.polar_to_point(sample[x],x*freq))
            #self.add(dots_set[x])
            Vg.add(dots_set[x])
            #ani_set.append(FadeIn(dots_set[x]))
        
        #self.play(*ani_set,run_time=run_time)
        return dots_set


    def construct(self):
        formula_004 = MathTex(
            r"\left[\begin{array}{l}\
            f_{0} \\\
            f_{1} \\\
            f_{2} \\\
            f_{3} \\\
            f_{4} \\\
            f_{5} \\\
            f_{6} \\\
            f_{7} \\\
            f_{8} \\\
            f_{9} \\\
            \end{array}\right]"
        ).to_edge(RIGHT)

        self.add(formula_004)
        
        formula_006 = MathTex(
            r"\left[\begin{array}{l}\
            e^{-i 2 \pi(2(0)) / 9  }\\\
            e^{-i 2 \pi(2(1)) / 9  }\\\
            e^{-i 2 \pi(2(2)) / 9  }\\\
            e^{-i 2 \pi(2(3)) / 9  }\\\
            e^{-i 2 \pi(2(4)) / 9  }\\\
            e^{-i 2 \pi(2(5)) / 9  }\\\
            e^{-i 2 \pi(2(6)) / 9  }\\\
            e^{-i 2 \pi(2(7)) / 9  }\\\
            e^{-i 2 \pi(2(8)) / 9  }\\\
            e^{-i 2 \pi(2(9)) / 9  }\\\
            \end{array}\right]" 
        ).next_to(formula_004,LEFT)
        


        polar_axix = PolarPlane(radius_max=2).next_to(formula_006,LEFT)
        self.add(polar_axix)
        graph_total = VGroup(polar_axix)
        
        sample = [1.50000000000000,-0.154508497187473,-1.21352549156242,0.404508497187473,0.463525491562423,-0.500000000000000,0.463525491562420,0.404508497187476,-1.21352549156242,-0.154508497187479,1.50000000000000,-0.154508497187468,-1.21352549156242,0.404508497187468,0.463525491562424,-0.500000000000000,0.463525491562415,0.404508497187478,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187460,-1.21352549156243,0.404508497187464,0.463525491562427,-0.500000000000000,0.463525491562410,0.404508497187484,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187451,-1.21352549156243,0.404508497187463,0.463525491562426,-0.500000000000000,0.463525491562409,0.404508497187488,-1.21352549156241,-0.154508497187491,1.50000000000000,-0.154508497187450,-1.21352549156243,0.404508497187455,0.463525491562433,-0.500000000000000,0.463525491562405,0.404508497187493,-1.21352549156241,-0.154508497187499,1.50000000000000,-0.154508497187462,-1.21352549156242,0.404508497187471,0.463525491562430,-0.500000000000000,0.463525491562419,0.404508497187469,-1.21352549156242,-0.154508497187472,1.50000000000000,-0.154508497187482,-1.21352549156242,0.404508497187487,0.463525491562417,-0.500000000000000,0.463525491562411,0.404508497187473,-1.21352549156241,-0.154508497187480,1.50000000000000,-0.154508497187454,-1.21352549156244,0.404508497187457,0.463525491562431,-0.500000000000000,0.463525491562404,0.404508497187478,-1.21352549156242,-0.154508497187488,1.50000000000000,-0.154508497187480,-1.21352549156243,0.404508497187473,0.463525491562418,-0.500000000000000,0.463525491562397,0.404508497187487,-1.21352549156242,-0.154508497187496,1.50000000000000,-0.154508497187472,-1.21352549156243,0.404508497187468,0.463525491562446,-0.500000000000000,0.463525491562390,0.404508497187492,-1.21352549156241,-0.154508497187510]
        
        self.play(Write(formula_006))
        graph_total.animate.to_edge(LEFT)
        
        polar_data = self.Create_Dot_Set(polar_axix, sample,graph_total,1)
        self.add(*polar_data)

        for x in range(100):
            new_dots=self.Create_Dot_Set(polar_axix, sample,graph_total,x/100)
            count=-1
            ani_set=[]
            for obj in polar_data:
                count=count+1
                ani_set.append(Transform(obj,new_dots[count]))
            self.play(*ani_set,run_time=0.2)
                

class STFT(Scene):
    def construct(self):
        formula_004a = MathTex(r"e^{-i 2 \pi(2(0)) / 19")
        self.add_subcaption("Hello sub!", duration=1)
        self.play(Write(formula_004a))

####
#i2gp()
#简而言之，在函数graph上打点
#i2gp() == input_to_graph_point()
#Returns the coordinates of the point on a graph corresponding to an x value.
class i2gp_test(Scene):
#创建ax坐标、curve曲线。使用i2gp()，取得curve上某点的坐标。创建dot点，移动过去。
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x : np.cos(x))
        position = ax.input_to_graph_point(graph=curve,x=PI)
        dot = Dot(color=YELLOW).move_to(position)
        self.add(ax, curve, dot)
        
class Camera_move(MovingCameraScene):
    def construct(self):
        #保存默认摄像机状态，方便恢复
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        #graph.t_min相当于graph.x_range[0],即定义域左边界
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)

        #摄像机放大一倍，放大中心是动点moving_dot
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        #创建更新函数
        # 作用：所有被传入的Mobject都会被移动到动点moving_dot的中心
        def update_cam_pos(mob):
            moving_dot.get_center()
            mob.move_to(moving_dot.get_center())

        #为camera添加updater更新函数
        self.camera.frame.add_updater(update_cam_pos)
        #动画函数MoveAlongPath，传入运动的物体，路径graph。
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        #self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))