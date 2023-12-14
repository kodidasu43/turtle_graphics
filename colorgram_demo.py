import colorgram

rgb_colors = []
colors = colorgram.extract(r"image.jpg", 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.g
    new_color_tuple=(r,g,b)

    rgb_colors.append(new_color_tuple)

print(rgb_colors)