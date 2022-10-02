import os # to connect the local enviromnet files

class FolderCreator:
    """Class utilised for creat a new folder for
    download zip files and another new folder for\
    extract the informaiton from zip files"""

    def __init__(self, location):
        """Initialize the folder location"""
        self.location = ''

    def folder_maker(self):
        """Create folder before starting any process
        pass the path of the folder as a self vaiable"""
        try:
            os.makedirs(self)# Creat a folder at the path
        except OSError as error:
            print(error)# Other wise generate error of folder already existed

class XmlConverter:
    """Load the individual XML files and further
    store the information into structure data frame"""

    def __init__(self,isr_data, fin_data):
        """Initialised the infoamtion of Issr and all
        variables of FinInstrmGnlAttrbts data"""
        self.isr_data = isr_data
        self.fin_data = fin_data

    def dic_to_lis(self, isr_data, fin_data):
        """Find the keys from data of Issr & FinInstrmGnlAttrbts
        and assign the values in new list and return the list"""

        parse_data= [] # new list

        for key, value in fin_data.items():
            #Check the id key from FinInstrmGnlAttrbts
            if key == "Id":
                parse_data.append(value)

            # Check key Fullnm from FinInstrmGnlAttrbts
            elif key == 'FullNm':
                parse_data.append(value)

            #Check key ClssfctnTp from FinInstrmGnlAttrbts
            elif key == 'ClssfctnTp':
                parse_data.append(value)

            #Check key CmdtyDerivInd from FinInstrmGnlAttrbts
            elif key == 'CmmdtyDerivInd':
                parse_data.append(value)

            #Check key Ntnlccy from FinInstrmGnlAttrbts
            elif key == 'NtnlCcy':
                parse_data.append(value)

        #Add key value of issr data
        else:
            parse_data.append(isr_data)

        # Return the final parse infoamtion new list
        return (parse_data)

    def xml_to_df(self):
        """Load the information keys and values of XML
        zip file clean data function return the process
        row information about the Issr data and
        FinInstrmGnlAttrbts data further utilize to convert into DF"""

        # List of each row information from diffrent xml files
        rows_data = []

        # Each consumer information list pass through for lopp
        for i in range(len(self)):

            # Utilise Try and exeptmenthod for diffrent type of recoed store in data
            try:
                isr_info = self[i]['TermntdRcrd']['Issr']
                fin_value = self[i]['TermntdRcrd']['FinInstrmGnlAttrbts']
                row = XmlConverter.dic_to_lis(self,isr_data=isr_info, fin_data=fin_value)
                rows_data.append(row)

            #If their iare key error check with another store record
            except KeyError:
                try:
                    isr_info = self[i]['ModfdRcrd']['Issr']
                    fin_value = self[i]['ModfdRcrd']['FinInstrmGnlAttrbts']
                    row = XmlConverter.dic_to_lis(self,isr_data=isr_info, fin_data=fin_value)
                    rows_data.append(row)

                except KeyError:
                    isr_info = self[i]['NewRcrd']['Issr']
                    fin_value = self[i]['NewRcrd']['FinInstrmGnlAttrbts']
                    row = XmlConverter.dic_to_lis(self,isr_data=isr_info, fin_data=fin_value)
                    rows_data.append(row)

        return (rows_data)
