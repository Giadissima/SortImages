
# SortImages
<p align="center">
  <img src="assets/logo.png" width="120" alt="SortImages Logo" />
</p>

<p align="center">A program to organize your photos and videos</p> 
<p align="center">Version 1.0.1</p>
<div align="center">
<a href="LICENSE.md" target="_blank"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://paypal.me/Giadissima1234?country.x=IT&locale.x=it_IT" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-ff3f59.svg"/></a>
<a href="https://t.me/Giadissima1234" target="_blank"><img src="assets/telegram.png" width=30/></a>
<a href="https://www.instagram.com/giadissima___/" target="_blank"><img src="assets/instagram.png" width=30/></a>
</div>

<br>
<div align="center">
<a align="center" href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/windows.zip" target="_blank"><img src="assets/windows_icon.png" height=50/></a>
<img src="assets/spaced.png" width=20/>
<a align="center" href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/linux.zip" target="_blank"><img src="assets/linux_icon.png" height=50/></a>
<img src="assets/spaced.png" width=20/>
<a align="center" href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/macos.zip" target="_blank"><img src="assets/mac_icon.png" height=50/></a>

</div>

## Overview

The SortImages tool is a powerful utility designed to efficiently organize images based on various parameters, including image names, metadata, and folder names. It extends its functionality to subdirectories, providing a comprehensive solution for image organization.

### Main interface

![Representative image of the project](assets/screenshot-v.1.0.1.png?raw=true "SortImages Screenshot")

### Result counters example

![Representative image of the end of a project](assets/result.png?raw=true "SortImages Screenshot")

###  Result of sort process example
![Representative image of sorting process](assets/example-dest-photos.png?raw=true "SortImages Screenshot")

## Features

- **Intelligent Sorting:** The tool intelligently organizes images by analyzing their names, metadata, and parent folder names.
- **Hierarchical Structure:** After specifying source and destination folders, images are structured into subfolders based on user-defined preferences, including the options to organize by `year`, `year/month`, or `year/month/day`.
- **Duplicate Recognition:** The tool recognizes duplicate images and offers user-selectable options to handle them:
  - Default: Leaves duplicates in the source folder and logs the detection.
  - Option to delete duplicates during the sorting process.
- **User Options:**
  - Option to choose the hierarchical structure based on year, year/month, or year/month/day.
  - Option to ignore folder names during sorting.
  - Option to delete empty folders after sorting.
  - Option to delete duplicates founded.
  - Option to move screenshots into a dedicated folder named "Screenshot" with organized subfolders.
  - Option to don't move Whatsapp's files into a dedicated folder named "Whatsapp" with organized subfolders.
  - Option to move files without date in a folder named "Unknown"

## How to Use

1. **Specify Source and Destination:**
   - Set the source folder containing unorganized images.
   - Specify the destination folder where organized images will be placed.

2. **Run the Tool:**
   - Execute the tool to initiate the sorting process.

3. **Customize Options:**
   - Choose options such as ignoring folder names, deleting duplicates, and removing empty folders.

4. **Review Log:**
   - Check the log for information on duplicate images and any skipped folders.

5. **Process Summary:**
   - After the sorting process is complete, a messagebox will display with the following counters:
     - Total media found: X
     - Total media without date found: Y
     - Total media without any date: Z
     - Total duplicate media found: W
     - Total media deleted: P
     - Total folders deleted: Q

   - These counters provide a quick summary of the results and help you understand the impact of the sorting process.

## Download

You can effortlessly download the project by clicking the following button:

<div>
<a href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/windows.zip" target="_blank"><img src="assets/windows_icon.png" height=50/></a>
<img src="assets/spaced.png" width=20/>
<a href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/linux.zip" target="_blank"><img src="assets/linux_icon.png" height=50/></a>
<img src="assets/spaced.png" width=20/>
<a href="https://github.com/Giadissima/SortImages/releases/download/1.0.1/macos.zip" target="_blank"><img src="assets/mac_icon.png" height=50/></a>
</div>

If you wish to view the source code follow these steps:

### Prerequisites

- Python 3.11

### Installation on Windows

1. Clone the repository:

   ```bash
   git clone https://github.com/Giadissima/SortImages

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the tool:

   ```bash
   py main.py

### Installation on Linux

1. Clone the repository:

   ```bash
   git clone https://github.com/Giadissima/SortImages

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   sudo apt-get install python-tk

3. Run the tool:

   ```bash
   python3 main.py

### Installation on MacOs

1. Clone the repository:

   ```bash
   git clone https://github.com/Giadissima/SortImages

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the tool:

   ```bash
   python3 main.py

## Contributing

Contributions are welcome! Add everything you want 😉.

See how to contribute in [CONTRIBUTE.md](CONTRIBUTE.md) file

## License

This project is licensed under the [MIT License](LICENSE.md).

See the [LICENSE.md](LICENSE.md) file for details.

<br>

<div align="center">
<a align="center", href="https://paypal.me/Giadissima1234?country.x=IT&locale.x=it_IT" target="_blank"><img src="assets/donations.png" width=210/></a>
</div>