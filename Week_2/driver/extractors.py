import numpy as np
import cv2
from skimage import feature as ft

# Extractors
# -----------------------
# Color feature extraction
def color_features(image, mask=None):
    bins = 8
    # Convert image to HSV color space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Calculate color histogram and normalize
    histogram = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
#     print(histogram)
    return histogram.flatten()

# Find contrast
def contrast_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = image.std()
    return contrast

def cloudy_contrast_features(image):
    bins = 8
    alpha = 1.5 # Simple contrast control
    beta =0   # Simple brightness control
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    histogram = cv2.calcHist([image], [0,1,2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram,histogram)
    contrast = histogram.flatten()
    return contrast 

def brightness_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    brightness = image[:, :, 2].flatten()
    brightness = cv2.normalize(brightness, brightness, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    brightness = brightness.flatten()
    brightness = (x for x in brightness if x > 0.8)
    return sum(list(brightness))

def colorfulness_features(image):
    (B, G, R) = cv2.split(image.astype("float"))
    
    rg = np.absolute(R-G)
    yb = np.absolute(0.5*(R+G) - B)
    
    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))
    
    stdRoot = np.sqrt((rbStd**2) + (ybStd**2))
    meanRoot = np.sqrt((rbMean**2) + (ybMean**2))
    
    return stdRoot + (0.3*meanRoot)

# Horizontal variance feature extraction
def horiz_var_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width, height = (500, 500)
    if not width or not height:
      return 0
    variances = []
    for y in range(height):
        row = [image[x, y] for x in range(width)]
        mean = sum(row)/width
        variance = sum([(x - mean)**2 for x in row])/width
        variances.append(variance)
    return variances

# Edge features using high-pass filter on FFT
def foggy_fourier_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (300, 300))
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
    
    rows, cols = (cv2.getOptimalDFTSize(300), cv2.getOptimalDFTSize(300))
    crow, ccol = (rows/2, cols/2)
    
    # circular hpf mask
    mask = np.ones((rows, cols, 2), np.uint8)
    r = 80
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1])**2 <= r*r
    mask[mask_area] = 0
    
    fshift = dft_shift*mask

    fshift_mask_mag = 2000*np.log(cv2.magnitude(fshift[:,:,0], fshift[:,:,1]))
    np.seterr(divide='ignore', invalid='ignore')
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    
    return img_back.flatten()

def snowy_fourier_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (250, 250))
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
    
    rows, cols = (cv2.getOptimalDFTSize(250), cv2.getOptimalDFTSize(250))
    crow, ccol = (rows/2, cols/2)
    
    # circular hpf mask
    mask = np.ones((rows, cols, 2), np.uint8)
    r = 80
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1])**2 <= r*r
    mask[mask_area] = 0
    
    fshift = dft_shift*mask
    np.seterr(divide='ignore', invalid='ignore')
    fshift_mask_mag = 2000*np.log(cv2.magnitude(fshift[:,:,0], fshift[:,:,1]))
    
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    
    return img_back.flatten()

# Histogram of Oriented Gradients
def hog_features(image):
  img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  cell_size = (40, 40)
  bins = 9
  cpb = (12, 12)
  norm = "L2"
  fd, hog_image = ft.hog(img, orientations=bins, pixels_per_cell=cell_size, 
                      cells_per_block=cpb, visualize=True, block_norm=norm, transform_sqrt=True)
  return fd


