# Introduction
Sounds have frequencies.
Here are two notes playing together,
```
1.  Show a sound icon, broadcast the sound.
```
or if we try to draw down the vibration of the air,
```
2.  Show f.
```
a periodic function.  That's what mathematicians call it.  We can see it from the graph, it is repeated, or periodic.

I can tell you that it is formed by 2 sine or cosine function, just as they come from two pure notes.
```
sin()+sin()
```
But what exactly?
```
?sin(?x)+?sin(?x)
```
A musician may recognize imidiately.  But not always.  And just looking at the graph, it doesn't seem obvious.
How are we going to solve it?  Fortunately, there's a method in mathematics called the **Fourier Transform**.
```
背景虚化，show 'Fourier Transform'
```
But before we look at how mathematicians deal with it, let's try to play with the wave ourself.
```
clear the screen
```
We try to build the sound ourselves.  We add 2 known sine or cosine functions, say, these two.
```
1.  In C_coordinate, show sin(x) first,
then add 2sin(4x).  Show also the formulas, one by one.
```
![](2022-08-04-18-33-32.png)

Or maybe these two.
```
sin(x)+0.5sin(8x)
```

![](2022-08-04-18-33-32.png)

Paterms can be seen as the intensity of the second wave is smaller, that adding periodic functions together looks like a *wave in a wave*.
```
Plot the first component inside the final sum-up graph.
```
An advantage of this paterms may be that, after mixing up together, the frequency property are preserved somehow, and being combined.  And the two components can be seen as interruption of each other, but not that destructive.

What I would like to say is that the idea of Fourier transform may have used this paterm.
```
clear screen
```

# Fourier Transform
Now we come to the mathematics.
```
Show text 'Fourier Transform'
```
Here is the core formula for the **Fourier Transform**.
```
Show the formula
```
We first focus on the two terms inside.
```
Leaves only f(t)e^.. , move to RIGHT.
Meanwhile, show the two coordinate system.
```
The f(t) is just our original sound function (+1).  t is time.  For explanation, we look at one note first, i.e. a single sine or cosine wave.
```
circumlate f(t)
f(t)->wave on cartessian coordinate
```
But also note that we would like to shift our function up a little bit, just to make things simpler.
```
f(t) shift up by 1.
```
And then for the exponential terms.
```
circumlate e^..
```
All we have to know is that it is a mathematical 简写 of spinning vector w.r.t time.
```
Show a 进度条 （一秒）。
Show a unit vector on the polar plane, 尖端显示e^..t
鼠标拖动进度条t的动画,vector随之移动,t in the e^.. t change
```
Together with 2pi and k, the vector swept 2 pi k radius Within the give time.  Here k is 0.4. So 0.4 * 2pi means 0.4 of a whole circle.
```
在polar plane上用圆弧箭头显示2pi*0.4跨度
```
Finally, multiplying f(t) with this just mean stretching this spining vector according to the magnitude of f(t).
```
加上f(t)后改变了轨迹。
鼠标拖动进度条动画,vector随之移动。
```
Or it can also be interpreted as we wound up the f(t) around on the plane as the trace of the vector, with the wounding frequency k = 0.4
```
wound up animation
```

Now coming back to our Fourier formula.
```
Add the integral sign on f(t)e^..  to complete the formula.
```
This simply meams finding the *Center of Mass* of the wound-up version of graph.
```
Circumlate the whole formula, meanwhile, show the CoM.
```
So for different k, we may get different CoM.
```
Change k animation, slowly
```
We can record and draw the distance of CoM from the origin, (but only x-coordinate).
```
Show frequency domain.
```
The important thing is that, when we wound the graph in a frequency that is just the true frequency of the original wave, the CoM will be far away from the origin.
```
k have moved to the spike value now.
```