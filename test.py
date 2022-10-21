from PIL import Image, ImageDraw, ImageFont
import textwrap
import csv



def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    print(str(image_width)+"X"+str(image_height))
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height


def main():

    with open('heart quotes list.txt') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        countxt = 0
        for row in csvReader:
            try:
                print(row[0])
                countxt = countxt + 1
                textgg=str(row[0])
            except:
                print(str(countxt+1))
                countxt = countxt + 1
                textgg=str(" Hi, Please Follow/Subscribe")
            '''
            Testing draw_multiple_line_text
            '''
            #image_width
            image = Image.open('ailive.png')
            # Image.new('RGB', (800, 600), color = (0, 0, 0))
            fontsize = 40  # starting font size
            font = ImageFont.truetype("arial.ttf", fontsize)
            text1 = str(textgg)
            text_color = (200, 200, 200)
            text_start_height = 200
            draw_multiple_line_text(image, text1, font, text_color, text_start_height)
            image.save(str(countxt)+'.png')

if __name__ == "__main__":
    main()
    #cProfile.run('main()') # if you want to do some profiling
