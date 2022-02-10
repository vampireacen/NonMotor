import os
os.system('python -m torch.distributed.launch --nproc_per_node=4 train.py ../configs/swin/mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_adamw_1x_coco.py 4 --launcher pytorch')