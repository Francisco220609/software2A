from turtle import *
color('purple', 'red')
begin_fill()
while True:
    forward(300)
    left(19)
    if abs(pos()) < 1:
        break
end_fill()
done()