from PIL import Image, ImageDraw, ImageFont

def create_dl_logo(python):
    #create a blank image with a white background
    width, height = 400,200
    image = Image.new("RGB",(width,height),"brown")
    draw = ImageDraw.Draw(image)

    #draw a rectangle as the backgrorund
    draw.rectangle([0,0,width,height],fill="blue")

    #add text to the image 
    font_size=40
    font=ImageFont.load_default()
    text="DESHKIB"

    #Use ImageDraw to get the size of the  text
    text_width,text_height=draw.textsize(text, font=font)
    text_position =((width-text_width)//2,(height-text-height)//2)
    draw.text(text_position,text,font=font,fill="yellow")

    #save the image to the specified path
    image.save(python)
    print(f"logo saved to{python}")

    if _name_=="__main__":
        output_path="dl_logo.png"
        create_dl_logo(python)