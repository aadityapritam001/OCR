# OCR
Documents_OCR

#preprocess.py 
This python file process and clean the image by doing some editing to make more sharp & clear and also it converts the image into black & white image , so that our ocr will recognise text in a more clear way.

#extract_text 
This is the main python file , to Run/Execute this file use the following command:
                step:1) Enter the command : "python extract_text.py"
                step:2) After execution it will ask for the image path : e.g- Enter the Image path:   sbi-1.jpg
                step:3) It will print the result on console as well it will save a txt file "Extracted_data.txt" in same directory 
                
                In this way Using these simple steps , we can extract the information from image(.jpg, .jpeg, .png , etc.)
                
                A file will also created with the name "Bounding_box.jpg" in which we can see how it recognises text on that image.
                
  
  # ---------Model---------
Model Used/Library Used : Pytesseract 
there are various OCRs like EAST, easyocr, Google ocr api, but the main reason behind using this library is it works well on documents or pages , and other OCR like EAST is specially designed for real world recognition or movable objects. 
  
Other Library use: there are also more python library used in this project , all mentioned in "requirements.txt" . So it is important to have these library installed before using or create virtual environment and install all these library before execution.  
