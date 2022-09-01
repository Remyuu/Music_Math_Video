# # # # from curses import flash
# # # # from manim import *

# # # # class ShowFormula2(Scene):
# # # #     def construct(self):
# # # #         formula_002 = MathTex(
# # # #             r"\hat{f}_{k}=\sum_{j=0}^{n-1} f_{j} e^{-i 2 \pi k j / n}"
# # # #             #,substrings_to_isolate="x"#隔离x作为字串，后面就可以单独渲染它的颜色了
# # # #         ).shift(UP)
# # # #         formula_003 = MathTex(
# # # #             r"k=0,1,2,...,n-1"
# # # #         ).next_to(formula_002,DOWN)

        
# # # #         #formula_002[0][11:13].color=YELLOW

        
        


# # # #         #self.add(formula_002,formula_003)

# # # #         self.play(Write(formula_002),Write(formula_003),run_time=2)
# # # #         self.play(formula_002[0][11:13].animate.set_color(YELLOW))
# # # #         self.play(Wiggle(formula_002[0][11:13]))
# # # #         self.play(Circumscribe(formula_002[0][11:13]))
# # # #         self.play(Indicate(formula_002[0][11:13]))#高亮
# # # #         self.wait()


# # # from manim import *
# # # import librosa







# # # class PlotDots(Scene):
# # #     def construct(self):
# # #         # WAVE_FILE, SAM_RATE = librosa.load(r'wav_dir/Example01_BreakAndColumn.wav')
# # #         # NUM_DOTS = len(WAVE_FILE)  # number of discrete point
# # #         # DURATION = NUM_DOTS/SAM_RATE  # duration of the audio (second)
# # #         # SAMPLE_DENSITY = 1 / 1 # the density of point

# # #         # data = WAVE_FILE[1000:1030:int(1/SAMPLE_DENSITY)]
# # #         # len_data = len(data)
# # #         sample = [1,0.929776485888251,0.728968627421412,0.425779291565073,0.0627905195293133,-0.309016994374947,-0.637423989748690,-0.876306680043864,-0.992114701314478,-0.968583161128631,-0.809016994374948,-0.535826794978997,-0.187381314585725,0.187381314585724,0.535826794978997,0.809016994374947,0.968583161128631,0.992114701314478,0.876306680043864,0.637423989748690,0.309016994374948,-0.0627905195293127,-0.425779291565072,-0.728968627421412,-0.929776485888252,-1,-0.929776485888252,-0.728968627421411,-0.425779291565072,-0.0627905195293152,0.309016994374947,0.637423989748689,0.876306680043864,0.992114701314478,0.968583161128631,0.809016994374947,0.535826794978997,0.187381314585726,-0.187381314585725,-0.535826794978996,-0.809016994374947,-0.968583161128631,-0.992114701314478,-0.876306680043864,-0.637423989748691,-0.309016994374948,0.0627905195293141,0.425779291565075,0.728968627421412,0.929776485888251,1,0.929776485888251,0.728968627421413,0.425779291565073,0.0627905195293120,-0.309016994374947,-0.637423989748690,-0.876306680043865,-0.992114701314477,-0.968583161128632,-0.809016994374948,-0.535826794978999,-0.187381314585726,0.187381314585724,0.535826794978992,0.809016994374945,0.968583161128630,0.992114701314479,0.876306680043866,0.637423989748692,0.309016994374948,-0.0627905195293102,-0.425779291565071,-0.728968627421411,-0.929776485888251,-1,-0.929776485888251,-0.728968627421413,-0.425779291565073,-0.0627905195293124,0.309016994374946,0.637423989748690,0.876306680043863,0.992114701314477,0.968583161128632,0.809016994374950,0.535826794978996,0.187381314585727,-0.187381314585721,-0.535826794978997,-0.809016994374947,-0.968583161128630,-0.992114701314479,-0.876306680043864,-0.637423989748692,-0.309016994374952,0.0627905195293134,0.425779291565071,0.728968627421409,0.929776485888252]

# # #         sample_len = len(sample)
# # #         axes = Axes(x_range=(0,sample_len,100),y_range=(-1,2,1))
# # #         # graph = axes.plot_line_graph(
# # #         #         x_values=range(sample_len),
# # #         #         y_values = sample,        
# # #         #         #line_color=G  OLD_E,
# # #         #         vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
# # #         #         stroke_width = 0,
# # #         #     )
# # #         dots_set = []
# # #         for x in range(int(len(sample))):
# # #             dots_set.append(Dot(stroke_width=3))
# # #             dots_set[x].move_to(axes.c2p(x,sample[x]))
# # #             #self.add(dots_set[x])
# # #             self.play(FadeIn(dots_set[x]),run_time=0.08)
# # #         self.add(axes)
# # from manim import *
# # import librosa


# # class PlotDots(Scene):
# #     def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
# #         dots_set = []
# #         _len_sample = int(len(sample))

# #         for x in range(_len_sample):
# #             dots_set.append(Dot(stroke_width=3))
# #             dots_set[x].move_to(axes.c2p(x,sample[x]))
# #             self.add(dots_set[x])
# #             Vg.add(dots_set[x])
# #             #self.play(FadeIn(dots_set[x]),run_time=run_time/_len_sample)
# #         return dots_set


# #     def construct(self):
# #         # WAVE_FILE, SAM_RATE = librosa.load(r'003.wav')
# #         # NUM_DOTS = len(WAVE_FILE)  # number of discrete point
# #         # DURATION = NUM_DOTS/SAM_RATE  # duration of the audio (second)
# #         # SAMPLE_DENSITY = 1 / 1 # the density of point

# #         # data = WAVE_FILE[1000:1030:int(1/SAMPLE_DENSITY)]
# #         #len_data = len(data)
# # ########################################################
# # #                       GOT SAMPLE                     #
# # ########################################################
# #         sample = [1,0.929776485888251,0.728968627421412,0.425779291565073,0.0627905195293133,-0.309016994374947,-0.637423989748690,-0.876306680043864,-0.992114701314478,-0.968583161128631,-0.809016994374948,-0.535826794978997,-0.187381314585725,0.187381314585724,0.535826794978997,0.809016994374947,0.968583161128631,0.992114701314478,0.876306680043864,0.637423989748690,0.309016994374948,-0.0627905195293127,-0.425779291565072,-0.728968627421412,-0.929776485888252,-1,-0.929776485888252,-0.728968627421411,-0.425779291565072,-0.0627905195293152,0.309016994374947,0.637423989748689,0.876306680043864,0.992114701314478,0.968583161128631,0.809016994374947,0.535826794978997,0.187381314585726,-0.187381314585725,-0.535826794978996,-0.809016994374947,-0.968583161128631,-0.992114701314478,-0.876306680043864,-0.637423989748691,-0.309016994374948,0.0627905195293141,0.425779291565075,0.728968627421412,0.929776485888251,1,0.929776485888251,0.728968627421413,0.425779291565073,0.0627905195293120,-0.309016994374947,-0.637423989748690,-0.876306680043865,-0.992114701314477,-0.968583161128632,-0.809016994374948,-0.535826794978999,-0.187381314585726,0.187381314585724,0.535826794978992,0.809016994374945,0.968583161128630,0.992114701314479,0.876306680043866,0.637423989748692,0.309016994374948,-0.0627905195293102,-0.425779291565071,-0.728968627421411,-0.929776485888251,-1,-0.929776485888251,-0.728968627421413,-0.425779291565073,-0.0627905195293124,0.309016994374946,0.637423989748690,0.876306680043863,0.992114701314477,0.968583161128632,0.809016994374950,0.535826794978996,0.187381314585727,-0.187381314585721,-0.535826794978997,-0.809016994374947,-0.968583161128630,-0.992114701314479,-0.876306680043864,-0.637423989748692,-0.309016994374952,0.0627905195293134,0.425779291565071,0.728968627421409,0.929776485888252]

# #         sample_len = len(sample)
# #         axes = Axes(x_range=(0,sample_len,100),y_range=(-1,1.1,1))
# #         self.add(axes)#Add coordinates()

# #         ax_TOTAL = VGroup(axes)
# #         dots_set = self.Create_Dot_Set(axes,sample,ax_TOTAL,run_time=1)#绘制点击，返回点的Mobject_list

# #         formula_004 = MathTex(
# #             r"\left[\begin{array}{l}\
# #             f_{0} \\\
# #             f_{1} \\\
# #             f_{2} \\\
# #             f_{3} \\\
# #             f_{4} \\\
# #             f_{5} \\\
# #             f_{6} \\\
# #             f_{7} \\\
# #             f_{8} \\\
# #             f_{9} \\\
# #             \end{array}\right]"
# #         ).to_edge(LEFT).scale(0.5)
        
# #         self.play(Write(formula_004),ax_TOTAL.animate.next_to(formula_004,RIGHT))
# #         _tc = 0 #temp Int_counter
# #         _ts=[] #temp Animation_set
# #         for dot in dots_set:
# #             if _tc <= 9 * 2:
# #                 _ts.append(Transform(dot,formula_004[0][18+_tc:20+_tc]))
# #             _tc = _tc +2
# #         self.play(*_ts,run_time=3)
# #         self.wait()


# # class Calculation(Scene):
# #     def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
# #         dots_set = []
# #         _len_sample = int(len(sample))

# #         for x in range(_len_sample):
# #             dots_set.append(Dot(stroke_width=3))
# #             dots_set[x].move_to(axes.polar_to_point(sample[x],x/TAU))
# #             self.add(dots_set[x])
# #             Vg.add(dots_set[x])
# #             #self.play(FadeIn(dots_set[x]),run_time=run_time/_len_sample)
# #         return dots_set
# #     def construct(self):
# #         formula_004 = MathTex(
# #             r"\left[\begin{array}{l}\
# #             f_{0} \\\
# #             f_{1} \\\
# #             f_{2} \\\
# #             f_{3} \\\
# #             f_{4} \\\
# #             f_{5} \\\
# #             f_{6} \\\
# #             f_{7} \\\
# #             f_{8} \\\
# #             f_{9} \\\
# #             \end{array}\right]"
# #         ).move_to(RIGHT*2)

# #         self.add(formula_004)

# #         formula_005 = MathTex(
# #             r"\left[\begin{array}{l}\
# #             e^{-i 2 \pi(2(0)) / 19  } \times  f_{0}\\\
# #             e^{-i 2 \pi(2(1)) / 19  } \times  f_{1}\\\
# #             e^{-i 2 \pi(2(2)) / 19  } \times  f_{2}\\\
# #             e^{-i 2 \pi(2(3)) / 19  } \times  f_{3}\\\
# #             e^{-i 2 \pi(2(4)) / 19  } \times  f_{4}\\\
# #             e^{-i 2 \pi(2(5)) / 19  } \times  f_{5}\\\
# #             e^{-i 2 \pi(2(6)) / 19  } \times  f_{6}\\\
# #             e^{-i 2 \pi(2(7)) / 19  } \times  f_{7}\\\
# #             e^{-i 2 \pi(2(8)) / 19  } \times  f_{8}\\\
# #             e^{-i 2 \pi(2(9)) / 19  } \times  f_{9}\\\
# #             \end{array}\right]" 
# #         ).to_edge(RIGHT)
# #         polar_axix = PolarPlane()
# #         self.add(polar_axix)
# #         graph_total = VGroup(polar_axix)

# #         polar_data = self.Create_Dot_Set(polar_axix, sample,graph_total)

# #         self.play(Transform(formula_004,formula_005))
# #         self.wait()

# from manim import *
# # import numpy as np
# # class ContinuousFourier(Scene):
# #     def construct(self):
# #         axes = Axes()
# #         normal_graph = axes.plot(lambda x: np.cos(x)).to_edge(UP)


# #         polar_axix = Axes()
# #         polar_graph = polar_axix.plot_parametric_curve(
# #             lambda t : [
# #                 np.cos(3*t) * (np.cos(t)+3-2),
# #                 np.sin(3*t) * (np.cos(t)+3-2),
# #                 0
# #             ],
# #             t_range=[0,TAU]
# #         ).to_edge(DOWN)
# #         self.add(axes,polar_axix)
# #         self.add(normal_graph,polar_graph)
# #         self.play(Transform(normal_graph,polar_graph))
# #         self.wait()


# class Calculation(Scene):
# #极坐标
#     def Create_Dot_Set(self,axes,sample,Vg,freq=1,run_time=1):
#         dots_set = []
#         _len_sample = int(len(sample))
#         ani_set=[]
#         for x in range(_len_sample):
#             dots_set.append(Dot(stroke_width=0.5))

#             dots_set[x].move_to(axes.polar_to_point(sample[x],x*freq))
#             #self.add(dots_set[x])
#             Vg.add(dots_set[x])
#             #ani_set.append(FadeIn(dots_set[x]))
        
#         #self.play(*ani_set,run_time=run_time)
#         return dots_set


#     def construct(self):
#         formula_004 = MathTex(
#             r"\left[\begin{array}{l}\
#             f_{0} \\\
#             f_{1} \\\
#             f_{2} \\\
#             f_{3} \\\
#             f_{4} \\\
#             f_{5} \\\
#             f_{6} \\\
#             f_{7} \\\
#             f_{8} \\\
#             f_{9} \\\
#             \end{array}\right]"
#         ).to_edge(RIGHT)

#         self.add(formula_004)
        
#         formula_006 = MathTex(
#             r"\left[\begin{array}{l}\
#             e^{-i 2 \pi(2(0)) / 9  }\\\
#             e^{-i 2 \pi(2(1)) / 9  }\\\
#             e^{-i 2 \pi(2(2)) / 9  }\\\
#             e^{-i 2 \pi(2(3)) / 9  }\\\
#             e^{-i 2 \pi(2(4)) / 9  }\\\
#             e^{-i 2 \pi(2(5)) / 9  }\\\
#             e^{-i 2 \pi(2(6)) / 9  }\\\
#             e^{-i 2 \pi(2(7)) / 9  }\\\
#             e^{-i 2 \pi(2(8)) / 9  }\\\
#             e^{-i 2 \pi(2(9)) / 9  }\\\
#             \end{array}\right]" 
#         ).next_to(formula_004,LEFT)
        

# #        formula_005 = MathTex(
# #            r"\left[\begin{array}{l}\
# #            e^{-i 2 \pi(2(0)) / 9  } \times  f_{0}\\\
# #            e^{-i 2 \pi(2(1)) / 9  } \times  f_{1}\\\
# #            e^{-i 2 \pi(2(2)) / 9  } \times  f_{2}\\\
# #            e^{-i 2 \pi(2(3)) / 9  } \times  f_{3}\\\
# #            e^{-i 2 \pi(2(4)) / 9  } \times  f_{4}\\\
# #            e^{-i 2 \pi(2(5)) / 9  } \times  f_{5}\\\
# #            e^{-i 2 \pi(2(6)) / 9  } \times  f_{6}\\\
# #            e^{-i 2 \pi(2(7)) / 9  } \times  f_{7}\\\
# #            e^{-i 2 \pi(2(8)) / 9  } \times  f_{8}\\\
# #            e^{-i 2 \pi(2(9)) / 9  } \times  f_{9}\\\
# #            \end{array}\right]" 
# #        ).to_edge(RIGHT)

#         polar_axix = PolarPlane(radius_max=2).next_to(formula_006,LEFT)
#         self.add(polar_axix)
#         graph_total = VGroup(polar_axix)
        
#         sample = [1.50000000000000,-0.154508497187473,-1.21352549156242,0.404508497187473,0.463525491562423,-0.500000000000000,0.463525491562420,0.404508497187476,-1.21352549156242,-0.154508497187479,1.50000000000000,-0.154508497187468,-1.21352549156242,0.404508497187468,0.463525491562424,-0.500000000000000,0.463525491562415,0.404508497187478,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187460,-1.21352549156243,0.404508497187464,0.463525491562427,-0.500000000000000,0.463525491562410,0.404508497187484,-1.21352549156242,-0.154508497187487,1.50000000000000,-0.154508497187451,-1.21352549156243,0.404508497187463,0.463525491562426,-0.500000000000000,0.463525491562409,0.404508497187488,-1.21352549156241,-0.154508497187491,1.50000000000000,-0.154508497187450,-1.21352549156243,0.404508497187455,0.463525491562433,-0.500000000000000,0.463525491562405,0.404508497187493,-1.21352549156241,-0.154508497187499,1.50000000000000,-0.154508497187462,-1.21352549156242,0.404508497187471,0.463525491562430,-0.500000000000000,0.463525491562419,0.404508497187469,-1.21352549156242,-0.154508497187472,1.50000000000000,-0.154508497187482,-1.21352549156242,0.404508497187487,0.463525491562417,-0.500000000000000,0.463525491562411,0.404508497187473,-1.21352549156241,-0.154508497187480,1.50000000000000,-0.154508497187454,-1.21352549156244,0.404508497187457,0.463525491562431,-0.500000000000000,0.463525491562404,0.404508497187478,-1.21352549156242,-0.154508497187488,1.50000000000000,-0.154508497187480,-1.21352549156243,0.404508497187473,0.463525491562418,-0.500000000000000,0.463525491562397,0.404508497187487,-1.21352549156242,-0.154508497187496,1.50000000000000,-0.154508497187472,-1.21352549156243,0.404508497187468,0.463525491562446,-0.500000000000000,0.463525491562390,0.404508497187492,-1.21352549156241,-0.154508497187510]
        
#         self.play(Write(formula_006))
#         graph_total.animate.to_edge(LEFT)
        
#         polar_data = self.Create_Dot_Set(polar_axix, sample,graph_total,1)
#         self.add(*polar_data)

#         for x in range(100):
#             new_dots=self.Create_Dot_Set(polar_axix, sample,graph_total,x/100)
#             count=-1
#             ani_set=[]
#             for obj in polar_data:
#                 count=count+1
#                 ani_set.append(Transform(obj,new_dots[count]))
#             self.play(*ani_set,run_time=0.2)
                
# class ContinuousFourier(Scene):
#     def construct(self):
#         axes = Axes(
#             x_range=[0, 10, 1],
#             y_range=[0, 2, 1],
#         )
#         f = lambda x: np.cos(10*x)+1
#         normal_graph = axes.plot(f,color=YELLOW)
#         group1 = VGroup(axes,normal_graph)
        
#         polar_axix = PolarPlane(radius_max=2,size=6)
#         polar_graph = polar_axix.plot_parametric_curve(
#             lambda t : [
#                 np.cos(0.75*t) * (f(t)),
#                 -np.sin(0.75*t) * (f(t)),
#                 0
#             ],
#             t_range=[0,TAU]
#         )
#         group2 = VGroup(polar_axix,polar_graph)

#         self.add(group1)
#         self.play(ReplacementTransform(normal_graph,group2),
#             run_time=3.5,
#             path_arc = -TAU*4/5)
#         self.wait() 

from manim import *
import numpy as np
import scipy.integrate

class test(Scene):
    def change_channel(self,change_to:int):
        self.__channel__= change_to
        # self.play(Transform(self.,target))
    def construct(self):
        #### Global variables ####
            #意思是现在选中需要扭转与分析的函数是哪一个（为了加updater显示不同颜色
        self.__channel__=1

        second = 2
        y_scale = 0.5
        Da = DecimalNumber(1)

        f1_lambda = 5
        f2_lambda = 11
        # function f
        f_1 = lambda x: y_scale*(np.cos(f1_lambda*2*PI*x)+1)
        f_2 = lambda x: y_scale*(np.cos(f1_lambda*2*PI*x)+0.5*np.cos(f2_lambda*2*PI*x)+1.5)

        # Cartesian coordinates
        c_axis = Axes(
            x_range=[0 , second + 0.1 , 1],y_range=[0, 2, 1],
            y_length=2,axis_config={"include_numbers": True},tips=False,
            ).to_edge(UP)
        c_axis_label = c_axis.get_axis_labels(x_label='time',y_label='intensity')

        _Tex_f_1 = MathTex(r'\cos({}\pi \cdot x)'.format(f1_lambda),
                color=RED_A).scale(1.5).shift(UP*2.5)
        _Tex_f_2 = MathTex(r'\cos({}\pi \cdot x)+0.5\cos({}\cdot 2\pi \cdot x)'.format(f1_lambda,f2_lambda),
                color=RED_A).scale(1.5).shift(UP*2.5)
        _backg_1 = BackgroundRectangle(_Tex_f_1, color=WHITE, fill_opacity=0.15)
        _backg_2 = BackgroundRectangle(_Tex_f_2, color=WHITE, fill_opacity=0.15)
        #图像的公式名称标签
        graph_label_1 = VGroup(_Tex_f_1,_backg_1)
        graph_label_2 = VGroup(_Tex_f_2,_backg_2)

        graph_c_1 = c_axis.plot(f_1,x_range=[0,second,0.01],color=YELLOW)
        graph_c_2 = c_axis.plot(f_2,x_range=[0,second,0.01],color=PINK)

        #### polar ####
        polar_axis = PolarPlane(radius_max=1.9,size=4.5).to_edge(DL)
        graph_polar = polar_axis.plot_parametric_curve(
            lambda t : [
                +np.cos(Da.get_value()*TAU*t) * (f_1(t)),
                -np.sin(Da.get_value()*TAU*t) * (f_1(t)),
                0
            ],t_range=[0,second,0.01],color=RED
            )

        def up_polar_graph(obj): 
            if   self.__channel__==1:
                _color_ = RED
                _fo_=f_1
            elif self.__channel__==2:
                _color_ = YELLOW
                _fo_=f_2
            return obj.become(polar_axis.plot_parametric_curve(
            lambda t: [
                +np.cos(Da.get_value()*TAU*t) * (_fo_(t)),
                -np.sin(Da.get_value()*TAU*t) * (_fo_(t)),
                0
            ], t_range=[0, second, 0.01], color=_color_))


        #####freqDomain####
        t_min = 0;t_max = second
        scale = 1 / t_max - t_min
        freqD_axis = Axes(x_range=[0,15,1],y_range=[-0.1,0.8],
                x_length=7,y_length=3,
                axis_config={"include_numbers": True}).next_to(polar_axis,RIGHT).align_to(polar_axis,UP)
        freqD_axis_label = freqD_axis.get_axis_labels(x_label='freq(TAU)',y_label='')
        def get_freqDomain_sample(wind):
            z = scale * scipy.integrate.quad(
                lambda t : f_2(t)*np.exp(complex(0, -TAU*wind*t)),
            t_min, t_max
            )[0]
            return z.real

        graph_freqD = freqD_axis.plot(get_freqDomain_sample,x_range=[0,15,0.1])

        def get_dot_freqDomain(wind_freq,color=RED):#'wind_freq'no need to times TAU
            return Dot(freqD_axis.input_to_graph_point(x=wind_freq,graph=graph_freqD),color=color)
        
        dot_freqDomain = get_dot_freqDomain(0.1)

        dot_freqDomain.add_updater(lambda mob :mob.become(get_dot_freqDomain(Da.get_value())))

        ###############
        #绘制三个坐标轴
        self.add(c_axis,polar_axis,freqD_axis,
                 c_axis_label,freqD_axis_label)
        #绘制初始直角坐标图像
        self.add(graph_freqD,dot_freqDomain)

        #现在场景中，除了三幅图像和一个点没画
        #绘制直角坐标的c_g_1
        graph_polar.add_updater(up_polar_graph)
        self.play(Create(graph_c_1),FadeIn(graph_label_1))
        c_1_p = graph_c_1.copy()
        self.change_channel(1)
        self.play(ReplacementTransform(c_1_p,graph_polar),
            run_time=3.5,
            path_arc = -TAU*2/3)
        self.wait()

        self.play(ReplacementTransform(c_1_p,graph_polar))
        self.wait()
        
        self.wait()

        self.play(ChangeDecimalToValue(Da,5,run_time=10))
        self.wait()
        self.change_channel(2)
        self.play(ChangeDecimalToValue(Da,11,run_time=10))
        self.wait()


        self.wait()
        #self.play(ChangeDecimalToValue(Dk,9*TAU),rate_func=rate_functions.linear,run_time=5)
        self.wait()