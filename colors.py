BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREY = (192, 192, 192)
GOLD = (255, 223, 50)
COLOR2 = (245, 245, 245)
COLOR4 = (255, 228, 196)
COLOR8 = (242, 177, 121)
COLOR16 = (245, 149, 99)
COLOR32 = (246, 124, 95)
COLOR64 = (246, 94, 59)
COLOR128 = (237, 207, 114)
COLOR256 = (237, 204, 97)
COLOR512 = (237, 200, 80)
COLOR1024 = (237, 197, 63)
COLOR2048 = (237, 194, 46)
COLOR4096 = (139, 69, 19)

def ColorChoose(block):
    if block==2:
        return COLOR2
    elif block ==4:
        return COLOR4
    elif block == 8:
        return COLOR8
    elif block == 16:
        return COLOR16
    elif block == 32:
        return COLOR32
    elif block == 64:
        return COLOR64
    elif block == 128:
        return COLOR128
    elif block == 256:
        return COLOR256
    elif block == 512:
        return COLOR512
    elif block == 1024:
        return COLOR1024
    elif block == 2048:
        return COLOR2048
    elif blick == 4096:
        return COLOR4096
    else:
        return GREY
    
