# SortImage

![Representative image of the project](relative%20path/assets/screen.jpg?raw=true "Sort Image Screen")

## Overview

The SortImage tool is a powerful utility designed to efficiently organize images based on various parameters, including image names, metadata, and folder names. It extends its functionality to subdirectories, providing a comprehensive solution for image organization.

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
   git clone https://github.com/Giadissima/SortImages
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
