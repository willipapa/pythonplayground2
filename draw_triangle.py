"""
draw_triangle.py
绘制三角形的程序
Willipapa
"""
import turtle

def draw_triangle(x1, y1, x2, y2, x3, y3, t ):  #定义画三角形的方法
    #尝试绘制一个三角形
    t.up()              #抬笔
    t.setpos(x1, y1)    #移动到坐标(x1, y1),没有画线
    t.down()            #下笔
    t.setpos(x2, y2)    #移动到坐标(x2, y2),有画线
    t.setpos(x3, y3)
    t.setpos(x1, y1)
    t.up()

def main():
    print('testing turtle graphics...')

    t = turtle.Turtle()
    t.hideturtle()
    draw_triangle(-100, 0, 0, -173.2, 100, 0, t)
    turtle.mainloop() 

# 调用main函数
if __name__ == '__main__':
    """__name__ == '__main__'这个条件判断通常用于确定代码是否在作为脚本直接运行，而不是作为模块被导入。
    如果条件为真，即__name__等于'__main__'，那么接下来的代码块将会被执行；如果为假，则不会执行。
    这种用法在Python脚本中非常常见，因为它允许脚本在被直接运行时执行某些操作，同时也可以作为模块被其他脚本导入而不会执行这些操作。
    """
    main()
