import os
import json

licenses = [
		{
			"name": "",
			"id": 0,
			"url": ""
		},
        {
			"name": "",
			"id": 1,
			"url": ""
		},
        {
			"name": "",
			"id": 2,
			"url": ""
		},
        {
			"name": "",
			"id": 3,
			"url": ""
		},
        {
			"name": "",
			"id": 4,
			"url": ""
		},
        {
			"name": "",
			"id": 5,
			"url": ""
		},
        {
			"name": "",
			"id": 6,
			"url": ""
		},
        {
			"name": "",
			"id": 7,
			"url": ""
		},
        {
			"name": "",
			"id": 8,
			"url": ""
		},
        {
			"name": "",
			"id": 9,
			"url": ""
		},
        {
			"name": "",
			"id": 10,
			"url": ""
		},
        {
			"name": "",
			"id": 11,
			"url": ""
		}
	]

info = {
	    "contributor": "",
		"date_created": "",
		"description": "",
		"url": "",
		"version": "",
		"year": ""
	}

categories = [
        {
            "id": 0,
            "name": "onepiece(dress)",
            "supercategory": "onepiece(dress)"
        },
        {
            "id": 1,
            "name": "jumpsuite",
            "supercategory": "jumpsuite"
        },
        {
            "id": 2,
            "name": "cardigan",
            "supercategory": "cardigan"
        },
        {
            "id": 3,
            "name": "coat",
            "supercategory": "coat"
        },
        {
            "id": 4,
            "name": "jacket",
            "supercategory": "jacket"
        },
        {
            "id": 5,
            "name": "jumper",
            "supercategory": "jumper"
        },
        {
            "id": 6,
            "name": "pants",
            "supercategory": "pants"
        },
        {
            "id": 7,
            "name": "skirt",
            "supercategory": "skirt"
        },
        {
            "id": 8,
            "name": "blouse",
            "supercategory": "blouse"
        },
        {
            "id": 9,
            "name": "shirt",
            "supercategory": "shirt"
        },
        {
            "id": 10,
            "name": "sweater",
            "supercategory": "sweater"
        },
        {
            "id": 11,
            "name": "t-shirt",
            "supercategory": "t-shirt"
        }]

rootDir = './Change Number & Combine/'
class_json = [
    '0. onepiece(dress).json', '1. onepiece(jumpsuite).json', '2. outer_cardigan.json', '3. outer_coat.json', '4. outer_jacket.json', '5. outer_jumper.json', '6. pants.json', '7. skirt.json', '8. top_blouse.json', '9. top_shirt.json', '10. top_sweater.json', '11. top_t-shirt.json']

train_object = {}
val_object = {}

train_anno = []
val_anno = []
train_images = []
val_images = []

divide = [860, 44, 389, 480, 480, 385, 270, 329, 460, 293, 297, 453] # Train : Valid = 8 : 2

categoryID = 0
id = 0
train_images_id = 0
val_images_id = 0
train_anno_id = 0
val_anno_id = 0
# train_anno_id = 1
# val_anno_id = 1

train_pre_img = ''
val_pre_img = ''
train_img_id = -1
val_img_id = -1

for i in class_json:
    print(i)
    
    with open(rootDir + i, 'r') as f:
        json_data = json.load(f)
        
        for combined_json_categories in json_data["categories"]:
            combined_json_categories["id"] = categoryID
            
        for images in json_data["images"]:
            if(id < divide[categoryID]):
                images["file_name"] = os.path.basename(images["file_name"])
                images["id"] = train_images_id
                train_images.append(images)
                train_images_id += 1
                
            else:
                images["file_name"] = os.path.basename(images["file_name"])
                images["id"] = val_images_id
                val_images.append(images)
                val_images_id += 1
            id += 1
            
        id = 0
        
        for anno in json_data['annotations']:
            anno["category_id"] = categoryID
            
            if(id < divide[categoryID]):
                anno["id"] = train_anno_id
                train_anno.append(anno)
                
                if anno["image_id"] != train_pre_img :
                    train_img_id += 1
                train_pre_img = anno["image_id"]
                anno["image_id"] = train_img_id
                
                train_anno_id += 1
                
            else:
                anno["id"] = val_anno_id
                val_anno.append(anno)
                
                if anno["image_id"] != val_pre_img :
                    val_img_id += 1
                val_pre_img = anno["image_id"]
                anno["image_id"] = val_img_id
                
                val_anno_id += 1
            id += 1
            
        id = 0
        
    categoryID += 1

train_object["licenses"] = licenses
train_object["info"] = info
train_object["categories"] = categories
train_object["images"] = train_images
train_object["annotations"] = train_anno

val_object["licenses"] = licenses
val_object["info"] = info
val_object["categories"] = categories
val_object["images"] = val_images
val_object["annotations"] = val_anno

with open('./train.json', 'w') as outfile:
    json.dump(train_object, outfile, indent='\t')
    
with open('./val.json', 'w') as outfile:
    json.dump(val_object, outfile, indent='\t')