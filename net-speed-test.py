import speedtest
from tqdm import tqdm
import time

class TqdmSpeedtest(speedtest.Speedtest):
    def _download(self, url, timeout, callback):
        def hook(current, total):
            callback(current / total * 100)

        return self._request(url, timeout=timeout, progress=True, progress_callback=hook)

    def _upload(self, url, data, timeout, callback):
        def hook(current, total):
            callback(current / total * 100)

        return self._request(url, timeout=timeout, progress=True, progress_callback=hook, data=data)

def test_network_speed():
    # Initialize the TqdmSpeedtest object
    st = TqdmSpeedtest()

    # Get the best server to test the network speed
    st.get_best_server()

    # Test download speed
    with tqdm(total=100, unit='%', desc='Download Test') as pbar:
        download_speed = st.download(callback=lambda percent, *args, **kwargs: (pbar.update(percent - pbar.n), time.sleep(0.01))) / 1_000_000

    # Test upload speed
    with tqdm(total=100, unit='%', desc='Upload Test') as pbar:
        upload_speed = st.upload(callback=lambda percent, *args, **kwargs: (pbar.update(percent - pbar.n), time.sleep(0.01))) / 1_000_000

    # Print results
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    test_network_speed()
