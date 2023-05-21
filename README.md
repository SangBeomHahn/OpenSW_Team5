# OpenSW_Team5_MLOps_Master!!!🔥
*Final_Project: mmdetection 기반 K-fashion 데이터 학습

## Introduction

본 프로젝트는 오픈소스 모델인 mmdetection을 활용하여 custom 데이터로 AI 모델을 학습하고 최종적으로는 docker image로 모델 개발 환경을 배포하는 것을 목표로 하고 있다. 또한 그 과정에서 오픈소스 협업 소프트웨어를 활용하여 팀원들과 이슈 및 형상관리를 실시한다.

![predict](https://github.com/SangBeom-Hahn/OpenSW_Team5/blob/main/sample_image/main.jpg)


## Dataset

|Data|데이터 수|Train 데이터 수|Val 데이터 수|세부사항|
|:-:|:-:|:-:|:-:|:-:|
|1|5826|4740|1186|K-fashion|


학습에는 K-fashion 데이터 셋을 사용, 각 이미지는 데이터 구축 사업을 위해 제작된 데이터로 이미지 jpg 파일과 그에 대응하는 annotation json 파일로 존재한다.

## Model

![project_pipeline](https://github.com/SangBeom-Hahn/OpenSW_Team5/blob/main/sample_image/mmdetection.PNG)

OpenMMLab은 Pytorch 기반으로 작성된 오픈 소스 프로젝트이며 학술 연구 및 산업 분야에서도 널리 사용된다. OpenMMLab은 Computer Vision 분야의 여러 Vision Library와 최신 알고리즘들 그리고 수많은 pretrained model을 제공하는데 뛰어난 구현 성능, 효율적 Module 설계와 Config 시스템 기반을 통해 Data부터 Model 학습, 평가까지 아우르는 간편한 Pipeline을 적용하였다.

OpenMMLab에서 제공하는 Detection 라이브러리인 MMDetection의 MASK-RCNN을 사용하여 instace segmentation를 진행한다.

https://github.com/open-mmlab/mmdetection



## Project Structure

```
OpenSW_Team5
├── Final Project_MMDetection
├── mmdetection_code
├── team_assignment
└── bot.py
```

- Final Project_MMDetection : 데이터 전처리
- mmdetection_code : MASK-RCNN 코드
- bot.py : 텔레그램 봇 실행 코드

## Getting started
- Download the code from GitHub:
```bash
git clone https://github.com/SangBeom-Hahn/OpenSW_Team5
cd OpenSW_Team5/mmdetection_code
```

- Install the python libraries.
```bash
pip install -r requirements.txt
```

- Run the python script
```bash
python demo/image_demo.py ${IMAGE_FILE} \
    configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py \
    checkpoints/epoch_12.pth \
    --device cuda:0
```

## Local
```
python==3.7.13
cuda 10.0 - rtx 2080 super
```

## Requirements
```
pytorch==1.6.0
torchvision==0.7.0
mmcv(mmcv-full)==1.7.0
mmdet==2.26.0
```

## Using k_fashion with Docker

```shell
docker pull hsb422/k_fashion:0.01
```

- Run it with

Download model checkpoint and move it to mmdetection_volume directory

```shell
docker run -it -v mmdetection_volume:/mmdetection/data hsb422/k_fashion
```


## Authors

|피선우|한상범|홍찬의|
|:-:|:-:|:-:|
|[Github](https://github.com/SunWoo98Pi)|[Github](https://github.com/SangBeom-Hahn)|[Github](https://github.com/hcu55)|

- Blog : [Tistory(openSW)](https://hsb422.tistory.com/entry/%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-SW-%EC%8B%A4%EC%8A%B5-final-project)
