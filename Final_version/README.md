-> This version of the project has object-oriented programming. The Main file contains the loading and parsing of main XML files.

-> The other file with the name ‘xml_to_csv.py’ was developed with two classes. The first class is named a ‘FolderMaker,’ which is 
utilized for creating new folders while downloading zip files for storing and unzipping the information of the XML files.

-> For parsing the XML files, the “xmltodict” python module was utilized, which converts the XML information and stores it 
into dictionary-type data.

-> From this dictionary data type, identify and locate the DLTINS zip files, download files using the wget package, store 
them in the new folder, and unzip all files into a new folder.

-> Next part into the main.py, the extracted zip file XML is loaded into the program and parsed the XML file into dictionary type.

-> At the back end of the program ‘xml_to_csv.py file, the class name ‘XmlConverter’ contains two functions. The first function 
locates and identifies the dictionary keys and values for the attributes needed to store in a data frame as per the requirement 
of column attributes using pandas.

-> All information from 4 XML files is further stored into CSV files and initially stored locally and stored into the s3 
bucket by keys and secret keys of the AWS.
