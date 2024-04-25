# Gaussian Blurring with Kivy

This project demonstrates the application of Gaussian blurring to images using a graphical user interface (GUI) built with Kivy. Gaussian blurring is a common image processing technique used to smooth images and reduce noise. It is based on the linear operation of convolution, where a kernel is applied to the image to produce the blurred effect.

## Technologies Used
- **Kivy**: For building the graphical user interface.
- **OpenCV**: For image processing and Gaussian blurring.

## Project Features
This project includes the following features:

### Image Loading and Capture
The GUI allows users to navigate folders to load an existing photo or capture a new one using a connected camera. This flexibility provides users with multiple options for selecting an image to process.

### Gaussian Blurring
Once an image is loaded, users can apply Gaussian blurring with different kernel sizes. The kernel size determines the level of blurring: larger kernels result in more blurring, while smaller kernels produce a subtler effect.

### Saving Processed Images
After applying Gaussian blurring, users can save the processed image to their desired location, allowing them to retain the edited images for further use.

## Linear Algebra in Gaussian Blurring
Gaussian blurring involves convolution, a linear operation where the kernel values are multiplied by the corresponding pixel values in the image and summed to produce the new pixel value in the output image. This process can be represented through matrix multiplication, a core operation in linear algebra.

## How to Use
1. Launch the application to open the GUI.
2. Navigate to a folder to load a photo or capture a new one using the camera.
3. Select a kernel size to apply Gaussian blurring. You can experiment with different kernel sizes to achieve the desired level of blurring.
4. Save the processed image to a specified location.

