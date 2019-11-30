import os 
from os import path
import csv 

current_path = os.getcwd()
#print("The current path is",current_path)

#import csv files (JOB number, Name)
import_path = "/home/kpraponpoj/Documents/Auto_files_folders/"
import_file = import_path + "names.csv"

#file destination path
file_descriptor = ['Contract Award','Contract Drawing','Delivery Checklist',
                   'DOT,DOB PERMITS, DETOUR PLAN','Fabrication','Field Measurements',
                   'Letter of Transmittal','Miscellaneous', 'MWI Shop Drawings',
                   'PE Calculations','Purchase Order, Quote (RFI)', 'Reviewed Submittal',
                   'Schedule of Values']

def main():
    with open(import_file, newline= '') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter = ',')
        for row in reader: 
            #print(row['job#'],row['job_name'])
            #create new main folder
            folderName = "Job No. {} ({})".format(row['job#'],row['job_name'])
            destination_path = "/home/kpraponpoj/Documents/Auto_files_folders/output/" + folderName + "/"
            os.mkdir(destination_path)
            for i in range(len(file_descriptor)):
                newdir = "{} (Job No. {}) - {}".format(row['job_name'],row['job#'],file_descriptor[i])
                full_dest_path = destination_path + newdir
                os.mkdir(full_dest_path)
    csvfile.close()
    print("Folders created successfully!")

if __name__ == "__main__":
    main()
    




