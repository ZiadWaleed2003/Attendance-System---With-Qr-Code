import pandas as pd
import os
import cv2
from datetime import datetime


class MainSystem:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MainSystem, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # To prevent reinitialization
            self.df = pd.DataFrame(columns=['Name','Code', 'Time' ,'Number' , 'Course'], dtype=str)
            self.folder_path = None
            self.image_path = None
            self.vid = None
            self.frame = None
            self.initialized = True
            self.edit_file_path = None
           

    def set_Df2_For_Edit(self , file_path):
        
        self.df = pd.read_csv(file_path)


    def format_data(self,data):

        input_val = data.split(",")

        formated_data = {
            "Name"   : input_val[0],
            "Code"   : input_val[1],
            "Number" : input_val[2],
            "Course" : input_val[3]
        }

        return formated_data

    def Decode_Img(self, image):
        if image is None:
            print("No image provided for decoding")
            return None
        
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #decoding the image
        qr_decoder = cv2.QRCodeDetector()
        decoded_info = qr_decoder.detectAndDecodeMulti(gray_image)
     
        if isinstance(decoded_info[1][0], str):
            data = self.format_data(str(decoded_info[1][0]))
            return data
        
        return None

    def convert_Path_to_Image(self, file_path):
        img = cv2.imread(file_path)
        return img

    def add_Data_To_DataFrame(self, data):
        time = str(datetime.now().strftime("%H:%M"))
        new_row = pd.DataFrame([{"Name" : data['Name'] , "Code": data['Code'], 'Time': time ,  "Number" : data['Number'], "Course" : data['Course']}])
        
        try:
            self.df = pd.concat([self.df, new_row], ignore_index=True)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def edit_File(self, data):
        
        time = str(datetime.now().strftime("%H:%M"))

        new_row = pd.DataFrame([{'Code': data, 'Time': time}])

        try:
            self.df = pd.concat([self.df, new_row], ignore_index=True)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def save_Data_To_CSV(self, folder_name):
        current_date = datetime.now()

        file_path = os.path.join(folder_name, f"{current_date.date()}.csv")

        try:
            self.df.to_csv(file_path, index=False)
            return True , file_path
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            return False

# Usage
# main_system = MainSystem()
# another_main_system = MainSystem()
# print(main_system is another_main_system)  # This should print True, indicating both references point to the same instance.

