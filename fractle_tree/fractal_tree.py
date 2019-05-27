import turtle

def draw_tree(len):
    turtle.forward(len)
    if len>5: #画出左边的枝干
        turtle.left(20)
        draw_tree(len-5)
    if len>5: #画出右边的枝干
        turtle.right(40)
        draw_tree(len-5)
    if len>5:
        turtle.left(20)
    turtle.backward(len) #返回本次分支的母结点



def main(len):
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    draw_tree(len)
    turtle.exitonclick() #单击退出


if __name__ == "__main__":
    len = int(input('请输入初始长度(px):'))
    print(type(len))
    main(len)