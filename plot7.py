from matplotlib import pyplot as plt
import numpy as np

size = 0.25
base = 50


plt.rcParams['font.family'] = 'SimHei'
fig, ax = plt.subplots(figsize = (10, 10))

vals_middle = np.array([
    [47.5,11.7,15.2,9.6],
    [0,44.8,7.5,0], 
    [9.2, 68.5 , 0, 0],
    [1.2, 7.2, 0, 0],
    [80,0, 0, 0],
    [1.7, 18.9, 0, 0]
])

vals_outer = np.array([ 
    [47.5,11.7,15.2,9.6],
    [0,36.6,8.2,7.5], 
    [9.2,38.1,30.4, 0],
    [1.2, 5.8, 1.4, 0],
    [80,0, 0, 0],
    [1.7, 18.9, 0, 0]
])

vals_inner = vals_middle.sum(axis=1)

# 最内圈使用的数值为内圈各类数据加上base
vals_first = vals_inner + base

'''
第二圈使用的数值, 因为最内圈每个类别都加上了base, 所以为了确保第二圈的数值和内圈相匹配, 第二圈的各类别要按照各自所占的比例分配各类的总数值.
'''
vals_second = np.zeros((6, 4))
for i in range(6):
    s_a = vals_first[i]
    s_b = vals_middle[i].sum()
    # 如果第二圈某类总数值为0, 则分配base.
    if s_b == 0.0:
        vals_second[i][1] = base
        continue
    for j in range(4):
        vals_second[i][j] = (vals_middle[i][j] / s_b) * s_a
    
# 第三圈使用的数值, 和上方同理
vals_third = np.zeros((6, 4))
for i in range(6):
    s_a = vals_first[i]
    s_b = vals_outer[i].sum()
    if s_b == 0.0:
        vals_third[i][1] = base
        continue
    for j in range(4):
        vals_third[i][j] = (vals_outer[i][j] / s_b) * s_a


# 获取colormap tab20c和tab20b的颜色
cmap_c = plt.get_cmap("tab20c")
cmap_b = plt.get_cmap("tab20b")

# 使用tab20c的全部颜色和tab20b中的 5至8 颜色
cmap_1 = cmap_c(np.arange(20))
cmap_2 = cmap_b(np.array([4, 5, 6, 7]))

# 内圈的颜色是每4个颜色中色彩最深的那个. vstack是将两类颜色叠加在一起
inner_colors = np.vstack((cmap_1[::4], cmap_2[0]))
# 外圈的颜色是全部24种颜色
outer_colors = np.vstack((cmap_1, cmap_2))



labels_first=["餐厨废弃物\n{}万吨".format(vals_inner[0]), 
        "农业秸秆\n{}万吨".format(vals_inner[1]), 
        "水草\n151.2万吨", 
        "园林绿化\n废弃物\n{}万吨".format(vals_inner[3]),
        "淤泥\n432.0万吨",
        "畜禽粪便\n21.6万吨"
        ]

labels_seocnd=[
    "未分类收集\n67.6万吨",
    "生物干化\n3.7万吨",
    "厌氧发酵\n10.2万吨",
    "油水分离\n2.6万吨",

    "",
    "粉碎\n46.8万吨",
    "好氧发酵\n3.5万吨",
    "",

    "未处理\n4.2万吨",
    "藻水分离\n147.0万吨",
    "",
    "",

    "未处理\n1.2万吨",
    "粉碎\n7.2万吨",
    "",
    "",

    "堆放\n432.0万吨",
    "",
    "",
    "",

    "未处理\n0.7万吨",
    "好氧发酵\n19.9万吨",
    "",
    "",
]

labels_third=[
    "未处理\n67.5万吨",
    "肥料化、发电\n3.7万吨",
    "沼气、沼渣发电\n10.2万吨",
    "焚烧\n2.6万吨",

    "",
    "还田\n42.6万吨",
    "燃料化\n4.2万吨",
    "肥料化\n3.5万吨",

    "未利用\n4.2万吨",
    "燃料化\n80.2万吨",
    "肥料化\n66.8万吨",
    "",

    "未利用\n1.2万吨",
    "肥料化\n5.8万吨",
    "燃料化\n1.4万吨",
    "",

    "未利用\n432.0万吨",
    "",
    "",
    "",

    "未利用\n0.7万吨",
    "肥料化\n19.9万吨",
    "",
    "",
]


handles, labels =  ax.pie(vals_first, radius=1-size-size, 
                labels=labels_first, 
                labeldistance=0.5,  rotatelabels=True, textprops={'fontsize': 11}, 
                colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals_second.flatten(),   radius=1-size, colors=outer_colors,
    labels=labels_seocnd, 
    labeldistance=0.7,  rotatelabels=True, textprops={'fontsize': 11}, 
    wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals_third.flatten(), radius=1, colors=outer_colors,
    labels=labels_third, 
    labeldistance=0.8,  rotatelabels=True, textprops={'fontsize': 11},
    wedgeprops=dict(width=size, edgecolor='w'))


plt.title('某市有机废弃物产生、处理、利用情况', fontsize=25)
plt.legend(handles=handles, labels=[
        "餐厨废弃物", 
        "农业秸秆", 
        "水草", 
        "园林绿化废弃物", 
        "淤泥",
        "畜禽粪便"],
        loc = 1
        )
plt.show()
