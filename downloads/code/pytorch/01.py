#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torch
print(torch.cuda.is_available())  # True则安装成功

# cuda 测试
x = torch.tensor([1.0])
x = x.cuda()  # 数据放置于gpu
print(x)  # tensor([1.], device='cuda:0')

# cudnn 测试
from torch.backends import cudnn
print(cudnn.is_acceptable(x))  # True
