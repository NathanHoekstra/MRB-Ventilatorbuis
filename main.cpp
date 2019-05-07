#include <iostream>

#include <opencv2/opencv.hpp>

int main(){
    cv::Mat image;
    image = imread( "img/lena.png", cv::IMREAD_COLOR ); // Read the file
    if( image.empty() )                      // Check for invalid input
    {
        std::cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }
    namedWindow( "Display window", cv::WINDOW_AUTOSIZE ); // Create a window for display.
    imshow( "Display window", image );                // Show our image inside it.
    cv::waitKey(0); // Wait for a keystroke in the window
    return 0;
}