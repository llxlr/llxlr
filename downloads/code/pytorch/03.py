#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torch

# Broadcast 自动扩展
# Expand自动维度扩展、扩展时不需要拷贝数据，节省数据
# Key idea
# 前面没有维度的话插入一个维度（Insert 1 dim ahead）
# A张量没有维度，插入1维shape变成了1，然后自动扩展到B张量
# Feature maps: [4, 32, 14, 14]（可能是经过一个卷积神经网络后的Feature maps）
# 在channel上叠加32个偏置Bias，手动插入两个维度: [32, 1, 1] => [1, 32, 1, 1] => [4, 32, 14, 14]
# size一致，可进行对应位置元素相加

# 1.for actual demanding
# [class, students, scores]  # 班级成绩单统计
# Add bias for every students: +5 score
# [4, 32, 8] + [4, 32, 8]
# [4, 32, 8] + [5.0]

# 2. memory consumption
# [4, 32, 8] => 1024
# [5.0] => 1

# A[] B[]
# Match from Last dim
# if current dim=1, expand to same
# if either has no dim,insert one dim and expand to same
# otherwise,Not broadcasting-able


