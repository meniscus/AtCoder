n,m = [int(i) for i in input().split()]

# 短針：12hで360deg => 1hで30deg => 1minで0.5deg
# 長針：1hで360deg => 1minで6deg

s_deg_by_origin = 30 * n + m * 0.5
l_deg_by_origin = m * 6

deg = l_deg_by_origin - s_deg_by_origin
if (deg < 0) :
    deg = s_deg_by_origin - l_deg_by_origin

print(min(deg%360, 360-(deg%360)))
# print(deg % 360)