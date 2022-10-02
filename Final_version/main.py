import xmltodict as xtd # To read xml files
import os # To handel files in local enviroments
from zipfile import ZipFile # For unzip the downloaded files
import wget # Used for download zip files from main XML
from xml_to_csv import FolderCreator, XmlConverter #Load the class file of xml readers
import pandas as pd # TO convert the data into dataframe and store information into csv
import s3fs # Store csv file information into AWS s3 bucket

# Load main XML file and Read the file from the location
main_xml_file = open('task_file.xml','r').read()

# Parse the information from main XML file
main_xml_file = xtd.parse(main_xml_file)

# Locate the information from XML files
xml_info_sets = main_xml_file['response']['result']['doc']

# new folder path for the zip files
zip_path = 'C:/Users/Dhrupad/Desktop/steel_i/final_project/zip_files'
FolderCreator.folder_maker(zip_path)

# Create a new folder for the xml files
xml_paths = 'C:/Users/Dhrupad/Desktop/steel_i/final_project/xml_files'
FolderCreator.folder_maker(xml_paths)

# Download the zip files and store it into the Created folder
for links in range(len(xml_info_sets)):
    # Url of the zip file
    url = xml_info_sets[links]['str'][1]['#text']
    # download the zip file and store into new folder
    get_files = wget.download(url, zip_path)

# Unzip the file and store the xml into new folder
for files in os.listdir(zip_path):
    # Load the zip file
    with ZipFile((os.path.join('zip_files/',files)),'r') as zip:
        zip.printdir()
        # Extract the xml file into new folder
        zip.extractall(path='xml_files/')


df_lists = [] # List of data frames
# Read individual xml files and store data into dataframes
for xml in os.listdir('xml_files/'):

    # utf8 encoding parsing
    file = open(os.path.join('xml_files/',xml), 'r',encoding='utf8').read()

    # Parse xml files one by one
    root = xtd.parse(file)

    # Filter out the main data
    filter_info = root['BizData']['Pyld']['Document']['FinInstrmRptgRefDataDltaRpt']['FinInstrm']

    # Load the function which convert the filter info into df
    data = XmlConverter.xml_to_df(filter_info)

    # Title of each column
    col = [
        'FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm',
        'FinInstrmGnlAttrbts.ClssfctnTp',
        'FinInstrmGnlAttrbts.CmmdtyDerivInd',
        'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'
    ]
    # Create a data frame
    df = pd.DataFrame(data, columns=col)

    # Store the data frame into new list
    df_lists.append(df)

# Concatination the dataframe
final_df = pd.concat(df_lists,ignore_index=True)

# Store csv file in local Enviroment
final_df.to_csv('task_data.csv',index= False)

# Store the csv file into the s3 bucket
final_df.to_csv(
    's3://python-engineering-assesment-task/task_auto_file.csv',
    storage_options={'key':'################',
                     'secret':'##############################'})
