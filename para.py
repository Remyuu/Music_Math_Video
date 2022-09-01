# # from manim import *

# # class PlotParametricFunction(Scene):
# #     def func(self, t):
# #         return np.array((np.sin(2 * t), np.sin(3 * t), 0))

# #     def construct(self):
# #         func = ParametricFunction(self.func, t_range = np.array([0, TAU]), 
# #             use_smoothing=False,
# #             fill_opacity=0).set_color(RED)
# #         #self.add(func.scale(3))

# from manimlib import *

# class TransformPathArc(Scene):
#     def construct(self):
#         def make_arc_path(start, end, arc_angle):
#             points = []
#             p_fn = path_along_arc(arc_angle)
#             # alpha animates between 0.0 and 1.0, where 0.0
#             # is the beginning of the animation and 1.0 is the end.
#             for alpha in range(0, 11):
#                 points.append(p_fn(start, end, alpha / 10.0))
#             path = VMobject(stroke_color=YELLOW)
#             path.set_points_smoothly(points)
#             return path

#         left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
#         colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
#         # Positive angles move counter-clockwise, negative angles move clockwise.
#         examples = [-90, 0, 30, 90, 180, 270]
#         anims = []
#         for idx, angle in enumerate(examples):
#             left_c = left.copy().shift((3 - idx) * UP)
#             left_c.fill_color = colors[idx]
#             right_c = left_c.copy().shift(4 * RIGHT)
#             path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
#                                      arc_angle=angle * DEGREES)
#             desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
#             # Make the circles in front of the text in front of the arcs.
#             self.add(
#                 path_arc.set_z_index(1),
#                 desc.set_z_index(2),
#                 left_c.set_z_index(3),
#             )
#             anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

#         self.play(*anims, run_time=2)
#         self.wait()


# class ContinuousFourier(Scene):
#     def construct(self):
#         axes = Axes()
#         normal_graph = axes.get_graph(lambda x: np.cos(10*x),
#             x_range=[0,TAU]
#             ).to_edge(UP).scale(0.5)

#         polar_axix = PolarPlane()
#         polar_graph = polar_axix.get_parametric_curve(
#             lambda t : [
#                 np.cos(0.6*t) * (np.cos(10*t)+3-2),
#                 np.sin(0.6*t) * (np.cos(10*t)+3-2),
#                 0
#             ],
#             t_range=[0,TAU]
#         ).to_edge(DOWN)
#         self.add(axes,polar_axix)
#         self.add(normal_graph,polar_graph)
#         self.play(ReplacementTransform(normal_graph,polar_graph,
#             run_time=3.5,
#             path_arc = -TAU*3/5))
#         self.wait() 










from manim import *
import librosa
import numpy as np

class ContinuousFourier(Scene):
    def construct(self):
        second = 3
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
                +np.cos(1*t) * (f(t)),
                -np.sin(1*t) * (f(t)),
                0
            ],
            t_range=[0,second],
            stroke_color=[YELLOW,BLUE,PINK,BLUE_E]
        )
        group2 = VGroup(polar_axix,polar_graph)
        group2.to_edge(DL)

        self.add(axes,polar_axix,axes_label)
        self.add(normal_graph)
        self.play(ReplacementTransform(normal_graph,polar_graph),
            run_time=3.5,
            path_arc = -TAU*2/3)
        self.wait()
    
class i2gp_test(Scene):
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x : np.cos(x))

        position = ax.input_to_graph_point(x=PI, graph=curve)
        sq = Dot(color=YELLOW).move_to(position)

        self.add(ax, curve, sq)
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
            #mob.move_to(moving_dot.get_center())
            mob.move_to([mob.get_x()+0.01,-1,0])

        #为camera添加updater更新函数
        self.camera.frame.add_updater(update_cam_pos)
        #动画函数MoveAlongPath，传入运动的物体，路径graph。
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        #self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
        dd(*[
            Text(f"{temp}") 
            for temp in ['a','b','c']
        ])