import customtkinter
import os
from PIL import Image
from save_info import save_info,setup
FONT = "Roboto"


class HeaderFrame(customtkinter.CTkFrame): 
    def __init__(self,master, **kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0), weight=1)
        count = len([f for f in (os.listdir('storage')) if f.endswith('_front.png')])
        self.number = customtkinter.CTkLabel(self, text=f"Bottle #{count+1}", font=(FONT,42))
        self.number.grid(row= 0, column=0, sticky = "swn", padx = 18)
    
    def update_num(self):
        count = len([f for f in (os.listdir('storage')) if f.endswith('_front.png')])
        self.number.configure(text=f"Bottle #{count+1}")


class BodyFrame(customtkinter.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0), weight=1) 
        self.frontphoto = FrontPhoto(self)
        self.frontphoto.grid(row= 0, column=0, sticky = "nsew", padx = 5)
        self.rearphoto = RearPhoto(self)
        self.rearphoto.grid(row= 0, column=1, sticky = "nswe")
        self.bottleinfo = BottleInfo(self)
        self.bottleinfo.grid(row= 0, column=2, sticky = "nwse", padx = 5)
        self.update_images()

    def update_images(self):
        self.frontphoto.refresh()
        self.rearphoto.refresh()
        self.after(50, self.update_images)


class FrontPhoto(customtkinter.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)  
        self.last_updated = 0
        self.image = customtkinter.CTkImage(light_image=Image.open('no-image.png'), size=(420,750))
        self.image_label = customtkinter.CTkLabel(self, text="", image=self.image)
        self.image_label.grid(row= 0, column=0, sticky = "nwse", padx = 5, pady = 5)
        
    def refresh(self):
        if os.path.isfile('current_files/front.png'):
            if self.last_updated < os.path.getmtime('current_files/front.png'):
                self.image.configure(light_image=Image.open('current_files/front.png'))
                self.image_label.configure(image = self.image)
                self.last_updated = os.path.getmtime('current_files/front.png')
        else:
            self.image.configure(light_image=Image.open('no-image.png'))
            self.image_label.configure(image = self.image)


class RearPhoto(customtkinter.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.last_updated = 0
        self.image = customtkinter.CTkImage(light_image=Image.open('no-image.png'), size=(420,750))
        self.image_label = customtkinter.CTkLabel(self, text="", image=self.image)
        self.image_label.grid(row= 0, column=0, sticky = "nwse", padx = 5, pady = 5)  
        
    def refresh(self):
        if os.path.isfile('current_files/rear.png'):
            if self.last_updated < os.path.getmtime('current_files/rear.png'):
                self.image.configure(light_image=Image.open('current_files/rear.png'))
                self.image_label.configure(image = self.image)
                self.last_updated = os.path.getmtime('current_files/rear.png')
        else:
            self.image.configure(light_image=Image.open('no-image.png'))
            self.image_label.configure(image = self.image)

class BottleInfo(customtkinter.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)  
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((5), weight=1) 
        self.distillery_label = customtkinter.CTkLabel(self, text="Distillery:", font=(FONT,32))
        self.distillery_label.grid(row= 0, column=0, sticky = "nws", padx = 5, pady = 5) 
        self.distillery_textbox = customtkinter.CTkEntry(master=self, width=400, height = 50, corner_radius=10, font=(FONT,28))
        self.distillery_textbox.grid(row=1, column=0, sticky="", padx = 10, pady = 10)
        self.ref_label = customtkinter.CTkLabel(self, text="Reference:", font=(FONT,32))
        self.ref_label.grid(row= 2, column=0, sticky = "nws", padx = 5, pady = 5) 
        self.ref_textbox = customtkinter.CTkEntry(master=self, width=400, height = 50, corner_radius=10, font=(FONT,28))
        self.ref_textbox.grid(row=3, column=0, sticky="", padx = 10, pady = 10)
        self.checkbox = customtkinter.CTkCheckBox(master=self, text="Boxed?", font=(FONT,32), height = 50, width = 50)
        self.checkbox.grid(row=4, column=0, sticky="nsew", padx = 10, pady = 10)
        self.submit_button = customtkinter.CTkButton(master=self, text="Submit", font=(FONT,42), command=self.submit)
        self.submit_button.grid(row=6, column=0, sticky="nsew", padx = 10, pady = 10)

    def submit(self):
        data = [self.distillery_textbox.get(),self.ref_textbox.get(),self.checkbox.get()]
        if os.path.isfile('current_files/front.png') and os.path.isfile('current_files/rear.png'):
            save_info(data)
            self.master.master.headerFrame.update_num()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        setup()
        self.title("Whiskey Catalogue")
        self.geometry("1320x830")
        self._set_appearance_mode("light")

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=1)

        self.headerFrame = HeaderFrame(self, fg_color = "#cf9d33")
        self.headerFrame.grid(row = 0, column = 0, columnspan = 1, sticky= "new")
        self.bodyframe = BodyFrame(self, fg_color = "#ffffff")
        self.bodyframe.grid(row = 1, column = 0, rowspan = 1, sticky= "nesw")


app = App()
app.mainloop()

