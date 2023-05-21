import json

file_path_1 = 'C:/Users/PiSunWoo-RTOS/Desktop/Mask_RCNN_실습데이터/11. top_t-shirt_01/annotations/instances_default.json'
file_path_2 = 'C:/Users/PiSunWoo-RTOS/Desktop/Mask_RCNN_실습데이터/11. top_t-shirt_02/annotations/instances_default.json'

with open(file_path_1, 'r') as f:
    json_data_1 = json.load(f)
    
with open(file_path_2, 'r') as f:
    json_data_2 = json.load(f)
    
json_1_images_id_len = len(json_data_1['images'])
json_2_images_id_len = len(json_data_2['images'])
json_1_annotations_id_len = len(json_data_1['annotations'])
json_2_annotations_id_len = len(json_data_2['annotations'])

for i in range(json_2_images_id_len):
    json_data_1['images'].append(json_data_2['images'][i])
    
for i in range(json_2_annotations_id_len):
    json_data_1['annotations'].append(json_data_2['annotations'][i])
    
with open(file_path_1, 'w', encoding='utf-8') as file:
    json.dump(json_data_1, file, indent="\t")