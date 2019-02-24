import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('--inputs', help='Directorio con los XMLs')
parser.add_argument('--output', help='Nombre del CSV a generarse')
args = parser.parse_args()
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = os.path.join(os.getcwd(), args.inputs)
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv(os.path.join(os.getcwd(),'CSV','{}.csv'.format(args.output)), index=None)
    print('Se han generado los CSVs')


main()
