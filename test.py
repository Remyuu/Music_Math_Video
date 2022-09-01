from manim import *
import pickle #写出读取打包 序列化二进制list

class sample_set:
    def get_winter_wav():
        with open('winter.libyy','rb') as pickle_file:
            #反序列化对象
            sample = pickle.load(pickle_file)
            
            return sample,max(sample)

    def get_sam():
        
        pass
class M_Shift(Scene):
    def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        for x in range(_len_sample):
            dots_set.append(Dot(radius=0.02,color=BLUE_A,fill_opacity=0.8))
            dots_set[x].move_to(axes.c2p(x,sample[x]))
            #self.add(dots_set[x])
            Vg.add(dots_set[x])
        return dots_set

    def drew_Manim_Graph(self,sample,windows_dot_num,shift):

            sample_part=sample[shift:shift+windows_dot_num]
            _big_ = max(sample)

            print("number of sample:"+str(len(sample))+"\ncurrent interval:"+str(shift)+","+str(shift+windows_dot_num))
            
            #### manim_graph ####
            axes = Axes(x_range=(0,windows_dot_num+1,512),
                y_range=(-_big_,_big_,round((_big_)/2)),
                axis_config={"include_numbers": True},)
        
            text_pos = VGroup(Text('Time Domain x_range:',font_size=22),
                          Text('['+str(shift)+','+str(shift+windows_dot_num)+']',font_size=22))

            text_pos.arrange(DOWN,aligned_edge=ORIGIN,buff=0.2).to_edge(UP)
        
            #np.hanning(windows_dot_num)

            ax_TOTAL = VGroup(axes).next_to(text_pos,DOWN)
            dots_set = self.Create_Dot_Set(axes,sample_part,ax_TOTAL)
            
            return ax_TOTAL,VGroup(*dots_set)

    def construct(self):
        ########################################################
        #                     GET SAMPLE                       #
        ########################################################
        sample,_abs_big_ = sample_set.get_winter_wav()
        windows_dot_num = 1024
        shift = 10000
        ax_TOTAL=VMobject();temp_ax_TOTAL = VMobject()
        text_pos=VMobject();temp_text_pos = VMobject()
        temp_ax_TOTAL,temp_text_pos=self.drew_Manim_Graph(sample,windows_dot_num,shift)

        for x in range(1):
            shift=int(shift+windows_dot_num/2)
            #self.remove(ax_TOTAL,text_pos)
            ax_TOTAL,text_pos=self.drew_Manim_Graph(sample,windows_dot_num,shift)
            self.play(temp_ax_TOTAL.animate.shift(LEFT))
            #self.play(Transform(temp_ax_TOTAL,ax_TOTAL),Transform(temp_text_pos,text_pos),run_time=1)

class qqq(Scene):
    def construct(self):
        ss = ImageMobject('youAndMe.jpg').scale(0.8)
        self.play(FadeIn(ss))
        self.play(ss.animate.shift(LEFT))