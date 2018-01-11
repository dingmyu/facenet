#!/bin/bash
python finetune_v1_result.py --logs_base_dir='log' --models_base_dir='log' --pretrained_model='log/20180109-155333/model-20180109-155333.ckpt-2000' --data_dir='ASD_train' --batch_size=32 --learning_rate=0.0002 --image_size=224 --gpu_memory_fraction=0.7 --epoch_size=300
