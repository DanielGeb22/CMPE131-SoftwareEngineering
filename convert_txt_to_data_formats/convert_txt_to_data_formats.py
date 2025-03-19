import pandas as pd
import dicttoxml
import os

def convert(file, format):
    # Defines current directory to save the converted files
    input_dir = os.path.dirname(os.path.abspath(file))
    # Reads the TXT file
    file_read = pd.read_csv(file, delimiter="\t", encoding="ISO-8859-1", na_values=["#N/A"])

    # Convert TXT to CSV
    if (format == 'c'):
        file_read.to_csv(os.path.join(input_dir, "data.csv"), index=False)
    # Convert TXT to JSON
    elif (format == 'j'):
        file_read.to_json(os.path.join(input_dir, "data.json"), orient="records", indent=4)
    # Convert TXT to XML
    elif (format == 'x'):
        data_dict = file_read.to_dict(orient="records")
        xml_data = dicttoxml.dicttoxml(data_dict, custom_root="Players", attr_type=False)

        xml_path = os.path.join(input_dir, "data.xml")
        with open(xml_path, "wb") as f:
            f.write(xml_data)
    # If none of the above, print error
    else:
        print("Invalid format, please try again")

convert("NFL Offensive Player stats, 1999-2013.txt", 'c')
convert("NFL Offensive Player stats, 1999-2013.txt", 'j')
convert("NFL Offensive Player stats, 1999-2013.txt", 'x')