import cv2
from tkinter import Tk, filedialog

def upload_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    # Upload gambar
    image_path = upload_image()
    
    # Membaca gambar dengan OpenCV
    image = cv2.imread(image_path)

    # Menampilkan gambar
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
