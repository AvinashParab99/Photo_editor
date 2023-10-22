from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageOps, ImageEnhance


user_choise=int(input('1. for black and white\n'
                      '2. for sepia\n'
                      '3. for negative\n'
                      '4. for brightness\n'
                      '5. for contrast\n'
                      '6. for sharpness\n'))



#1-----gray scale----------------------------------------
def apply_grayscale(filepath3, output_file3):
    with Image.open(filepath3) as img:
        grayscale_img = img.convert("L")
        grayscale_img.save(output_file3)


def grayscale_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_grayscale(filepath3, output_file3)
        print(f"Grayscale filter applied and image saved to {output_file3}")

        window.destroy()

#2--------sepia--------------------------------------------------

def apply_sepia(filepath3, output_file3):
    with Image.open(filepath3) as img:
        sepia_img = img.convert("RGB")
        sepia_img = Image.blend(sepia_img, Image.new("RGB", sepia_img.size, (94, 38, 18)), alpha=0.5)
        sepia_img.save(output_file3)


def sepia_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_sepia(filepath3, output_file3)
        print(f"Sepia filter applied and image saved to {output_file3}")

        window.destroy()
##-------------negative---------------------------------------------------

def apply_negative(filepath3, output_file3):
    with Image.open(filepath3) as img:
        negative_img = ImageOps.invert(img)
        negative_img.save(output_file3)


def negative_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image files", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_negative(filepath3, output_file3)
        print(f"Negative filter applied and image saved to {output_file3}")

        window.destroy()

#4----------------------brightness--------------------------------------------------
def apply_brightness(filepath3, output_file3, factor):
    with Image.open(filepath3) as img:
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(factor)
        bright_img.save(output_file3)


def brighness_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image files", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_brightness(filepath3, output_file3,factor=1.5)
        print(f"Brightness filter applied and image saved to {output_file3}")

        window.destroy()

#5---------contrast---------------------------------------------------------
def apply_contrast(filepath3, output_file3, factor):
    with Image.open(filepath3) as img:
        enhancer = ImageEnhance.Contrast(img)
        contrast_img = enhancer.enhance(factor)
        contrast_img.save(output_file3)


def contrast_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image files", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_contrast(filepath3, output_file3,factor=1.8)
        print(f"Contrast filter applied and image saved to {output_file3}")

        window.destroy()

#6----------------------sharpness------------------------------------------------------
def apply_sharpness(filepath3, output_file3, factor):
    with Image.open(filepath3) as img:
        enhancer = ImageEnhance.Sharpness(img)
        sharp_img = enhancer.enhance(factor)
        sharp_img.save(output_file3)


def sharpness_transform():
    filepath3 = filedialog.askopenfilename(initialdir="C:\\",
                                              title="Open file ",
                                              filetypes=(("image files", "*.jpg"),
                                                         ("all files", "*.*")))

    if filepath3:

        output_file3 = "New_output.jpg"
        apply_sharpness(filepath3, output_file3,factor=1.5)
        print(f"Sharpness filter applied and image saved to {output_file3}")

        window.destroy()






if user_choise==1:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=grayscale_transform)
    file_button.pack()

    window.mainloop()


elif user_choise==2:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=sepia_transform)
    file_button.pack()

    window.mainloop()

elif user_choise == 3:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=negative_transform)
    file_button.pack()

    window.mainloop()


elif user_choise==4:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=brighness_transform)
    file_button.pack()

    window.mainloop()


elif user_choise==5:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=contrast_transform)
    file_button.pack()

    window.mainloop()

elif user_choise==6:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select  image From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=sharpness_transform)
    file_button.pack()

    window.mainloop()

else:
    print('invalid')


