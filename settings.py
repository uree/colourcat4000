#folders
text_folder = 'absolute path to the folder containing pdfs' # contians pdfs; use absoute path
md_folder = text_folder+'notes/'


# colour coding
# rgb 16-bit notation
# if colours differ slightly
colours = [{'category': 'argument', 'codes': [{'rgb-hex': [65535, 65535, 0], 'device_name': 'pdf-x-view'}, {'rgb-hex': [65535, 65535, 0], 'device_name': 'iannotate'}]}, {'category': 'continued', 'codes': [{'rgb-hex': [32125, 40606, 49344], 'device_name': 'pdf-x-view'}, {'rgb-hex': [32124, 40606, 49343], 'device_name': 'iannotate'}, {'rgb-hex': [0, 0, 65535], 'device_name': 'iannotate-old'}]}, {'category': 'quote', 'codes': [{'rgb-hex': [65535, 32896, 0], 'device_name': 'pdf-x-view'}, {'rgb-hex': [65535, 32767, 0], 'device_name': 'iannotate'}]}, {'category': 'data', 'codes': [{'rgb-hex': [0, 65535, 0], 'device_name': 'pdf-x-view'}, {'rgb-hex': [0, 65535, 0], 'device_name': 'iannotate'}]}, {'category': 'derived', 'codes': [{'rgb-hex': [16448, 57568, 53456], 'device_name': 'pdf-x-view'}, {'rgb-hex': [0, 65535, 65535], 'device_name': 'iannotate'}]}, {'category': 'useful', 'codes': [{'rgb-hex': [65535, 0, 65535], 'device_name': 'pdf-x-view'}, {'rgb-hex': [65535, 0, 65535], 'device_name': 'iannotate'}]}]


# elasticsearch
es_index = 'highlights'
es_type = 'highlight'
