#Amir Abbas Fattahi - Thursday 14-18 class
#tamrin hazf horoof sedadar
silents = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z,  ".split(", ")
jomle = input("jomle khod ra vared konid:\n")
for item in jomle:
    if item in silents:
        print(item, end="")
