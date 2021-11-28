import tkinter
from tkinter import filedialog as fd
import JPGtoPDF


#delcaring func----------------

def get_last_filepath():
    global in_filepath
    global out_filepath
    File = open("filepath.txt","r")
    in_filepath =  File.readline()
    out_filepath = File.readline()
    File.close()


def window(main):
    #main application requires root
    main.title("JPG TO PDF")
    width = 500
    hight = 400
    x = ((main.winfo_screenwidth()/2)-(width/2))
    y =((main.winfo_screenheight()/2)-(hight/2))
    main.geometry(f"{width}x{hight}+{int(x)}+{int(y)}")


def main_widget():
    global file_type
    #buttons and labels ect, only label1 is not here since it has to be accessed by get_dir
    top_label = tkinter.Label(root,text="hello, this is JPG to PDF", font="25")
    in_button = tkinter.Button(root,text="Choose input files DIR",command= get_in_dir)
    out_button = tkinter.Button(root,text="Choose output DIR",command= get_out_dir)
    file_accept = tkinter.Button(root,text="submit file type",command=get_file_type)
    name_accept = tkinter.Button(root,text="submit file name",command=get_name)    
    final_convert = tkinter.Button(root,text="[CONVERT]",command=convert,font = "10")  

    top_label.pack()
    in_button.pack()
    label1.pack()
    out_button.pack()
    label2.pack()
    label3.pack()
    file_type_box.pack()
    file_accept.pack()
    label4.pack()
    file_name_box.pack()
    name_accept.pack()
    final_convert.pack()

def get_in_dir():
    #takes gobal variable filepath and will change it to where ever the user chooses
    global in_filepath
    in_filepath = fd.askdirectory() # askes user for dir
    label1.config(text=f"current dir: \n {in_filepath}")    #changes label to selected dir
    File = open("filepath.txt","r")     #opens 
    data = File.read()
    split = data.split("?")      #data is broken up by ??
    split[0] = in_filepath
    File.close()
    print(split)
    File = open("filepath.txt","w")
    for i in range(3):
        try:
            File.writelines(split[i]+"?")
        except:
            File.writelines(" "+"?")
    File.close()

def get_out_dir():
    #takes gobal variable filepath and will change it to where ever the user chooses
    global out_filepath
    out_filepath = fd.askdirectory() # askes user for dir
    label2.config(text=f"out dir: \n {out_filepath}")    #changes label to selected dir
    File = open("filepath.txt","r")     #opens 
    data = File.read()
    split = data.split("?")      #data is broken up by ??
    split[1] = out_filepath
    File.close()
    print(split)
    File = open("filepath.txt","w")
    for i in range(3):
        try:
            File.writelines(split[i]+"?")
        except:
            File.writelines(" "+"?")
    File.close()


def check_file_empty():     #checks if file for path
    global in_filepath
    global out_filepath
    global file_type
    try:
        File = open("filepath.txt","r") #if there is lines it will assign last values 
        count = 0
        All = File.read().split("?")
        for i in range(3):      #there should only be 3 lines in the file 
            if All[i] == "\n":
                continue
            else:
                if count == 0:
                    in_filepath = All[i]
                    count += 1
                elif count == 1:
                    out_filepath = All[i]
                    count += 1
                elif count ==2:
                    if All[i] == "":            #if no file type is found then default to jpg
                        file_type = ".jpg"
                        count += 1
                    else:
                        file_type = All[i]
                        count += 1
        File.close()

    except:             #if there is no file/path then it will make 3 lines
        File = open("filepath.txt","w")
        for i in range(3):
            File.writelines("\n")
        File.close()

def get_file_type():
    global file_type_box
    global file_type
    type_extention = "."+file_type_box.get()
    label3.config(text=f"current file name: \n {type_extention}")

    File = open("filepath.txt","r")     #opens 
    data = File.read()
    split = data.split("?")      #data is broken up by ??
    split[2] = type_extention
    File.close()
    print(split)
    File = open("filepath.txt","w")
    for i in range(3):
        try:
            File.writelines(split[i]+"?")
        except:
            File.writelines(" "+"?")
    File.close()

def get_name():
    global file_name
    file_name = file_name_box.get()
    label4.config(text=f"current file name: \n {file_name}")


def convert():
    global in_filepath
    global out_filepath
    global file_type
    global file_name
    JPGtoPDF.convert_to_pdf(file_name,file_type,in_filepath,out_filepath)



#init TK---------------------------------------

root = tkinter.Tk()          

in_filepath,out_filepath,file_type,file_name = str(),str(), ".jpg","untitled"            #file path is used to store the global input file path
check_file_empty()    
label1 = tkinter.Label(root,text=f"current input dir: \n {in_filepath}") #tells you what the current input DIR which is selected
#running program----------------------
file_type_box = tkinter.Entry(root,font=5)
file_name_box = tkinter.Entry(root,font=5)
label2 = tkinter.Label(root,text=f"current output dir: \n {out_filepath}")
label3 = tkinter.Label(root,text=f"file type: \n {file_type}")
label4 = tkinter.Label(root,text=f"current file name: \n {file_name}")
window(root)
main_widget()

root.mainloop()

#end of main--------------------


# to clean up and make sure choices is saved
File = open("filepath.txt","r")
data = File.readlines()
File.close()
print(data)
File = open("filepath.txt","w")
for i in range(3):
    try:
        File.write(data[i])
    except:
        File.write("\n")
File.close()
input()
