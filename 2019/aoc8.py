import sys

with open("aoc8.txt") as f:
    image = f.read()


def split_x_at(input_string, split):
    return [input_string[i : i + split] for i in range(0, len(input_string), split)]


width = 25
height = 6

pixel_count = len(image)
layer_lenght = width * height
layer_count = int(pixel_count / (width * height))
layers = split_x_at(image, layer_lenght)
test = len(layers[0])

fewest_zeros = sys.maxsize
for element in layers:
    zeros = element.count("0")
    ones = element.count("1")
    twos = element.count("2")
    if fewest_zeros > zeros:
        fewest_zeros = zeros
        output = ones * twos

print(output)

picture = ""


lines = []
for element in layers:
    line = split_x_at(element, width)
    lines.append(line)


def get_deeper_pixel(position, layer_number, latest_pixel=""):
    line = layers[layer_number]
    latest_pixel = line[position]
    if latest_pixel != "2":
        return latest_pixel
    else:
        if layer_number < layer_count - 1:
            return get_deeper_pixel(position, layer_number + 1, latest_pixel)
        else:
            return ''

for x in range(layer_lenght):
    picture += get_deeper_pixel(x, 0)

picture = split_x_at(picture, width)

test = len(picture[0])

for i, line in enumerate(picture):
    length = len(line)
    if i == 98:
        print('here')
    newline = ''
    for x in line:
        if x == '1':
            newline += ' '
        else:
            newline += 'X'
    print(newline)