| 第三届计图挑战赛赛题二：大规模无监督予以分割赛题

# Jittor 推理出测试集中图片对应的伪标签分割图 

![主要结果](https://data.educoder.net/api/attachments/4856567?type=image/png)


## 简介

本项目包含了第三届计图挑战赛计图 - 大规模无监督予以分割赛题。本项目的特点是：采用了对baseline模型进行超参数改进。

## 安装 

本项目可在 1张 4090上运行，训练时间约为 4 小时。

#### 运行环境
- ubuntu 20.04 LTS
- python >= 3.8
- jittor >= 1.3.0

#### 安装依赖
执行以下命令安装 python Jittor依赖
```
conda create -n jt python=3.8
conda activate jt
python -m pip install jittor 
python -m jittor.test.test_core 
python -m jittor.test.test_example
```

## 训练

单卡训练可运行以下命令：
```
对luss50_pass_jt.sh进行train.py
```



## 致谢
| 对参考的论文、开源库予以致谢，可选

此项目基于论文 *Large-scale unsupervised semantic segmentation* 实现，部分代码参考了 [jittor-gan](https://github.com/Jittor/gan-jittor)。

## 注意事项

点击项目的“设置”，在Description一栏中添加项目描述，需要包含“jittor”字样。同时在Topics中需要添加jittor。

![image-20220419164035639](https://s3.bmp.ovh/imgs/2022/04/19/6a3aa627eab5f159.png)