# SortImages

<p align="center">
  <a href="https://nestjs.com/" target="blank"><img src="assets/white_logo.jfif" width="120" alt="Nest Logo" /></a>
</p>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

  <p align="center">A progressive <a href="https://nodejs.org" target="_blank">Node.js</a> framework for building efficient and scalable server-side applications.</p>
    <p align="center">
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/v/@nestjs/core.svg" alt="NPM Version" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/dm/@nestjs/common.svg" alt="NPM Downloads" /></a>
<a href="https://circleci.com/gh/nestjs/nest" target="_blank"><img src="https://img.shields.io/circleci/build/github/nestjs/nest/master" alt="CircleCI" /></a>
<a href="https://discord.gg/G7Qnnhy" target="_blank"><img src="https://img.shields.io/badge/discord-online-brightgreen.svg" alt="Discord"/></a>
<a href="https://opencollective.com/nest#backer" target="_blank"><img src="https://opencollective.com/nest/backers/badge.svg" alt="Backers on Open Collective" /></a>
<a href="https://opencollective.com/nest#sponsor" target="_blank"><img src="https://opencollective.com/nest/sponsors/badge.svg" alt="Sponsors on Open Collective" /></a>
  <a href="https://paypal.me/kamilmysliwiec" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-ff3f59.svg"/></a>
    <a href="https://opencollective.com/nest#sponsor"  target="_blank"><img src="https://img.shields.io/badge/Support%20us-Open%20Collective-41B883.svg" alt="Support us"></a>
  <a href="https://twitter.com/nestframework" target="_blank"><img src="https://img.shields.io/twitter/follow/nestframework.svg?style=social&label=Follow"></a>
</p>

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
