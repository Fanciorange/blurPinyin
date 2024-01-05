import json
import random
from pypinyin import pinyin, Style
from blur_utils import get_check_by_name,get_fun_by_name
filenamelis =['BA_2_RF','RF_2_BA','back_2_front_nasal','front_2_back_nasal','other']
prefix = "tone_rule/"
def select_elements_with_ratio(input_list, ratio):
    num_elements = int(len(input_list) * ratio)
    selected_elements = random.sample(input_list, num_elements)
    return selected_elements

def hz_2_py(hz):
    pinyin_str = pinyin(hz, style=Style.TONE3, heteronym=True)
    return " ".join([item[0] for item in pinyin_str])
def getMAP():
    mp_lis = {}
    for filename in filenamelis:
        with open(prefix+filename,'r',encoding='utf-8') as f:
            content = f.read()
            mp_lis[filename] = {}
            content  =json.loads(content)
            mp_lis[filename]['mp'] =content
            mp_lis[filename]['pylis'] = []
    return mp_lis


'''这里的ratio_lis是对于上面filenamelis 里面五个不同模糊音的比例'''
def get_final_mp(py,BA_2_RF=0.5,RF_2_BA=0.5,back_2_front_nasal=0.5,front_2_back_nasal=0.5,other=0.5):
    ratio_lis = [BA_2_RF,RF_2_BA,back_2_front_nasal,front_2_back_nasal,other]
    mp_lis = getMAP()
    filtered_list = [x for x in py.split(" ") if x.strip()]

    filtered_list = [x[:-1]  if x[-1].isdigit() else x for x in filtered_list]
    py_set = set(filtered_list)

    py_change={}
    for item in py_set:
        for filename in filenamelis:
            if get_check_by_name(filename)(item,mp_lis[filename]['mp']):
                mp_lis[filename]['pylis'].append(item)


    for filename,ratio in zip(filenamelis,ratio_lis):
        pylis = mp_lis[filename]['pylis']
        selected_py = select_elements_with_ratio(pylis, ratio)
        for item_py in selected_py:
            if item_py not in py_change:
                py_change[item_py] =[]
            py_change[item_py].append(filename)

    final_py_mp={}
    for py,change_lis in py_change.items():
        temp_py = py
        for change  in change_lis:
            temp_py = get_fun_by_name(change)(temp_py,mp_lis[change]['mp'])
        final_py_mp[py] =temp_py
    return final_py_mp

def get_blured_pinyin(py, BA_2_RF=0.5, RF_2_BA=0.5, back_2_front_nasal=0.5, front_2_back_nasal=0.5, other=0.5):
    ratio_lis = [BA_2_RF,RF_2_BA,back_2_front_nasal,front_2_back_nasal,other]
    filtered_list = py.split(" ")
    tone = [x[-1]  if len(x) and x[-1].isdigit() else '' for x in filtered_list]
    filtered_list = [x[:-1]  if len(x) and x[-1].isdigit() else x for x in filtered_list]
    final_py_mp = get_final_mp(py,BA_2_RF,RF_2_BA,back_2_front_nasal,front_2_back_nasal,other)
    for i,py in enumerate(filtered_list):
        if py not in final_py_mp:
            final_py_mp[py]=py
        filtered_list[i] = final_py_mp[py]+tone[i]
    return ' '.join(filtered_list)


def random_replace(lst, ratio, replace_value=''):
    # 计算要替换的元素数量
    num_elements_to_replace = int(len(lst) * ratio)

    # 生成要替换的元素的索引列表
    indices_to_replace = random.sample(range(len(lst)), num_elements_to_replace)

    # 替换元素
    for index in indices_to_replace:
        lst[index] = replace_value

    return lst
def removeTone(py,ratio):
    pyls =[item[:-1]  if len(item) and item[-1].isdigit() else item for item in py.split(" ")]
    tonels = [item[-1] if len(item) and item[-1].isdigit() else '' for item in py.split(" ")]
    tonels = random_replace(tonels,ratio)
    for i in range(len(pyls)):
        pyls[i]+=tonels[i]
    return " ".join(pyls)