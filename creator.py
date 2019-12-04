import os 
from os import path
import csv 

#current_path = os.getcwd()
#print("The current path is",current_path)

#import csv files
import_path = "/home/kpraponpoj/Documents/Auto_files_folders/"
import_file = import_path + "names.csv"

#file destination path
file_descriptor = ['Contract Award','Contract Drawing','Delivery Checklist',
                   'DOT,DOB PERMITS, DETOUR PLAN','Fabrication','Field Measurements',
                   'Letter of Transmittal','Miscellaneous', 'MWI Shop Drawings',
                   'PE Calculations','Purchase Order, Quote (RFI)', 'Reviewed Submittal',
                   'Schedule of Values']

#create a new folder 
DestFolderLoc = "/home/kpraponpoj/Documents/Auto_files_folders/output/"

def main():
    #read csv file 
    with open(import_file, newline= '') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter = ',')
        for row in reader: 

            #print(row['job#'],row['job_name'],row['PM'],row ['address'])
            #create new main folder

            #check if PM sub folder exists, if not create one
            PM_sub_folder = DestFolderLoc + row['PM'] + "/"
            if not (os.path.isdir(PM_sub_folder)):
                os.mkdir(PM_sub_folder)
            
            #crete project path
            Proj_Name = "Job No. {} ({}, {})".format(row['job#'],row['job_name'],row ['address'])
            project_path = PM_sub_folder + Proj_Name + "/"
            os.mkdir(project_path)
            
            #create sub_project_path
            for i in range(len(file_descriptor)):
                sub_proj_name = "{} (Job No. {}) - {}".format(row['job_name'],row['job#'],file_descriptor[i])
                sub_proj_path = project_path + sub_proj_name
                os.mkdir(sub_proj_path)

    csvfile.close()
    print("Folders created successfully!")

if __name__ == "__main__":
    main()
    




