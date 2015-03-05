from PIL import Image
with Image.open('test2.png') as im:
    im_width, im_height = im.size
    r_vals = []
    g_vals = []
    b_vals = []
    x_vals = []
    for x in range(im_width):
        for y in range(im_height):
            r_vals.append(im.getpixel((x, y))[0])
            g_vals.append(im.getpixel((x, y))[1])
            b_vals.append(im.getpixel((x, y))[2])
            x_vals.append(im.getpixel((x, y))[3])
    r_mean = sum(r_vals) / len(r_vals)
    g_mean = sum(g_vals) / len(g_vals)
    b_mean = sum(b_vals) / len(b_vals)
    x_mean = sum(x_vals) / len(x_vals)
    print((r_mean, g_mean, b_mean, x_mean))