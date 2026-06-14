#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torch
import numpy as np

# # 类型判断
# a = torch.randn(2, 3)  # 随机正态分布的初始化一个二维张量，size为[2 3]    N(0,1)（均值为0，方差为1）
# print(a.type())  # 返回张量的类型
# print(type(a))  # 返回python变量的数据类型
# print(isinstance(a, torch.FloatTensor))  # 参数的合法化检验
#
# # 同一数据在不同设备内类型不同
# print(isinstance(data, torch.cuda.DoubleTensor))  # CPU
# data = data.cuda()  # 将数据放置于GPU
# print(isinstance(data, torch.cuda.DoubleTensor))  # GPU

# # 标量（Scalar）（维度(dimension)和秩(rank)都为0）
# print(torch.tensor(1.))
# print(torch.tensor(1.3))  # 1.3是0维张量，即标量
# print(torch.tensor([1.3]))  # [1.3]是1维，长度为1的张量
# # 标量通常用于计算误差（loss）
# a = torch.tensor(2.2)
# print(a.shape)  # 获取a标量的shape
# print(len(a.shape))   # 获取a标量的长度size
# print(a.size())  # 获取a标量的size

# # 向量（vector）（维度(dimension)和秩(rank)都为1）
# print(torch.tensor([1.1]))  # 长度为1
# print(torch.tensor([1.1, 2.2]))  # 长度为2
# # 甚至长度是N的
# print(torch.FloatTensor(1))  # 生成一个长度size为1的1维张量，使用torch.randn()初始化的
# print(torch.FloatTensor(2))  # 生成一个长度size为2的1维张量
# # 用numpy数组生成Tensor
# data = np.ones(2)  # np.ones()创建指定维度和元素的矩阵
# print(data)
# print(torch.from_numpy(data))
# # 向量通常用于神经元的偏置（Bias）和神经网络线性层的输入（Linear Input）

# # 得到1维的张量（shape或size为1）
# a = torch.ones(2)
# print(a.shape)  # 或者print(a.size())

# # 得到2维的张量（shape或size为2）
# a = torch.randn(2, 3)
# print(a)
# print(a.shape)
# print(a.size(0))  # 取第一维的元素，或者print(a.shape[0])
# print(a.size(1))  # 取第二维的元素，或者print(a.shape[1])
# # Dim 2的张量通常用于批量的线性层输入(Linear Input Batch)

# # 得到3维的张量（shape或size为3）
# a = torch.rand(1, 2, 3)  # 随机均匀分布的初始化一个三维张量
# print(a)
# print(a.shape)
# print(a[0])  # 取第一维的元素
# print(a[0][0])  # 取第二维的第一个元素
# print(list(a.shape))
# # Dim 3的张量通常用于批量循环神经网络输入(RNN Input Batch)

# # 得到4维的张量（shape或size为4）
# a = torch.rand(2, 3, 28, 28)
# # 28, 28对应mnist数据集的长宽，通道3代表彩色图片（通道1代表灰度图片），图片数量2
# # CNN: (b,c,w,h)，即(batch,channel,width,height)
# print(a)
# print(a.shape)
# # 特别适用于卷积神经网络CNN
# # 补充
# print(a.numel())  # 查看张量的大小，numel是指Tensor占用内存的数量
# print(a.dim())  # 查看张量的维度/长度
# print(torch.tensor(1).dim())  # 查看标量的维度/长度

######

# 创建Tensor

# # 从numpy导入数据
# a = np.array([2, 3.3])  # 创建dim 1,size 2的数组
# print(torch.from_numpy(a))  # 将numpy数组转换成torch里的张量，从numpy导入的Float是Double类型
# a = np.ones([2, 3])  # 用numpy的ones()函数创建一个[2, 3]的矩阵
# print(torch.from_numpy(a))

# # 从列表里导入
# print(torch.tensor([2., 3.2]))
# print(torch.FloatTensor([2., 3.2]))
# print(torch.tensor([[2., 3.2], [1., 22.3]]))

# # 生成未初始化(uninitialized)的数据,(申请未初始化的内存空间)
# # torch.empty()  # 输入shape
# # torch.FloatTensor(dim1, dim2, dim3) # 输入shape
# # torch.IntTensor(dim1, dim2, dim3) # 输入shape
# print(torch.empty(1))
# print(torch.Tensor(2, 3))  # torch.tensor()接受的是带[]的数据，torch.Tensor()接受的是shape(虽然可以输入带[]的数据，但不推荐)
# print(torch.IntTensor(2, 3))
# print(torch.FloatTensor(2, 3))
# # 未初始化的数据存在隐患，需要用其它的类型将其覆盖掉，否则喂给神经网络会出现torch.nan或torch.inf

# # 设置默认类型
# # Tensor()是一个泛指概念，若不指定，默认是FloatTensor()
# print(torch.tensor([1.2, 3]).type())
# torch.set_default_tensor_type(torch.DoubleTensor)
# print(torch.tensor([1.2, 3]).type())
# # 增强学习一般使用double(64位有更高的精度)，其他一般使用float

# # 随机均匀分布初始化(rand/rand_like,randint)
# # rand() 随机的使用[0,1)的均值分布初始化
# print(torch.rand(3, 3))  # dim 2, shape [3,3] 的矩阵
# a = torch.rand(3, 3)
# print(torch.rand_like(a))  # 读取a的shape再喂给torch.rand()
# print(torch.randint(1, 10, [3, 3]))  # 需要指定最大和最小值[min,max)，即randint(min, max, shape)
# # 均匀采样0~10的Tensor，要用x=10*torch.rand(dim1,dim2)，randint只能采样整数

# # 随机标准正态分布的初始化
# # N(0,1)，其中N(u,std)，即N(均值,方差(或标准方差))
# print(torch.randn(3, 3))
# # 随机离散正态分布
# print(torch.normal(mean=torch.full([10], 0), std=torch.arange(1, 0, -0.1)))  # 自定义均值和方差
# # torch.normal()先将3x3矩阵打平成[9]的矩阵，使用torch.full()生成长度为10但都为0的均值，方差是从1到0步长为0.1逐次减小

# # torch.full()
# print(torch.full([2, 3], 7))  # 生成size为[2, 3]但全为7的张量
# print(torch.full([], 7))  # dim 0 的标量（Scalar）
# print(torch.full([1], 7))  # dim 1 的向量（Vector）

# # arange/range
# 生成等差的张量
# print(torch.arange(0, 10))  # 生成[0,10)差值为1的等差数列
# print(torch.arange(0, 10, 2))  # 生成[0,10)差值为2的等差数列
# # torch.range()在pytorch 0.5中已经移除

# # linspace/logspace
# # 生成等分的张量(线性间距向量)
# print(torch.linspace(0, 10, steps=4))  # steps表示等分的数量
# print(torch.linspace(0, 10, steps=10))
# print(torch.linspace(0, 10, steps=11))  # 等分切割
# print(torch.logspace(0, -1, steps=11))  # 等分切割[0,1]
# print(torch.logspace(0, 1, steps=11))  # 等分切割[0,10]
# print(torch.logspace(0, 2, steps=11, base=2))  # 等分切割[0,2^2]
# print(torch.logspace(0, 1, steps=11, base=10))  # 等分切割[0,10]
# # base参数可以设置为2，10，e等底数

# # ones/zeros/eye
# print(torch.ones(3, 3))  # 3x3 的全一矩阵
# print(torch.zeros(3, 3))  # 3x3 的全零矩阵
# print(torch.eye(3, 4))  # 3x4 的单位矩阵
#
# a = torch.zeros(3, 3)
# print(torch.ones_like(a))

# # randperm(随机打散)
# a = torch.randn(2, 3)
# b = torch.randn(2, 2)
# idx = torch.randperm(2)  # 生成[0,2)的随机索引
# print(idx)
# print(a[idx])
# print(b[idx])
# # 随机种子用来shuffle(洗牌)

######

# 索引与切片

# a = torch.rand(4, 3, 28, 28)

# # 直接索引
# print(a[0].shape)
# print(a[0, 0].shape)
# print(a[0, 0, 0, 0])

# # 取连续片段
# print(a[:2].shape)  # 取第一维的前两个元素
# print(a[:2, :1, :, :].shape)  # 取第一维的前两个元素，取第二维的前一个元素，后两维取全部，可不写
# print(a[:2, 1:, :, :].shape)  # 取第一维的前两个元素，第二维从第一个元素取到最后，后两维取全部，可不写
# print(a[:2, -1:, :, :].shape)  # 取第一维的前两个元素，第二维从最后取到最后，后两维取全部，可不写

# # 隔行取样
# print(a[:, :, 0:28:2, 0:28:2].shape)
# print(a[:, :, ::2, ::2].shape)

# # 特定索引取样
# print(a.index_select(0, torch.tensor([0, 2])).shape)
# print(a.index_select(1, torch.tensor([0, 2])).shape)
# print(a.index_select(2, torch.arange(28)).shape)
# print(a.index_select(2, torch.arange(8)).shape)

# # ...
# 当...出现时，右边索引理解为最右边
# print(a[...].shape)
# print(a[0, ...].shape)
# print(a[0, ..., ::2].shape)
# print(a[:, 1, ...].shape)
# print(a[..., :2].shape)

# # 用掩码(mask)索引
# # 弊端：将数据打平
# x = torch.randn(3, 4)
# mask = x.ge(0.5)  # dtype=torch.uint8 把所有大于0.5的索引给取出来
# print(torch.masked_select(x, mask))
# print(torch.masked_select(x, mask).shape)  # dim 1的随机长度
#
# # 使用打平(flatten)索引
# src = torch.tensor([[4, 3, 5], [6, 7, 8]])
# print(torch.take(src, torch.tensor([0, 2, 5])))  # [2,3] -> [6]

######

# 维度变换

# # View/reshape
# a = torch.rand(4, 1, 28, 28)
# print(a.view(4, 28*28))  # 合并channel，width，height(三者相乘)，变成二维[4, 784]，适合全连接层
# print(a.view(4, 28*28).shape)
# print(a.view(4*28, 28))  # 合并batch，channel，width(三者相乘)，变成二维[112, 28]，适合
# print(a.view(4*28, 28).shape)
# print(a.view(4*1, 28, 28).shape)
#
# b = a.view(4, 784)
# print(b.view(4, 28, 28, 1))  # Logic bug
# 数据维度丢失
# 数据的存储/维度的顺序很重要
# print(a.view(4, 783))  # view和原来的数据不一样会报错，Flexible but prone to corrupt

# a = torch.arange(4.)
# print(a)
# print(torch.reshape(a, (2, 2)))
# print(a.reshape(2, 2))

# # Squeeze/unsqueeze(挤压与展开)
# print(a.unsqueeze(0).shape)  # 在原来数据的第一维插入维度 等价于a.unsqueeze(-5).shape
# print(a.unsqueeze(-1).shape)  # 在原来数据的最后一维插入维度 等价于a.unsqueeze(4).shape
# print(a.unsqueeze(-4).shape)  # 在原来数据的倒数第四维插入维度 等价于a.unsqueeze(1).shape
# a.unsqueeze(5).shape 添加超出原维度的索引会报错
#
# b = torch.rand(32)  # bias
# # bias相当于给每个channel上的所有像素增加一个偏置
# f = torch.rand(4, 32, 14, 14)
# b = b.unsqueeze(1).unsqueeze(2).unsqueeze(0)
# print(b.shape)
#
# # squeeze
# b = torch.rand(1, 32, 1, 1)
# print(b.squeeze().shape)  # 不给参数挤压能挤压的，比如dim 1的维
# print(b.squeeze(0).shape)  # 挤压第一维 等价于b.squeeze(-4).shape
# print(b.squeeze(-1).shape)  # 挤压最后一维
# print(b.squeeze(1).shape)  # 挤压第二维，但挤压不了
#
# # Expand/repeat(维度扩展)
# b = torch.rand(1, 32, 1, 1)
# print(b.expand(4, 32, 14, 14).shape)  # expand要保证维度一致
# print(b.expand(-1, 32, -1, -1).shape)  # -1是偷懒，因为有时候不知道维度
# print(b.expand(-1, 32, -1, -4).shape)  # -4是个bug
#
# # 不建议repeat
# print(b.repeat(4, 32, 1, 1).shape)  # 主动复制内存数据的方式
# print(b.repeat(4, 1, 1, 1).shape)
# print(b.repeat(4, 1, 32, 32).shape)
#
# # Transpose/t/permute(矩阵转置)
# # t()
# b = torch.rand(1, 32, 1, 1)
# print(b.t())  # .t()只适用于2D
# a = torch.rand(3, 4)
# print(a.t())  # 矩阵转置 [3,4] -> [4,3]
#
# # transpose()
# a = torch.rand(4, 3, 32, 32)
# print(a.transpose(1, 3).shape)
# # print(a.transpose(1, 3).view(4, 3*32*32).view(4, 3, 32, 32))  # 报错，数据的维度顺序必须和存储顺序一致
# a1 = a.transpose(1, 3).contiguous().view(4, 3*32*32).view(4, 3, 32, 32)  # 错误操作
# a2 = a.transpose(1, 3).contiguous().view(4, 3*32*32).view(4, 32, 32, 3).transpose(1, 3)  # .contiguous()把数据变成连续的
# print(a1.shape, a2.shape)
# print(torch.all(torch.eq(a, a1)))  # .eq()判断数据是否一致 .all() 返回所有数据
# print(torch.all(torch.eq(a, a2)))
# # .view()会导致维度顺序关系模糊，需要人为追踪
#
# # permute()
# a = torch.rand(4, 3, 28, 28)
# print(a.transpose(1, 3).shape)
# b = torch.rand(4, 3, 28, 32)
# print(b.transpose(1, 3).shape)
# print(b.transpose(1, 3).transpose(1, 2).shape)
# print(b.permute(0, 2, 3, 1).shape)
