def BA_2_RF_Check(py,mp):
    if len(py)>1 and py[1]!='h' and py[0] in mp.keys():
        return 1
    return 0
def RF_2_BA_Check(py,mp):
    if len(py)>=3 and py[0:2] in mp.keys():
        return 1
    return 0
def Back_2_Front_Nasal_Check(py,mp):
    if len(py)>3 and py[-3:] in mp.keys():
        return 1
    return 0
def Front_2_Back_Nasal_Check(py,mp):
    if len(py)>2 and py[-2:] in mp.keys():
        return 1
    return 0
def Other_Check(py,mp):
    if py[0] in mp.keys():
        return 1
    return 0

def BA_2_RF_Fun(py,mp):
    if len(py)>1 and py[1]!='h' and py[0] in mp.keys():
        return mp[py[0]]+py[1:]
    return py
def RF_2_BA_Fun(py,mp):
    if len(py)>=3 and py[0:2] in mp.keys():
        return mp[py[0:2]]+py[2:]
    return py
def Back_2_Front_Nasal_Fun(py,mp):
    if len(py)>3 and py[-3:] in mp.keys():
        return py[:-3]+mp[py[-3:]]
def Front_2_Back_Nasal_Fun(py,mp):
    if len(py)>2 and py[-2:] in mp.keys():
        return py[:-2]+mp[py[-2:]]
    return py
def Other_Fun(py,mp):
    if py[0] in mp.keys():
        return mp[py[0]]+py[1:]
    return py
def get_fun_by_name(func_name):
    if func_name == 'BA_2_RF':
        return BA_2_RF_Fun
    elif func_name == 'RF_2_BA':
        return RF_2_BA_Fun
    elif func_name == 'back_2_front_nasal':
        return Back_2_Front_Nasal_Fun
    elif func_name == 'front_2_back_nasal':
        return Front_2_Back_Nasal_Fun
    elif func_name == 'other':
        return Other_Fun
    else:
        # 处理未知的 func_name
        raise ValueError(f"Unknown function name: {func_name}")
def get_check_by_name(func_name):
    if func_name == 'BA_2_RF':
        return BA_2_RF_Check
    elif func_name == 'RF_2_BA':
        return RF_2_BA_Check
    elif func_name == 'back_2_front_nasal':
        return Back_2_Front_Nasal_Check
    elif func_name == 'front_2_back_nasal':
        return Front_2_Back_Nasal_Check
    elif func_name == 'other':
        return Other_Check
    else:
        # 处理未知的 func_name
        raise ValueError(f"Unknown function name: {func_name}")