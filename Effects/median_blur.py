import cv2
import numpy 

def get_kernel_median(img,row_initial,col_initial,kernel_size):
    values = []
    for row in range(row_initial,row_initial+kernel_size):
        for col in range(col_initial,col_initial+kernel_size):
            values.append(img[row,col])
    values.sort()
    median = values[len(values)//2]
    return median 

def set_kernel_values(img,row_initial,col_initial,kernel_size,value):
   img[row_initial+kernel_size//2,col_initial+kernel_size//2] = value 

def median_blur(img, kernel_size):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    final_img = gray_img
    for row in range(0,len(gray_img)-kernel_size):
        for col in range(0,len(gray_img[0])-kernel_size):
            median = get_kernel_median(gray_img,row,col,kernel_size)
            set_kernel_values(final_img,row,col,kernel_size,median)
    
    blurred_img = cv2.cvtColor(final_img,cv2.COLOR_GRAY2BGR)
    return blurred_img

if __name__ == "__main__":
        img = cv2.imread("Ggstokes.jpg")
        blurred = median_blur(img,5)
        cv2.imshow("org",img)
        cv2.imshow("blur",blurred)
        cv2.waitKey(0)
