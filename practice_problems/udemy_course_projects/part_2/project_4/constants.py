from parse_utils import parse_date

# Files
fname_personal = 'project_4_data_file/personal_info.csv'
fname_employment = 'project_4_data_file/employment.csv'
fname_vehicles = 'project_4_data_file/vehicles.csv'
fname_update_status = 'project_4_data_file/update_status.csv'
fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicle_parser = (str, str, str, int)
update_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Namedtuples names..
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

# Field Inclusion/Exclusion
presonal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = presonal_fields_compress, employment_fields_compress, vehicle_fields_compress, update_status_fields_compress
