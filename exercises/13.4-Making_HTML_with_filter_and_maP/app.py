all_colors = [
    {"label": 'Red', "sexy": True},
    {"label": 'Pink', "sexy": False},
    {"label": 'Orange', "sexy": True},
    {"label": 'Brown', "sexy": False},
    {"label": 'Pink', "sexy": True},
    {"label": 'Violet', "sexy": True},
    {"label": 'Purple', "sexy": False},
]

def filter_colors(color):
    return color["sexy"]


def generate_li(color):
    return f"<li>{color['label']}</li>"


filtered_colors = filter(filter_colors, all_colors)
html_list = list(map(generate_li, filtered_colors))


print(html_list)



