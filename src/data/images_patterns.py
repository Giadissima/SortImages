IMAGE_FORMATS = { 
      # image patterns with 'img' prefix
      'img_1': '^img_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img_2023-12-09_12-09-23.gif
      'img_2': '^img-\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img-2023-12-09.gif
      'img_3': '^img\d{8}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img20231209.jpeg
      'img_4': '^img_\d{4}_\d{2}_\d{2}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img_2023_12_09.jpg
      'img_5': '^img-\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img-20231209_150738.jpg
      'img_6': '^img_\d{2}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img_12-09-23_150738.jpg
      'img_9': '^img\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img20231209_150738.jpg
      'img_10': '^img\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img2023-12-09.jpg
      'img_11': '^img-\d{2}-\d{2}-\d{2}-\d{6}\.(?:jpg|jpeg|png|gif|bmp|webm)', # img-12-09-23-150738.jpg
      'img_12': '^img_\d{2}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # img_12-09-23_150738.png
      
      # image patterns with 'image' prefix
      'image_1': '^image-\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # image-2023-12-09.jpg
      'image_2': '^image\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # image20231209.jpeg
      'image_3': '^image_\d{4}_\d{2}_\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # image_2023_12_09.jpg
      'image_4': '^image-\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # image-20231209_150738.jpg
      'image_8': '^image\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # image20231209_150738.jpg
      'image_9': '^image\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # image2023-12-09.jpg
      'image_10': '^image-\d{2}-\d{2}-\d{2}-\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # image-12-09-23-150738.jpg
      
      # image patterns with 'IMG' prefix
      'IMG_2': '^IMG\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # IMG20231209.jpg
      'IMG_3' : '^IMG-\d{8}-\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # IMG_20221222_215022_388.jpg
      'IMG_4' : '^IMG_\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # IMG_20231209_150738.jpg
      
      # image patterns with 'pic' prefix
      'pic_1': '^pic_\d{4}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # pic_20231209_150738.jpg
      'pic_2': '^pic-\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # pic-2023-12-09.jpg
      'pic_3': '^pic\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # pic20231209.jpeg
      'pic_4': '^pic_\d{4}_\d{2}_\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # pic_2023_12_09.jpg
      'pic_5': '^pic-\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # pic-20231209_150738.jpg
      'pic_6': '^pic_\d{2}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # pic_12-09-23_150738.jpg
      'pic_7': '^pic\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # pic12345678.jpg
      'pic_9': '^pic\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # pic20231209_150738.jpg
      'pic_10': '^pic\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # pic2023-12-09.jpg
      'pic_11': '^pic-\d{2}-\d{2}-\d{2}-\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # pic-12-09-23-150738.jpg
      
      # image patterns with 'photo' prefix: 
      'photo_1' : '^photo_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # photo_2023-12-09_15-07-38.png
      'photo_2': '^photo-\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # photo-2023-12-09.jpg
      'photo_3': '^photo\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # photo20231209.jpeg
      'photo_4': '^photo_\d{4}_\d{2}_\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # photo_2023_12_09.jpg
      'photo_5': '^photo-\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # photo-20231209_150738.jpg
      'photo_6': '^photo_\d{2}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # photo_12-09-23_150738.jpg
      'photo_7': '^photo\d{8}\.(?:jpg|jpeg|png|gif|bmp)', # photo20230912.jpg
      'photo_9': '^photo\d{8}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # photo20231209_150738.jpg
      'photo_10': '^photo\d{4}-\d{2}-\d{2}\.(?:jpg|jpeg|png|gif|bmp)', # photo2023-12-09.jpg
      'photo_11': '^photo-\d{2}-\d{2}-\d{2}-\d{6}\.(?:jpg|jpeg|png|gif|bmp)', # photo-12-09-23-150738.jpg
      
      # Screenshot patterns
      'screenshot_1': '^Screenshot_\d{8}\.(?:png|jpg|jpeg|gif|bmp)', # Screenshot_20231209.png
      'screenshot_2': '^ScreenCapture_\d{8}_\d{6}\.(?:png|jpg|jpeg|gif|bmp)', # ScreenCapture_20231209_150738.png
      'screenshot_3': '^Screen_\d{2}-\d{2}-\d{2}_\d{6}\.(?:png|jpg|jpeg|gif|bmp)', # Screen_12-09-23_150738.jpg
      'screenshot_4': '^scrnshot_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.(?:png|jpg|jpeg|gif|bmp)', # scrnshot_2023-12-09_15-07-38.png
      'screenshot_5': '^Desktop_\d{8}_screenshot\.(?:png|jpg|jpeg|gif|bmp)', # Desktop_20231209_screenshot.jpg
      'screenshot_7': '^ScreenShot\d{8}\.(?:png|jpg|jpeg|gif|bmp)', # ScreenShot20231209.jpg
      'screenshot_8': '^scrn-\d{4}-\d{2}-\d{2}_\d{6}\.(?:png|jpg|jpeg|gif|bmp)', # scrn-2023-12-09_150738.png
      'screenshot_9': '^Screenshot\d{2}_\d{2}-\d{2}-\d{2}_\d{6}\.(?:png|jpg|jpeg|gif|bmp)', # Screenshot01_12-09-23_150738.gif
      'screenshot_10': '^Capture_\d{8}_\d{6}\.(?:png|jpg|jpeg|gif|bmp)', # Capture_20231209_150738.bmp
      'screenshot_11': '^snapshot_\d{2}-\d{2}-\d{2}_\d{6}\.(?:jpg|jpeg|png|gif|bmp)' # snapshot_12-09-23_150738.png
    }