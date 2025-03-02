
# 预估收益===============
# 计划电量 = 41394.0962
# 自发自用比例 = 0.65
# 基础电价 = 0.96
# 上网电价 = 0.4155
# 分成比例 = 0.65
#
# 预估自用收益 = 计划电量 * 基础电价 * 自发自用比例
# 预估上网收益 = 计划电量 * 上网电价 * (1 - 自发自用比例)
# 预估投资方收益 = 预估上网收益 + 预估自用收益 * 分成比例
# 预估业主方收益 = 预估自用收益 * (1 - 分成比例)

# print("预估自用收益"+str(预估自用收益))
# print("预估上网收益"+str(预估上网收益))
# print("预估投资方收益"+str(预估投资方收益))
# print("预估业主方收益"+str(预估业主方收益))
# print("总收益"+str(预估自用收益+预估上网收益))
# # 预估自用收益+预估上网收益 ==预估投资方收益+预估业主方收益
# print("总收益"+str(预估自用收益+预估上网收益))
# print("总收益"+str(预估投资方收益+预估业主方收益))

print('==========================================')
# =========实际收益======================
#
# 实际发


实际发电量 = 8926.63
自发自用电量=3570.625
余电上网电量=5355.978
实际自发自用比例 = 0.4
分成比例 = 0.65
尖 = 1.5
峰 = 1.3
平 = 0.65
谷 = 0.27
深谷 = 0.5

上网电价 = 0.421
低谷累计发电量0_7 = 5.23
高峰累计发电量7_12  = 4539.21
平累计发电量12_14 = 2903.61
峰累计发电量14_18 = 1847.52


# 实际自用收益 = 各时段发电量 * 实际自发自用比例 * 各时段电价
实际自用收益 = 低谷累计发电量0_7*0.27*实际自发自用比例 + 高峰累计发电量7_12*1.5*实际自发自用比例 + 平累计发电量12_14*0.65*实际自发自用比例 + 峰累计发电量14_18*1.3*实际自发自用比例

实际上网收益 = 余电上网电量 * 上网电价 * (1 - 实际自发自用比例)
实际总收益 = 实际上网收益 + 实际自用收益
实际投资方收益 = 实际上网收益 + 实际自用收益 * 分成比例
实际业主方收益 = 实际自用收益 * (1 - 分成比例)
print("实际自用收益"+str(实际自用收益))
print("实际上网收益"+str(实际上网收益))
print("实际总收益"+str(实际总收益))
print("实际投资方收益"+str(实际投资方收益))
print("实际业主方收益"+str(实际业主方收益))