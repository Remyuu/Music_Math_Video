# from manim import *

# class LineExample(Scene):
#     def construct(self):
#         ax = Axes()
#         line1 = Line(ax.c2p(1,-3),ax.c2p(1,3),buff=0)
#         line2 = Line(ax.c2p(2,-3),ax.c2p(2,3),buff=1)
#         line3 = Line(ax.c2p(2,-3),ax.c2p(2,3),path_arc=PI)
#         self.add(ax,line1,line2,line3)

# class cir(Scene):
#     def construct(self):
#         cir = Circle(sheen_factor=1)
#         self.add(cir)
# from manim import *

# class RectangleExample(Scene):
#     def construct(self):
#         rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
#         rect2 = Rectangle(width=1.0, height=4.0)

#         rects = Group(rect1,rect2).arrange(buff=1)
#         self.add(rects)
# from manim import *

# class SquareExample(Scene):
#     def construct(self):
#         square = Square(side_length=2.0,color=BLUE,fill_opacity=1,sheen_factor=0.8)
#         self.add(square)




# from manim import *
# from manim import *

# class StarExample(Scene):
#     def construct(self):
#         pentagram = RegularPolygram(5, radius=2).to_edge(LEFT)
#         star = Star(outer_radius=2, color=RED).next_to(pentagram,RIGHT)
#         sum = VGroup(
#             pentagram.copy().to_edge(RIGHT),
#             star.copy().to_edge(RIGHT))
#         self.add(pentagram,star,sum)


# from manim import *

# class TriangleExample(Scene):
#     def construct(self):
#         triangle_1 = Triangle()
#         triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
#         tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
#         self.add(tri_group)




# from manim import *

# class SurroundingRectExample(Scene):
#     def construct(self):
#         title = Title("Fourier Transform")
#         quote = Text('''
# Generally speaking, the two ways to describe the same problem 
# can be called that they are the mutual transform to each other.
# ''',color=BLUE,
#         ).scale(0.75)
#         box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF,
#             corner_radius=1)

#         t2 = Tex(r"Hello World").scale(1.5)
#         box2 = SurroundingRectangle(t2, corner_radius=0.2)
#         mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
#         self.add(title, mobjects)
# from manim import *

# class UnderLine(Scene):
#     def construct(self):
#         man = MathTex("Manim \enspace Remoo")  # Full Word
#         ul = Underline(man)  # Underlining the word
#         self.add(man, ul)

# class aaa (Scene):
#     def construct(se):
#         aa = UnitInterval()
#         se.add(aa)




from manim import *

# class AxesExample(Scene):
#     def construct(self):
#         ax1 = Axes(
#             x_range=[-2*2*PI,2*2*PI,PI],
#             y_range=[-1,1,0.5],
#             x_length=6,
#             tips=True).to_edge(LEFT)
#         graph1 = ax1.plot(lambda x : np.sin(x))
#         ax2 = Axes(
#             x_range=[-1,4,1],
#             y_range=[-2,2,1],
#             x_length=6,
#             tips=False).to_edge(RIGHT)
#         graph2 = VGroup(*(Dot(ax2.c2p(x-1,2-x)) for x in range(5)))

#         self.add(ax1,graph1,ax2,graph2)




# class LogScalingExample(Scene):
#     def construct(self):
#         ax = Axes(
#             x_range=[0, 10, 1],
#             y_range=[-2, 6, 1],
#             tips=False,
#             axis_config={"include_numbers": True},
#             y_axis_config={"scaling": LogBase(custom_labels=True)},
#         )

#         graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10,0.01])
#         self.add(ax, graph)

# from manim import *

# class CoordsToPointExample(Scene):
#     def construct(self):
#         plane = NumberPlane(x_range=[-1,1,0.5])
#         dot_scene = Dot((2,2,0), color=RED)

#         self.add(plane, dot_scene)
from manim import *

class NumberPlaneExample(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(number_plane)