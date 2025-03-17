from PIL import Image, ImageDraw, ImageFont

class ImageReader:
    def __init__(self):
        """
        Instantiate an ImageReader object. Constructor does not require any parameters.
        :param: None - Does not require any parameters.
        :return: ImageReader Object with Nulled Parameters color_mode,
        image_format, image_height, image_width, image_attributes_dict, and image_path.
        """
        self.color_mode = None
        self.image_format = None
        self.image_height = None
        self.image_width = None
        self.image_attributes_dict = None
        self.image_path = None
        self.im = None

    def read_image(self, image_path:str):
        """
        Reads an image from a specified path. The Read Image is displayed in a separate window.
        :param image_path:str: Path to the image
        :return: None. Object is self-contained.
        """
        self.im = Image.open(image_path)
        self.image_path = image_path
        print(f"Successfully Read Image from Path: {self.image_path}.  Image Attributes:\n\tImage Format: {self.im.format}\n\t"
              f"Image Size: {self.im.size}\n\t"
              f"Color Mode: {self.im.mode}\n")
        self.image_attributes_dict = {'format': self.im.format, 'size':self.im.size, 'mode':self.im.mode}
        self.image_width = self.im.size[0]
        self.image_height = self.im.size[1]
        self.image_format = self.im.format
        self.color_mode = self.im.mode
        self.im.show()


    def convert_to_greyscale(self):
        """
        Converts the image to greyscale.
        :param self: function is applied to the object
        :return: None. Object is self-contained.
        """
        self.im = self.im.convert('L')
        print(f"Successfully Converted Image to Greyscale.")
        self.im.show()
        self.im.save("./images/out.jpg")

    def draw_text(self, text:str):
        """
        Draws the text parameter unto the image
        :param text:str: the text to be drawn on the image
        :return: None. Object is self-contained.
        """
        draw = ImageDraw.Draw(self.im)
        font = ImageFont.truetype(font=r'./fonts/sans-serif.ttf', size=50)
        draw.text(xy=(int(self.image_width/4), int(self.image_height/4)),
                  text=text, font=font, fill="purple")
        self.im.show()
        self.im.save('./images/out.jpg')






