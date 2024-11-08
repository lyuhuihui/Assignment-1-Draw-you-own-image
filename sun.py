from  turtle import *
import math

bgcolor("skyblue")
def draw_sun(x, y, radius, rays):
    # 画太阳的圆形部分

    pensize(5)
    hideturtle()  # 隐藏海龟图标
    penup()
    hideturtle()
    speed(8)
    goto(x, y - radius)  # 将海龟移动到圆的底部中心
    pendown()
    color("yellow")
    pensize(5)
    begin_fill()
    circle(radius)  # 画圆
    end_fill()

    # 画太阳的光线
    for _ in range(rays):
        speed(6)
        penup()
        goto(x, y)  # 移到太阳的中心
        hideturtle()
        pensize(5)
        pendown()
        forward(radius)  # 向外移动到圆的边缘
        pendown()
        forward(30)  # 画光线
        penup()
        backward(radius + 20)  # 返回中心
        right(360 / rays)  # 旋转
    done()  # 结束绘制
# 绘制小熊的头
def draw_circle(color, x, y, radius):
    penup()
    speed(12)
    pensize(3)
    fillcolor(color)
    goto(x, y)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()


# 绘制小熊的耳朵
def draw_ear(color, x, y):
    draw_circle(color, x, y, 30)

# 绘制小熊的身体
def draw_body():
    draw_circle("brown", 0, -150, 70)  # 身体

# 绘制小熊的脸
def draw_face():
    draw_circle("brown", 0, -50, 50)  # 脸
    draw_circle("black", -20, 0, 5)  # 左眼
    draw_circle("black", 20, 0, 5)  # 右眼
    penup()
    goto(0, -35)
    pendown()
    fillcolor("pink")
    begin_fill()
    circle(10)  # 鼻子
    end_fill()

# 绘制小熊的耳朵
def draw_ears():
    draw_ear("brown", -50, 0)  # 左耳
    draw_ear("brown", 50, 0)   # 右耳

# 绘制小熊
def draw_pic():
    draw_body()
    draw_ears()
    draw_face()

# 开始绘制
draw_pic()
draw_sun(-200, 200, 50, 12)







