import os
import sys
import zipfile
from urllib.request import urlretrieve

# download GDA2020 digital boundary files in 2021 (based on SA2)
print(f'Downloading: 2021 GDA2020 digital boundary files.')
landing_dir_temp = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/'
URL = 'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip'
landing_dir = f'{landing_dir_temp}SA2_2021_AUST_SHP_GDA2020.zip'
urlretrieve(URL, landing_dir)

# unzip the file
zip_file_path = landing_dir
extracted_folder_path = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/shapefile/SA2_2021_AUST_SHP_GDA2020/'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)
print(f'Finished.')

###########################################################################################################################

# download 'Vicmap Admin - Postcode Polygon' (Shape file for Vic based on postcode)
print(f'Downloading: Vicmap Admin - Postcode Polygon.')
landing_dir_temp = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/'
URL = 'https://s3.ap-southeast-2.amazonaws.com/cl-isd-prd-datashare-s3-delivery/Order_IKG8AK.zip'
landing_dir = f'{landing_dir_temp}postcode_polygon.zip'
urlretrieve(URL, landing_dir)

# unzip the file
zip_file_path = landing_dir
extracted_folder_path = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/shapefile/postcode_polygon/'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)
print(f'Finished.')

###########################################################################################################################

# download shape file for PTV Train Station Platform
print(f'Downloading: PTV Train Station Platform.')
landing_dir_temp = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/'
URL = 'https://s3.ap-southeast-2.amazonaws.com/cl-isd-prd-datashare-s3-delivery/Order_W0XS5B.zip?orderid=G2E2YE'
landing_dir = f'{landing_dir_temp}PTV_Train_Station.zip'
urlretrieve(URL, landing_dir)

# unzip the file
zip_file_path = landing_dir
extracted_folder_path = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/shapefile/PTV_Train_Station/'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)
print(f'Finished.')

#############################################################################################################################

# download shape file for neighborhood parks and reserves
print(f'Downloading: neighborhood parks and reserves.')
landing_dir_temp = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/'
URL = ' https://s3.ap-southeast-2.amazonaws.com/cl-isd-prd-datashare-s3-delivery/Order_X3J0T7.zip'
landing_dir = f'{landing_dir_temp}Parks_reserves.zip'
urlretrieve(URL, landing_dir)

# unzip the file
zip_file_path = landing_dir
extracted_folder_path = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/external_data/shapefile/Parks_reserves/'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)
print(f'Finished.')

#################################################################################################################################