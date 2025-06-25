import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

r=tk.Tk()
r.withdraw()
file_path=filedialog.askopenfilename(title="Select the image",filetypes=[("Image File",("*jpg","*png","*jpeg"))])
im=cv2.imread(file_path,1)

drawing=False
ix , iy = -1,-1
fx, fy = -1 , -1
im_copy=im.copy()
final_img = []

def draw_rectange(event,x,y,flags,param):
    global ix,iy,fx,fy,drawing,im,im_copy, final_img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
        fx,fy=x,y
    
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        
        fx,fy=x,y
        im=im_copy.copy()
        cv2.rectangle(im,(ix,iy),(fx,fy),(0,0,255),thickness=4)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx,fy=x,y
        x1 , y1 = min(ix,fx),min(iy,fy)
        x2 , y2 = max(ix,fx),max(iy,fy)

        blur = im_copy[y1:y2,x1:x2]
        im_copy[y1:y2,x1:x2] = cv2.blur(blur,(25,25))
        im=im_copy.copy()
        final_img = im

cv2.namedWindow("Image")
cv2.setMouseCallback("Image",draw_rectange)

messagebox.showinfo("BLURRING TOOL INFO"," IF YOU WANT TO SAVE PRESS - S . \n\n IF YOU WANT TO REALOAD IMAGE PRESS ANY KEY (EXCEPT ESC). \n\n"
    "FOR CLOSING WITHOUT SAVING PRESS - ESC \n\n THANK YOU :) !!")
while True:
    cv2.imshow("Image",im)
    key = cv2.waitKey(1)
    
    if key==27:
        messagebox.showerror("TERMINATED !!","THE PROGRAM TERMINATED !! :(")

        break
    elif key == ord("s") or key == ord("S"):
        if final_img is None:
            messagebox.showwarning("Warning !!","You haven't blurred anything !!")
        else:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg",title="Select the path for saving te Image",filetypes=[("Image Files",("*.jpg","*.jpeg","*.png"))])
            cv2.imwrite(save_path,final_img)
            messagebox.showinfo("File Saved !!","Blurred Image is Saved Successfully !!  :)")
            break

cv2.destroyAllWindows()
