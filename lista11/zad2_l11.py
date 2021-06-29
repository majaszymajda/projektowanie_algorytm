import matplotlib.pyplot as plt
from numpy import dot,array,empty_like
from matplotlib.path import Path


def make_path(x1,y1,x2,y2):
    return Path([[x1,y1],[x1,y2],[x2,y2],[x2,y1]])


def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )

    x3 = ((num / denom.astype(float))*db + b1)[0]
    y3 = ((num / denom.astype(float))*db + b1)[1]
    p1 = make_path(a1[0],a1[1],a2[0],a2[1])
    p2 = make_path(b1[0],b1[1],b2[0],b2[1])
    if p1.contains_point([x3,y3]) and p2.contains_point([x3,y3]):
        return x3,y3
    else:
        return False


def compare(point,vec1,vec2):
    new_point = point
    xpoint = point[0]
    if xpoint > vec1[0] and xpoint > vec2[1]:
        print("Punkt jest po prawej stronie")
    else:
        print("Punkt jest po lewej stronie")

    return True


point1 = [1, 2]
point2 = [3, 4]

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

point3 = [2, 2]
point4 = [1, 4]

x_values1 = [point3[0], point4[0]]
y_values1 = [point3[1], point4[1]]

fig, ax = plt.subplots()
ax.plot(x_values, y_values,'r')
ax.plot(x_values1, y_values1,'c')

p1 = array( [1, 2] )
p2 = array( [3,4] )

p3 = array( [2,2] )
p4 = array( [1,4] )

cross_point = seg_intersect( p1,p2, p3,p4)
ax.scatter(cross_point[0],cross_point[1])
ax.annotate("   Cross point", cross_point)
userpointx = -10
userpointy = -12
ax.scatter(userpointx,userpointy)
userpoint = [userpointx,userpointy]
compare(userpoint,point1,point2)

plt.show()