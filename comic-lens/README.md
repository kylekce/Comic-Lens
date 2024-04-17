# Comic Lens
Comic Lens is an open-source desktop application designed for both readers and translators alike, offering a seamless solution for manga, comics, and webcomic translation. This tool enable users to effortlessly translate characters or texts with precision and ease.

It is a Qt application written in Python, and uses [Pytesseract](https://github.com/madmaze/pytesseract) for optical character recognition (OCR) and [Googletrans](https://github.com/ssut/py-googletrans) for Google Translate API.

It currently supports the following languages:
* English
* French
* Indonesian
* Japanese
* Korean
* Spanish
* Chinese (Simplified)
* Chinese (Traditional)


Video Demo for CS50p Final Project: https://youtu.be/JC6sqe1ZZnw


## Installation
__Note:__ This application currently does not have a installer provided yet. So, please follow the steps below to run the application.

### Prerequisites
* Python 3.6 or above.
* PySide6 ([Installation guide](https://pypi.org/project/PySide6/))
* Googletrans ([Installation guide](https://github.com/ssut/py-googletrans))
* OpenCV ([Installation guide](https://pypi.org/project/opencv-python/))
* Pytesseract and its dependencies. ([Installation guide](https://github.com/madmaze/pytesseract))
* Make sure all the listed dependencies on the `requirements.txt` file are installed.

### Running the application
* Clone the repo
   ```sh
   git clone https://github.com/kylekce/Comic-Lens.git
    ```
* Run via terminal
   ```sh
   cd comic-lens
   python project.py
   ```

* Or run via Qt Creator
   * Open the project file `comic-lens.pyproject` in Qt Creator.
   * Click on the green play button on the bottom left corner of the IDE.

## Contribution
This project is currently in its early stages of development. If you would like to contribute, please fork the repo and create a pull request. You can also post issues on the issue tracker for any bugs or feature requests.

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
