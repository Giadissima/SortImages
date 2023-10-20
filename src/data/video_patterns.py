VIDEO_FORMATS = {
  # video patterns with 'VID' prefix
  'VID_1': '^VID_(\d{8})_(\d{6})\.(?:mp4|avi|mov)',  # VID_20231209_150738.mp4
  'VID_2': '^VID_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_20231209_150738.mkv
  'VID_3': '^VID_(\d{4}-\d{2}-\d{2})_(\d{6})\.(?:mp4|avi|mov)',  # VID_2023-12-09_150738.mp4
  'VID_4': '^VID_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_20231209_150738.mkv
  'VID_5': '^VID_(\d{4}-\d{2}-\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_2023-12-09_150738.mkv
  'VID_6': '^VID_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_20231209_150738.mkv
  'VID_7': '^VID_(\d{4}-\d{2}-\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_2023-12-09_150738.mkv
  'VID_8': '^VID_(\d{4}-\d{2}-\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # VID_2023-12-09_150738.mkv
  
  # video patterns with 'DSCN' prefix
  'DSCN_1': '^DSCN(\d{8})_(\d{6})\.(?:mp4|avi|mov)',  # DSCN20231209_150738.avi
  'DSCN_2': '^DSCN(\d{4}\d{2}\d{2})_(\d{6})\.(?:mp4|avi|mov)',  # DSCN20231209_150738.mp4
  'DSCN_3': '^DSCN(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  'DSCN_4': '^DSCN(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  'DSCN_5': '^DSCN(\d{4}\d{2}\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  'DSCN_6': '^DSCN(\d{4}\d{2}\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  'DSCN_7': '^DSCN(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  'DSCN_8': '^DSCN(\d{4}\d{2}\d{2})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # DSCN20231209_150738.mkv
  
  # video patterns with 'A' prefix
  'A_1': '^A(\d{8})-(\d{6})\.(?:mp4|avi|mov)',  # A20231209-150738.mp4
  'A_2': '^A(\d{4}-\d{2}-\d{2}-\d{6})\.(?:mp4|avi|mov|mkv)',  # A20231209-150738.mkv
  'A_3': '^A(\d{4}-\d{2}-\d{2}-\d{6})\.(?:mp4|avi|mov)',  # A20231209-150738.mp4
  'A_4': '^A(\d{4}-\d{2}-\d{2}-\d{6})\.(?:mp4|avi|mov|mkv)',  # A20231209-150738.mkv
  'A_5': '^A(\d{8})-(\d{6})\.(?:mp4|avi|mov|mkv)',  # A20231209-150738.mkv
  'A_6': '^A(\d{8})-(\d{6})\.(?:mp4|avi|mov|mkv)',  # A20231209-150738.mkv
  'A_7': '^A(\d{8})-(\d{6})\.(?:mp4|avi|mov|mkv)',  # A20231209-150738.mkv
  
  # video patterns with 'webcam' prefix
  'webcam_1': '^webcam_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_2': '^webcam_(\d{4}-\d{2}-\d{2}-\d{6})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_3': '^webcam_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_4': '^webcam_(\d{4}\d{2}\d{2}-\d{6})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_5': '^webcam_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_6': '^webcam_(\d{4}\d{2}\d{2}-\d{6})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
  'webcam_7': '^webcam_(\d{8})_(\d{6})\.(?:mp4|avi|mov|mkv)',  # webcam_20231209_150738.mkv
}