# Internet Speed Test

## Description
This program is designed to test the network speed of a user's computer, specifically their download and upload speeds. The program utilizes the speedtest library to perform the tests and the tqdm library to display progress bars during the tests. Here's a step-by-step explanation of how the program works:

## How it works
1. The program starts by importing the necessary libraries: speedtest, tqdm, and time.
2. A custom class TqdmSpeedtest is defined, which inherits from the speedtest.Speedtest class. This custom class is created to override the _download and _upload methods of the speedtest.Speedtest class to integrate tqdm progress bars.
3. In the TqdmSpeedtest class, the _download and _upload methods are redefined to include callback hooks that are triggered during the progress of the download and upload tests. These hooks update the progress bars as the tests proceed.
4. The test_network_speed() function is defined to perform the actual network speed tests.
5. Inside the test_network_speed() function, a TqdmSpeedtest object is created and the best server to test the network speed is determined using the get_best_server() method.
6. The download speed test is performed using a tqdm progress bar. The download() method of the TqdmSpeedtest object is called with a callback function that updates the progress bar based on the progress percentage. The download speed is then calculated and stored in the download_speed variable (in Mbps).
7. Similarly, the upload speed test is performed using another tqdm progress bar. The upload() method is called with a callback function that updates the progress bar based on the progress percentage. The upload speed is then calculated and stored in the upload_speed variable (in Mbps).
8. After both tests are completed, the download and upload speeds are printed to the console.
9. The if __name__ == "__main__": block ensures that the test_network_speed() function is called only when the script is executed directly (not when it's imported as a module).

## Summary
Overall, this program provides a simple and visually informative way to test the network speed of a user's computer by displaying real-time progress bars for download and upload tests.
