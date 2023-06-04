
```
# Image Dataset Creation Tool

This is a Python application that allows you to create an image dataset by downloading images from different sources, such as Pexels and Bing. The application provides a user-friendly graphical interface for ease of use.

## Prerequisites

- Python 3.x
- Required Python packages (can be installed via pip):
  - use requirements.txt

## Installation

1. Clone the repository or download the source code files.

2. Install the required packages using pip:
   ```shell
   pip install gooey requests
   ```

3. Obtain the necessary API authentication code for Pexels:
   - Sign up for an account on the Pexels website (https://www.pexels.com/).
   - Generate an API key in your account settings.
   - Copy the generated authentication code.
   - Open the `settings.py` file and replace `pexels_auth_code` with your authentication code.

## Acknowledgements

This application includes code adapted from the [bing_image_downloader](https://github.com/gurugaurav/bing_image_downloader/) repository by Gurugaurav.

## Usage

### Executable 

1. Download the exe file from dist folder and run 

2. The graphical user interface (GUI) will be displayed, allowing you to configure the image dataset creation.

   - Select the image sources (Pexels and/or Bing) from the list.
   - Enter the categories of images you want to download, separated by commas.
   - Specify the number of images to download per class/category.
   - Choose the output location where the dataset will be saved.

3. Click the "Start" or "Create Dataset" button to initiate the image download process.

### Code

1. Open a terminal or command prompt.

2. Navigate to the directory where the source code files are located.

3. Run the application by executing the following command:

   ```shell
   python main_gooey.py
   ```
4. The graphical user interface (GUI) will be displayed, allowing you to configure the image dataset creation.

   - Select the image sources (Pexels and/or Bing) from the list.
   - Enter the categories of images you want to download, separated by commas.
   - Specify the number of images to download per class/category.
   - Choose the output location where the dataset will be saved.

5. Click the "Start" or "Create Dataset" button to initiate the image download process.

6. The application will download the images from the selected sources and save them in the specified output location. The images will be organized into folders based on their categories.

## TO DO 

### 1. Support for folloeing Image sources:
- Instagram
- google search
### 2. multiprocessing
### 3.metadata collection
### 4. Add modules to remove duplicate images


## Contributing

Contribuxtions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```





