本篇文章从律学开始，从十二平均律出发，介绍一些基础必要的乐理知识，然后编写python文件，输出和弦音频文件。


<!--more-->


# 乐理知识部分：

# 一、[律学简述](https://baike.baidu.com/item/%E5%BE%8B%E5%AD%A6/74940?fr=aladdin)(temperament)

##   1、概论

  律学，又称“音律学”，是研究律制构成与应用的科学。律学须对音乐所用的音律进行研究。音乐所用的音绝大多数是确定的，[律制](https://baike.baidu.com/item/%E5%BE%8B%E5%88%B6/6785021)则是以某特定[音程](https://baike.baidu.com/item/%E9%9F%B3%E7%A8%8B/18483922)为基础，用[数学](https://baike.baidu.com/item/%E6%95%B0%E5%AD%A6)方法规定的一系列乐音的体系。体系中的每个单位称为“律”；[音阶](https://baike.baidu.com/item/%E9%9F%B3%E9%98%B6/135355)是按照音程关系的一定规格从律制中选择若干律而构成的音列，其中的每个单位称为“音”。“音”与“律”合称“音律”时，除指律制外，兼指作精确规定的所有乐音。 ----百度百科

  简而言之，律就是用数学的方法规定各个音高（不止）的振动频率。“律”是构成律制的基本单位。“律”和“音”的概念相近但略有不同，律制中每个单位称为“律”，而音阶中每个单位称为“音”，律制与音阶的关系十分密切。

##   2、律的计算

  音律计算法即音程的计算法，使用频率比或音程值（interval value）来表示和计算音程的大小。

  从古至今，律法不断更替。不同的律制由不同的生律法决定。

  音程值（interval value）有四种，分别为对数值、八度值、音分值和平均音程值。

##   3、五度相生律（circle-of-fifths system）

  五度相生律，规定构成纯五度音程的两个音的频率规定为2:3。这种每隔五度产生一律，继续相生而得各律的做法，称为“五度相生法”。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/02926865-c0f8-4b33-8252-8a1a16dc40de)


  其中，由于最大音差的存在，使五度相生律无法在十二律上循环构成各调音阶，即从主音出发，生律十二次（或更多次）并纳入同一八度后，无法回到主音，这对五度相生律的使用造成了一定障碍。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/6d89f2d1-8f93-4efe-b581-8e1c154e1b8b)


##   4、纯律（just intonation）

  其中音阶中音符的频率是由小整数的比率得出的。在这个系统中，音符之间的音程是基于简单的数字比例，例如八度音程为2:1，完美五度音程为3:2，完美四度音程为4:3。这些比例创造出和谐纯净的音程，据说比现代西方音乐中使用的等温调音系统产生的音色更自然、更悦耳。

##   5、十二平均律（twelve-tone equal temperament）

  十二平均律是把一个八度均分为频率比相等的十二个半音的律制，又称为“十二等比律”。

  接下来我们所有代码都是采用十二平均律的。原因是，钢琴就是基于十二平均律设计的。

  百度百科写道：十二平均律最早是由我国明朝科学家[朱载堉](https://baike.baidu.com/item/%E6%9C%B1%E8%BD%BD%E5%A0%89/1182870)发现（1584年）。后通过丝绸之路传至西方。

  1605年荷兰数学家[西蒙·斯特芬](https://zh.m.wikipedia.org/wiki/%E8%A5%BF%E8%92%99%C2%B7%E6%96%AF%E7%89%B9%E8%8A%AC "西蒙·斯特芬")在一篇未完成的手稿“Van de Spiegheling der singconst”提出用

$$
\sqrt[12]{\frac{1}{2} }
$$

  计算十二平均律，但因计算精度不够，他算出的弦长数字，有些偏离正确数字一至二单位之多。

  一个八度的频率比为2:1，则十二平均律各律之间的频率比应为：$\sqrt[12]{2} =1.05946122  $

  在音乐实践中，当时的音乐家已深知十二平均律的便利之处，各国的作曲家、演奏家都开始使用十二平均律，同时也致力于十二平均律的开发。例如德国的巴赫（J.S.Bach），作有《十二平均律钢琴曲集》二卷，此二卷虽并非只使用了十二平均律（还使用了一些不规则律），但被认为是充分发挥十二平均律的效能，可以自由转调的典范作品。

##   6、三种律制的比较

  三种律制各有其优缺点。十二平均律解决了五度相生律和纯律中存在的一些矛盾，例如不断增加律数仍无法回到出发律的矛盾，但十二平均律又会影响音程的和谐性。总体而言，十二平均律将五度相生律和纯律加以调和与折衷，介于两者之间而又更接近五度相生律。十二平均律是目前使用最为广泛的一种律制。

# 二、基础乐理----p1----乐音体系及分组



##   1、音乐体系、音列

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/25a609ec-49de-46a6-be40-bc3ac3cea6b0)


  钢琴有88个键。这些乐音加起来的总和叫做--音乐体系。

  从低到高排起来叫做--音列。

##   2、音名

  在乐音体系中，每个乐音都有其固定名称，即：音名 。通常用字母C、D、E、F、G、A、B来表示。

  这七个音级也称为基本音级，在钢琴键盘上的位置是固定不变的。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/02173217-596b-4949-bd8f-b2826dac5578)


##   3、音的分组

  钢琴划分不同的区域。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/3e454ffe-0e50-43c4-a238-fe010d68d961)


  钢琴键盘上中央C开始的这一音组称为小字一组，也是“轴心组”。小字一组往右方依次称为小字二组、小字三组、小字四组、小字五组；小字一组往左方依次称为小字组、大字组、大字一组、大字二组

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/9f49b9cf-243b-46f8-b266-da91dff4a7b1)


# 三、基础乐理----p2----五线谱&音符


##   1、谱表

  谱表由五线四间构成，用于记录音符高低。由于谱表有五条等距离平行横线，因此称为五线谱。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/6c7935d4-5915-4e9d-9172-ccf19b6f8e77)


##   2、谱号

  这里简单认识一下高音谱号就好了。除此，还有低音谱号、中音谱号。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/0665d456-a3d4-4a27-9efb-72743bc63b7d)


![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/49c8f9b5-d00e-46cd-aa36-bd82855d3b5e)


##   3、音符

  音符由三部分组成：符头（空心或实心的椭圆形符号）、符干（短竖线）和符尾（符干右侧的小弧线）。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/4cf58ec8-875e-47bf-bf96-77131d2307dd)


![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/dd661a3b-45b7-4087-8559-621717498779)


##   4、休止符

  休止符是用来表示音乐休止、间断的符号。

  在音乐进行中，休止符虽然表示短暂的无声，但此时有着特殊的意义，而且音乐并没有中断，因此休止符是音乐作品中的重要组成部分之一。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/1481c4e8-1af6-4943-9f17-fb2dd3570faa)


##   5、拍号

  分子的数字代码一个小节有多少拍，分母的数字代表一几分音符为一拍。读法注意不能读作几分之几拍！

  此外，拍号还明确了旋律的强弱变化规律。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/610d15d1-ace6-4e25-a5c8-9d97618935be)


# 四、基础乐理----p3----音程


##   1、音程

  两个音之间音高距离就叫做音程。

  音程分为两种：旋律音程、和声音程。

  简而言之，旋律音程是两个音先后发出声响。而和声音程指的是同时发出。

##   2、旋律音程

  按照发声先后读。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/c254decb-ee80-4b8e-8a9c-bf9699e5f39f)


##   3、和声音程

  下方的音称为根音，上方的音称为冠音。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/6a6c1c65-54e7-40af-84d4-cf09d3fffd3b)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/6efe9417-e0d5-4544-a0d2-55fe9a37767a)



##   4、协和音程与不协和和音程

  协和音程的音响效果听起来悦耳动听、声音融合，可分为完全协和音程和不完全协和音程。

  完全协和音程包括纯一度、纯四度、纯五度、纯八度；不完全协和音程包括小三度、大三度、小六度、大六度。

  纯八度的音响听起来非常融合，像一个音的声音，也因为过于融合声音听起来会比较空洞。

  纯一、纯四度、纯五度音程比起纯八度的音响效果略显饱满一些，但也显空洞。

  因此，所有纯音程（纯一度、纯四度、纯五度、纯八度）都是完全协和音程。

  不协和音程的音响比较刺耳，听起来紧张、不稳定，如大小二度、大小七度、增四度、减五度等音程。

  不协和音程虽然音响效果尖锐，但是它在音乐作品中也是构成乐曲的重要元素。

# 五、基础乐理----p4----调式

##   1、调式

  若干高低不同的乐音，围绕某一具有稳定感的中心音（主音），按照一定关系组织起来所构成的体系，称为调式。现在世界上应用最广泛的调式是大小调式。

  其中，巴赫的《十二平均律》更是大小调式的经典中的经典。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/e9f9e087-9062-4a6a-a6de-bbde803a5f82)


##   2、主音

  在调式中，主音是处于核心地位的中心音，其稳定感最强，其他的音都倾向于它。在歌（乐）曲中，主音常出现在强拍、音较长或终止处。

##   3、大调式

  大调式简称为“大调”，由七个音级构成。它的主音与Ⅲ级音之间为大三度音程关系，这个大三度也是大调式的特征所在。其中Ⅰ、Ⅲ、Ⅴ级音构成大三和弦，因此大调式的色彩是明亮、辉煌的。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/bff55698-6647-4eb8-8c9d-2e667352a301)


  大调式共有三种类型：自然大调、和声大调和旋律大调。

###     1、自然大调

    自然大调是大调中用得最多的一种，全部由自然音级构成。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/e0fb0b1a-b645-4203-a9cd-8eba0473d911)


    自然大调音阶由五个全音和两个半音组成，

    其音阶结构是：全音-全音-半音-全音-全音-全音-半音，即由大二度、大二度、小二度、大二度、大二度、大二度、小二度音程组成。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/b54c9ed2-5523-42f4-80a9-bb19cffd8b3f)


**      C和D之间隔了一个音（黑键），所以CD叫全音。**

**      E和F之间没有间隔，所以叫半音。**

    为了便于熟记，自然大调编成口诀为：全、全、半、全、全、全、半。

    即我们平时说的：de re mi fa sol la si

    C自然大调如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/99ef15dd-ff22-4faa-a370-00c23852b754)


###     2、和声大调

    在自然大调音阶的基础上，将第Ⅵ级音降低半音，即为和声大调。

    其特征是降Ⅵ级音与Ⅶ级音之间所形成的增二度音程。

    这个增二度即为判断和声大调的标志，也是和声大调的特征所在。

    C和声大调音阶如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/f7231dc3-545b-4b0d-bd2e-e9ce435e0d2b)


###     3、旋律大调

    在自然大调音阶的基础上，将第Ⅵ级音降低半音，即为旋律大调。

    其特征是降Ⅵ级音与Ⅶ级音之间所形成的增二度音程。

    这个增二度即为判断和声大调的标志，也是和声大调的特征所在。

    C旋律大调音阶如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/387ad7d7-2dc4-4d2b-aa5d-bfe69004bd43)


##   4、小调式

  小调式简称为“小调”，也是由七个音级构成。

  它的主音与Ⅲ级音之间为小三度音程关系，这个小三度也是小调式的特征所在。其中Ⅰ、Ⅲ、Ⅴ级音构成小三和弦，因此小调式的色彩是柔和、暗淡的。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/31bda838-4454-4f2f-93cb-92c0811ec403)


  小调也有三种类型：自然小调、和声小调和旋律小调。

###     1、自然小调

    自然小调音阶也由五个全音和两个半音组成，其音阶结构是全音-半音-全音-全音-半音-全音-全音，即由大二度、小二度、大二度、大二度、小二度、大二度、大二度音程组成。

    a自然小调如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/abe9617d-349b-4e5f-ab9b-5c3b80424c04)


    为了便于熟记，编成口诀为：全、半、全、全、半、全、全。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/7e3adec5-5b8b-4f3a-a9b6-6e90e13fd010)


###     2、和声小调

    在自然小调音阶的基础上，将第Ⅶ级音升高半音，即为和声小调。

    其特征是Ⅵ级音与升Ⅶ级音之间所形成的增二度音程，并且Ⅶ级音在升高半音之后具有了导音倾向于主音的功能，和自然小调相比紧张度更大。

    a和声小调如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/92cda83c-6622-4769-8617-48aeeed13828)


###     3、旋律小调

    在自然小调音阶的基础上，将自然小调上行音阶中的第Ⅵ级和第Ⅶ级升高半音，下行音阶中再将这两个音还原，即为旋律小调。

    a旋律小调如下图所示：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/2e55ed12-6932-409e-a175-2f062039a427)


# 六、基础乐理----p5----调号


##   1、调号

  调号作为表示一首歌（乐）曲的调高（即主音高度）的符号，位于每行谱表起首处（谱号之后）或乐曲进行中出现新调的地方。

  调号是用升、降记号来记写的。

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/22b19363-077a-4cf3-ab25-4bee7b87c1f9)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/f438945f-d01c-4b47-99cf-cd02291e45e6)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/7f89d197-72c2-4bc4-a619-4054ef454b41)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/edc23410-0105-413c-90e9-3aa9c9886460)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/14e922f2-e179-4522-a4b8-91edc3f62295)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/7b3be557-d4eb-46a8-90b3-b2b1315613d6)

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/e89491dc-2474-445f-8b47-60809c6552ba)


![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/7d3d752e-5aaf-4dc5-9ea5-ae43b117faee)



# **python编曲部分：**

# 一、认识MIDO库


## 1、导入mido

`from mido import Message,MidiFile,MidiTrack`

## 2、mido基本框架

创建两个mido库的对象：MidiFile() , MidiTrack()

前者用于编辑、生成、输出Midi文件，后者用于midi文件轨道编辑。

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

在轨道对象中添加信息，'program\_change'意为切换轨道。

直观理解就是：编辑某条轨道前需要先把轨道选好。（此为官方固定套路，看不懂也无所谓，照着写即可）

    track.append(Message('program_change', program=0, time=0))

## 3、编写音符

选好轨道之后，直接在轨道上添加音符即可。注意，此处的时间单位是毫秒。

    track.append(Message('note_on', note=60, velocity=64, time=0))

添加完后再添加一条结束标记，此处才算真正完成一个音符的书写。

    track.append(Message('note_off', note=60, velocity=64, time=2000))

添加完以后，就可以直接生成一个midi文件了

    mid.save('MyFirstDamnSong.mid')

## 4、代码

代码如下：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/1db20f52-2a2b-4f3a-a7ab-494a8d21fae7)


# 二、结合乐理


## 1、midi文件频率编号表格：

![image](https://github.com/Remyuu/Music_Math_Video/assets/64857501/13df8ea7-e7fe-46e5-8def-db2481a4fa73)


由上表可知，中央C的midi编号是60 。

## 2、编写工具库

###   1、任务分析

  我们首先编写一个工具库`Notes_Toolbox.py`，定义一些常用的，根基的东西。

  定义好基础的东西：音程、音名、调式、和弦、节拍、基础音等等。

  然后编写一些简单的方法供调用，比如返回一组和弦、自动转调、通过五线谱得到MIDI频率编号等方法。

###   2、定义变量

<table style="border-collapse: collapse; width: 100%; height: 210px;" border="1">
<tbody>
<tr style="height: 21px;">
<td style="width: 4%; text-align: center; height: 21px;">编号</td>
<td style="width: 13%; height: 21px; text-align: center;">变量名</td>
<td style="width: 8%; height: 21px; text-align: center;">Is static？</td>
<td style="width: 26.402%; height: 21px;">Default value</td>
<td style="width: 47.4308%; height: 21px;">作用</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;"><span style="font-family: 'Microsoft YaHei';">1<br /></span></td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">bpm</span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">No<br /></span></td>
<td style="width: 26.402%; height: 21px;">125</td>
<td style="width: 47.4308%; height: 21px;">节拍</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">2</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">timePerBeat</span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">No</td>
<td style="width: 26.402%; height: 21px;">60 / bpm * 100</td>
<td style="width: 47.4308%; height: 21px;">每拍持续时间（毫秒）</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">3</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">base_note</span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;">60</td>
<td style="width: 47.4308%; height: 21px;">中央C对应MIDI编号</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">4</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">note_name[] </span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;">
<div>
<div>[&nbsp;'C','D','E','F','G','A','B']</div>
</div>
</td>
<td style="width: 47.4308%; height: 21px;">音名</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">5</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">major_notes[] </span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;">
<div>
<div>&nbsp;[0, 2, 2, 1, 2, 2, 2, 1]</div>
</div>
</td>
<td style="width: 47.4308%; height: 21px;">自然音阶</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">6</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">Cmajor_notes[] </span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;"><span style="text-decoration: underline;">&lt;intermediate variable&gt;</span></td>
<td style="width: 47.4308%; height: 21px;">&nbsp;</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">7</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">Eflatmajor_notes[] </span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;"><span style="text-decoration: underline;">&lt;intermediate variable&gt;</span></td>
<td style="width: 47.4308%; height: 21px;">&nbsp;</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">8</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">Cmajor{} </span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;">
<div>
<div>{'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71}</div>
</div>
</td>
<td style="width: 47.4308%; height: 21px;">C大调字典</td>
</tr>
<tr style="height: 21px;">
<td style="width: 4.58585%; text-align: center; height: 21px;">9</td>
<td style="width: 12.8404%; height: 21px; text-align: center;"><span style="font-family: 'Microsoft YaHei';">Eflatmajor{}</span></td>
<td style="width: 8.71256%; height: 21px; text-align: center;">static</td>
<td style="width: 26.402%; height: 21px;">
<div>
<div>{'C': 63, 'D': 65, 'E': 67, 'F': 68, 'G': 70, 'A': 72, 'B': 74}</div>
</div>
</td>
<td style="width: 47.4308%; height: 21px;">E小调字典</td>
</tr>
<tr>
<td style="width: 4.58585%; text-align: center;">...</td>
<td style="width: 12.8404%; text-align: center;"><span style="font-family: 'Microsoft YaHei';">...<br /></span></td>
<td style="width: 8.71256%; text-align: center;">...</td>
<td style="width: 26.402%;">
<div>
<div>...</div>
</div>
</td>
<td style="width: 47.4308%;">...</td>
</tr>
</tbody>
</table>



###   3、定义函数

<table style="border-collapse: collapse; width: 99.9694%;" border="1">
<tbody>
<tr>
<td style="width: 4.58585%; text-align: center; height: 21px;">编号</td>
<td style="width: 12.7749%; height: 21px; text-align: center;">方法名</td>
<td style="width: 13.0369%; height: 21px; text-align: center;">返回</td>
<td style="width: 16.9043%; height: 21px;">传入参数</td>
<td style="width: 52.6697%; height: 21px;">作用</td>
</tr>
<tr>
<td style="width: 4.58585%; text-align: center; height: 21px;"><span style="font-family: 'Microsoft YaHei';">1<br /></span></td>
<td style="width: 12.7749%; height: 21px; text-align: center;">
<div>
<div>get_note</div>
</div>
</td>
<td style="width: 13.0369%; height: 21px; text-align: center;">
<div>
<div>MIDI编号</div>
</div>
</td>
<td style="width: 16.9043%; height: 21px;">
<div>
<div>note,group=0,**kw</div>
</div>
</td>
<td style="width: 52.6697%; height: 21px;">输入音名与音符区域，返回对应的MIDI编号。（需要改进，没有黑键）</td>
</tr>
<tr>
<td style="width: 4.58585%; text-align: center; height: 21px;">2</td>
<td style="width: 12.7749%; height: 21px; text-align: center;">
<div>
<div>get_chord</div>
</div>
</td>
<td style="width: 13.0369%; height: 21px; text-align: center;">和弦数组</td>
<td style="width: 16.9043%; height: 21px;">
<div>
<div>name，**kw</div>
</div>
</td>
<td style="width: 52.6697%; height: 21px;">输入和弦名称，返回和弦数组</td>
</tr>
<tr>
<td style="width: 4.58585%; text-align: center;">3</td>
<td style="width: 12.7749%; text-align: center;">
<div>
<div>
<div>
<div>originToEflatMajor</div>
</div>
</div>
</div>
</td>
<td style="width: 13.0369%; text-align: center;">新E小调MIDI编号数组</td>
<td style="width: 16.9043%;">
<div>
<div>
<div>
<div>list,**kw</div>
</div>
</div>
</div>
</td>
<td style="width: 52.6697%;">输入C大调，返回E小调。（需要改进，支持指定什么调到什么调）</td>
</tr>
<tr>
<td style="width: 4.58585%; text-align: center;">...</td>
<td style="width: 12.7749%; text-align: center;">
<div>
<div>...</div>
</div>
</td>
<td style="width: 13.0369%; text-align: center;">...</td>
<td style="width: 16.9043%;">
<div>
<div>...</div>
</div>
</td>
<td style="width: 52.6697%;">...</td>
</tr>
</tbody>
</table>



    bpm = 125 #why 125:
        #bpm = 1 * 1000 / 8 
    timePerBeat = 60 / bpm * 1000
    base_note = 60 # C4
    note_name =[
        'C','D','E','F','G','A','B'
    ]
    
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    Cmajor_notes = []
    Eflatmajor_notes = []
    
    for num in range(12):
        Cmajor_notes.append(base_note+sum(major_notes[0:num+1]))
        Eflatmajor_notes.append(base_note+3+sum(major_notes[0:num+1]))
    #这里只有一个区
    Cmajor = dict(zip(note_name,Cmajor_notes))
    # Cmajor = {'C':60,'D':62,'E':64,'F':65,'G':67,'A':69,'B':71}
    Eflatmajor = dict(zip(note_name,Eflatmajor_notes))
    # Eflatmajor = {'C': 63, 'D': 65, 'E': 67, 'F': 68, 'G': 70, 'A': 72, 'B': 74}
    
    def get_note(note,group=0,**kw):#Group = 0 means 4Group
        global base_note,major_notes
        return base_note + group*12 + sum(major_notes[0,note])
    
    def originToEflatMajor(list,**kw):
        Ef=[]
        for x in list:
            Ef.append(x+3)
        return Ef
    
    #get_note(1,group=0) return 60
    #get_note(2,group=0) return 62
    def get_chord(name):
        chord = {
            "Major3":[0,4,7,12],#大三和弦
            "Minor3":[0,3,7,12],#小三和弦
            "Augmented3":[0,4,8,12],#增三和弦
            "Diminished3":[0,3,6,12],#减三和弦
    
            "M7":[0,4,7,11],#大七和弦
            "Mm7":[0,4,7,10],#属七和弦
            "m7":[0,3,7,10],#小七和弦
            "mM7":[],
            #...
        }
        return chord[name]
    #get_chord(“Major”) return [0,4,7,12]

## 3、写一段分解和弦

上面已经写完了工具类模块，接下来就可以专注于和弦的部分了。

###   1、编写输出和弦函数

  输出分解和弦到midi文件

  使用此方法时，需要传入：

<table style="border-collapse: collapse; width: 99.9694%;" border="1">
<tbody>
<tr>
<td style="width: 4.91347%; text-align: center;">编号</td>
<td style="width: 15.068%;">参数名：</td>
<td style="width: 21.3622%;">传入：</td>
<td style="width: 58.6291%;">示例：</td>
</tr>
<tr>
<td style="width: 4.91347%; text-align: center;">1</td>
<td style="width: 15.068%;">track&nbsp;</td>
<td style="width: 21.3622%;">mido库的输出音频接口</td>
<td style="width: 58.6291%;">MidiTrack()</td>
</tr>
<tr>
<td style="width: 4.91347%; text-align: center;">2</td>
<td style="width: 15.068%;">root&nbsp;</td>
<td style="width: 21.3622%;">音符的名称</td>
<td style="width: 58.6291%;">&nbsp;'C','D','E','F','G','A','B'</td>
</tr>
<tr>
<td style="width: 4.91347%; text-align: center;">3</td>
<td style="width: 15.068%;">name&nbsp;</td>
<td style="width: 21.3622%;">和弦的名称，在Notes_Toolbox中定义</td>
<td style="width: 58.6291%;">'Major3'...</td>
</tr>
<tr>
<td style="width: 4.91347%; text-align: center;">4</td>
<td style="width: 15.068%;">format&nbsp;</td>
<td style="width: 21.3622%;">输出分解和弦的方式</td>
<td style="width: 58.6291%;">[0,1,2] [1,3,2,3]...</td>
</tr>
<tr>
<td style="width: 4.91347%; text-align: center;">5</td>
<td style="width: 15.068%;">length&nbsp;</td>
<td style="width: 21.3622%;">音符持续的时长</td>
<td style="width: 58.6291%;">4</td>
</tr>
</tbody>
</table>



  直接放上源代码：


    def add_broken_chord(root, name, format, length, track, tone_name='Cmajor', root_base=0, channel=0):
        #默认是c大调
        root_num = Notes_Toolbox.Cmajor
        if tone_name == 'Eflat':
            root_num = {'C': 63, 'D': 65, 'E': 67, 'F': 68, 'G': 70, 'A': 72, 'B': 74}
        root_note = root_num[root] + root_base*12  # 分解和弦的根音
        
        time = (length * 480) / len(format)  # 此处为官方文档写法，我也不懂，time指的是音符持续时长
        for broken_chord in format:  # 通过for循环，逐个输出和弦的音符
            note = root_note + Notes_Toolbox.get_chord(name)[broken_chord]
            track.append(Message('note_on', note=note,
                         velocity=60, time=0, channel=channel))
            track.append(Message('note_on', note=note, velocity=60,
                         time=round(time), channel=channel))

###    2、调用参考：

    format = [0, 1, 2, 3]
    add_broken_chord('C', 'Major3', format, 4, track)
    add_broken_chord('C', 'Minor3', format, 4, track)
    add_broken_chord('C', 'Augmented3', format, 4, track)
    add_broken_chord('C', 'Diminished3', format, 4, track)
    add_broken_chord('C', 'Diminished3', format, 4, track)

  最后调用保存midi文件即可。

* * *

* * *

# 三、规范化代码

为了方便调用，我们对函数的参数顺序做出调整。

另外，重载play\_note方法，使其可以接收int类型的note（也就是直接输入MIDI编号）。

同理，所有的有关note的输入都可以进行重载。

    def play_note(note,  track, length=1, tone_name='Cmajor', root_base=0, delay=0, velocity=1.0, channel=0):
        ...
        
    def play_note(note:int,  track, length=1, tone_name='Cmajor', root_base=0, delay=0, velocity=1.0, channel=0):
        ...
        
    def play_broken_chord(root, name, format, track,length=1, tone_name='Cmajor', delay=0, velocity=1.0,root_base=0, channel=0):
        ...

* * *

* * *

# 四、总结、mido之旅未完待续...

  经过上述学习与实践，浅显地了解了音乐与数学的联系，与一些基础乐理知识。通过代码，实现了各种和弦的输出。

  结合乐理知识，接下来，将进行圈式和弦的书写。

* * *

## 参考文献

\[1\]. 《[音乐理论基础](https://www.zhihu.com/search?q=%E9%9F%B3%E4%B9%90%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A128328022%7D)》，李重光编著，人民音乐出版社；

[1]: https://remoooo.com/usr/uploads/2022/10/2803310720.png
[2]: https://remoooo.com/usr/uploads/2022/10/3208967430.png
[3]: https://remoooo.com/usr/uploads/2022/10/4008680871.png
[4]: https://remoooo.com/usr/uploads/2022/10/909759569.png
[5]: https://remoooo.com/usr/uploads/2022/10/149839181.png
[6]: https://remoooo.com/usr/uploads/2022/10/4134451402.png
[7]: https://remoooo.com/usr/uploads/2022/10/25836825.png
[8]: https://remoooo.com/usr/uploads/2022/10/276565512.png
[9]: https://remoooo.com/usr/uploads/2022/10/2563129835.png
[10]: https://remoooo.com/usr/uploads/2022/10/3759337357.png
[11]: https://remoooo.com/usr/uploads/2022/10/2175240129.png
[12]: https://remoooo.com/usr/uploads/2022/10/1535159131.png
[13]: https://remoooo.com/usr/uploads/2022/10/2159351125.png
[14]: https://remoooo.com/usr/uploads/2022/10/1105095640.png
[15]: https://remoooo.com/usr/uploads/2022/10/3829794185.png
[16]: https://remoooo.com/usr/uploads/2022/10/3010404871.png
[17]: https://remoooo.com/usr/uploads/2022/10/283484227.png
[18]: https://remoooo.com/usr/uploads/2022/10/85772124.png
[19]: https://remoooo.com/usr/uploads/2022/10/2983346726.png
[20]: https://remoooo.com/usr/uploads/2022/10/2564364.png
[21]: https://remoooo.com/usr/uploads/2022/10/2939495906.png
[22]: https://remoooo.com/usr/uploads/2022/10/3114562946.png
[23]: https://remoooo.com/usr/uploads/2022/10/3547842155.png
[24]: https://remoooo.com/usr/uploads/2022/10/1071538497.png
[25]: https://remoooo.com/usr/uploads/2022/10/345525854.png
[26]: https://remoooo.com/usr/uploads/2022/10/117923879.png
[27]: https://remoooo.com/usr/uploads/2022/10/2105909465.png
[28]: https://remoooo.com/usr/uploads/2022/10/3397544722.png
[29]: https://remoooo.com/usr/uploads/2022/10/49554152.png
[30]: https://remoooo.com/usr/uploads/2022/10/4292335931.png
[31]: https://remoooo.com/usr/uploads/2022/10/273861735.png
[32]: https://remoooo.com/usr/uploads/2022/10/1259784051.png
[33]: https://remoooo.com/usr/uploads/2022/10/1456331981.png
[34]: https://remoooo.com/usr/uploads/2022/10/966161410.png
[35]: https://remoooo.com/usr/uploads/2022/10/2081878802.png
[36]: https://remoooo.com/usr/uploads/2022/10/344355925.png
[37]: https://remoooo.com/usr/uploads/2022/10/3880419636.png
