# Image Dataset Creation Tool
![image](https://github.com/akhil451/create_image_dataset/blob/main/images/image.png?raw=true)

```
This is a Python application that allows you to create an image dataset by downloading images from different sources, such as Pexels and Bing. The application provides a user-friendly graphical interface for ease of use.


## Prerequisites

- Python 3.x
- Required Python packages (can be installed via pip):
  - use requirements.txt


s```

## Acknowledgements

This application includes code adapted from the [bing_image_downloader](https://github.com/gurugaurav/bing_image_downloader/) repository by Gurugaurav.

## Usage

### Executable 

1. Download the exe file from dist folder and run 

2. The graphical user interface (GUI) will be displayed, allowing you to configure the image dataset creation.

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

   - Enter the categories of images you want to download, separated by commas.
   - Specify the number of images to download per class/category.
   - Choose the output location where the dataset will be saved.

5. Click the "Start" or "Create Dataset" button to initiate the image download process.

6. The application will download the images from the selected sources and save them in the specified output location. The images will be organized into folders based on their categories.


## BUILD EXE
```
pyinstaller build.spec
```

## TO DO 

### 1. Support for folloeing Image sources:
- Instagram
- google search
### 3.metadata collection
### 4. Add modules to remove duplicate images


## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## Note : 
Support for Pixabay and pexels has been removed for now as they are limited by their APIs. They can be activated by uncommenting following lines:

main_goeey.py - 14,15,23-30,42,47-54,62,63

In settings.py, you would need to add values for pexels_auth_code and pixabay_auth_code


## License

This project is licensed under the [MIT License](LICENSE).
```





