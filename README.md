
# SortImages
<p align="center">
  <a href="https://nestjs.com/" target="blank"><img src="assets/logo.png" width="120" alt="Nest Logo" /></a>
</p>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

<p align="center">A program to organize your photos and videos</p> 
<div align="center">
<a href="LICENSE.md" target="_blank"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://paypal.me/Giadissima1234?country.x=IT&locale.x=it_IT" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-ff3f59.svg"/></a>
<a href="https://t.me/Giadissima1234" target="_blank"><img src="assets/telegram.png" width=30/></a>
<a href="https://www.instagram.com/giadissima___/" target="_blank"><img src="assets/instagram.png" width=30/></a>
</div>

<br>
<a align="center", href="https://github.com/Giadissima/SortImages/releases/download/alpha/SortImages_alpha.rar" target="_blank"><img src="assets/windows_download.png" height=50/></a>

<br>

![Representative image of the project](assets/screen.png?raw=true "SortImages Screenshot")

## Overview

The SortImages tool is a powerful utility designed to efficiently organize images based on various parameters, including image names, metadata, and folder names. It extends its functionality to subdirectories, providing a comprehensive solution for image organization.

## Features

- **Intelligent Sorting:** The tool intelligently organizes images by analyzing their names, metadata, and parent folder names.
- **Hierarchical Structure:** After specifying source and destination folders, images are structured into subfolders based on the following format: `year/month/day`.
- **Duplicate Recognition:** The tool recognizes duplicate images and offers user-selectable options to handle them:
  - Default: Leaves duplicates in the source folder and logs the detection.
  - Option to delete duplicates during the sorting process.
- **User Options:**
  - Option to ignore folder names during sorting.
  - Option to delete empty folders after sorting.

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

## Getting Started

### Prerequisites

- Python 3.11

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Giadissima/SortImagess
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:

   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

See the [LICENSE.md](LICENSE.md) file for details.
