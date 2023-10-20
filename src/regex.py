import re
from src.data.images_patterns import IMAGE_FORMATS
class RegexImage:
  def __init__(self):
    self.formats = IMAGE_FORMATS

  def check_regex(self, text:str):
    """Controlla i vari formati della stringa text

    Args:
        text (str): il testo da matchare (il filename)

    Returns:
        None | [int, int, int]: Returns None if any formats match, otherwise it returns the date extrapolated ([YYYY, MM, DD]).
    """
    if (re.search(self.formats['photo_1'], text) or 
            re.search(self.formats['image_4'], text) or
            re.search(self.formats['image_3'], text) or
            re.search(self.formats['image_1'], text) or
            re.search(self.formats['photo_2'], text) or
            re.search(self.formats['photo_5'], text) or
            re.search(self.formats['photo_4'], text)): 
        """ example photo matching:
            photo_2023-12-09_15-07-38.png, 
            photo-2023-12-09.jpg, 
            photo-20231209_150738.jpg, 
            photo_2023_12_09.jpg, 
            image-2023-12-09.jpg, 
            image_2023_12_09.jpg, 
            image-20231209_150738.jpg """
        return [text[6:10], text[11:13], text[14:16]]
    elif (re.search(self.formats['photo_3'], text) or
            re.search(self.formats['photo_7'], text) or
            re.search(self.formats['photo_9'], text)):
        """ example photo matching:
            photo20231209.jpeg, 
            photo20230912.jpg,  
            photo20231209_150738.jpg """
        return [text[4:8], text[8:10], text[10:12]]
    elif (re.search(self.formats['photo_6'], text) or
          re.search(self.formats['image_10'], text) or
          re.search(self.formats['photo_11'], text)):
        """ example photo matching: 
            photo_12-09-23_150738.jpg,
            photo-12-09-23_150738.jpg, 
            image-12-09-23-150738.jpg """
        return [(int)('20'+text[11:13]), text[8:10], text[5:7]]
    elif (re.search(self.formats['photo_10'], text) or
        re.search(self.formats['img_5'], text) or
        re.search(self.formats['img_4'], text) or
        re.search(self.formats['img_2'], text) or
        re.search(self.formats['img_1'], text) or
        re.search(self.formats['IMG_4'], text) or
        re.search(self.formats['IMG_3'], text) or
        re.search(self.formats['pic_5'], text) or
        re.search(self.formats['pic_4'], text) or
        re.search(self.formats['pic_2'], text) or
        re.search(self.formats['pic_1'], text)):
        """ example photo matching:
            img-2023-12-09.gif, 
            img_2023-12-09_12-09-23.gif, 
            img_2023_12_09.jpg,
            img-20231209_150738.jpg, 
            IMG_20231209_150738.jpg, 
            IMG_20221222_215022_388.jpg, 
            photo2023-12-09.jpg, 
            pic_20231209_150738.jpg, 
            pic-2023-12-09.jpg, 
            pic_2023_12_09.jpg, 
            pic-20231209_150738.jpg
        """
        return [text[4:8], text[9:11], text[12:14]]
    elif re.search(self.formats['screenshot_1'], text): # Screenshot_20231209.png
        return [text[11:15], text[15:17], text[17:19]]
    elif re.search(self.formats['screenshot_2'], text): # ScreenCapture_20231209_150738.png
        return [text[13:17], text[17:19], text[19:21]]
    elif re.search(self.formats['screenshot_3'], text): # Screen_12-09-23_150738.jpg
        return [(int)('20'+text[12:14]), text[9:11], text[6:8]]
    elif re.search(self.formats['screenshot_4'], text): # scrnshot_2023-12-09_15-07-38.png
        return [text[8:12], text[13:15], text[16:18]]
    elif (re.search(self.formats['screenshot_5'], text) or
          re.search(self.formats['screenshot_10'], text)):
        """ example photo matching:
            Capture_20231209_150738.bmp, 
            Desktop_20231209_screenshot.jpg """
        return [text[8:12], text[12:14], text[14:16]]
    elif re.search(self.formats['screenshot_7'], text): # ScreenShot20231209.jpg
        return [text[10:14], text[14:16], text[16:18]]
    elif re.search(self.formats['screenshot_8'], text): # scrn-2023-12-09_150738.png
        return [text[5:7], text[8:10], text[11:13]]
    elif re.search(self.formats['screenshot_9'], text): # Screenshot01_12-09-23_150738.gif
        return [(int)('20'+text[18:20]), text[12:14], text[9:11]]
    elif (re.search(self.formats['pic_3'], text) or
        re.search(self.formats['img_9'], text) or
        re.search(self.formats['img_3'], text) or
        re.search(self.formats['IMG_2'], text) or
        re.search(self.formats['pic_9'], text) or
        re.search(self.formats['pic_7'], text)):
        """ example photo matching:
            IMG20231209.jpg,
            pic20231209.jpeg,
            img20231209.jpeg,
            pic20231209_150738.jpg,
            img20231209_150738.jpg,
            pic12345678.jpg """
        return [text[3:7], text[7:9], text[9:11]]
    elif (re.search(self.formats['pic_6'], text) or
          re.search(self.formats['img_11'], text) or
          re.search(self.formats['img_12'], text) or
          re.search(self.formats['pic_11'], text)):
        """ example photo matching:
            pic_12-09-23_150738.jpg,
            pic-12-09-23-150738.jpg,
            img-12-09-23-150738.jpg """
        return [(int)('20'+text[9:11]), text[6:8], text[3:5]]
    elif (re.search(self.formats['pic_10'], text) or
          re.search(self.formats['img_10'], text)):
        """ example photo matching:
            pic2023-12-09.jpg,
            img2023-12-09.jpg """
        return [text[3:7], text[8:10], text[11:13]]
    elif (re.search(self.formats['image_2'], text) or
          re.search(self.formats['image_8'], text)):
        """ example photo matching
            image20231209.jpeg,
            image20231209_150738.jpg"""
        return [text[5:9], text[9:11], text[11:13]]
    elif re.search(self.formats['image_9'], text): # image2023-12-09.jpg
        return [text[5:9], text[10:12], text[13:15]]
    elif re.search(self.formats['img_6'], text): # img_12-09-23_150738.jpg
        return [text[4:6], text[7:9], text[10:12]]
    else:
      return None

    
class RegexVideo:
  pass