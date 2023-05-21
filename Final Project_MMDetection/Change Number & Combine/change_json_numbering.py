import json

file_path_1 = 'C:/Users/PiSunWoo-RTOS/Desktop/Mask_RCNN_실습데이터/onepiece(dress)_02/annotations/instances_default.json'
file_path_2 = 'C:/Users/PiSunWoo-RTOS/Desktop/Mask_RCNN_실습데이터/onepiece(dress)_03/annotations/instances_default.json'

with open(file_path_1, 'r') as f:
    json_data_1 = json.load(f)

with open(file_path_2, 'r') as f:
    json_data_2 = json.load(f)

print(len(json_data_1['images']))
print(len(json_data_2['images']))
print(len(json_data_1['annotations']))
print(len(json_data_2['annotations']))

json_1_id_len = len(json_data_1['images'])
json_2_id_len = len(json_data_2['images'])
for image_id in range(json_2_id_len):
    json_data_2['images'][image_id]['id'] += json_1_id_len
    
json_1_id_len = len(json_data_1['annotations'])
json_2_id_len = len(json_data_2['annotations'])
for image_id in range(json_2_id_len):
    json_data_2['annotations'][image_id]['id'] += json_1_id_len
    json_data_2['annotations'][image_id]['image_id'] += json_1_id_len
    
with open(file_path_2, 'w', encoding='utf-8') as file:
    json.dump(json_data_2, file, indent="\t")