from PIL import Image

def img_to_gif(number_of_days):
    frames = []
    for frame_number in range(number_of_days - 1, -1, -1):
        frame = Image.open(f'figure{frame_number}.png')
        frames.append(frame)
 
    frames[0].save(
        'NS_animation.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=500,
        loop=0
    )