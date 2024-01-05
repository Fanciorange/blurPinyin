
from funzyInput import get_blured_pinyin,hz_2_py,removeTone



'''
一种5种不同的模糊发音：
BA_2_RF 平舌->翘舌
RF_2_BA 翘舌->平舌
back_2_front_nasal  后鼻音-》前鼻音
front_2_back_nasal  前鼻音-》后鼻音
other  其他单声母

参数比例设置在 0-1之间


'''

if __name__ == '__main__':
    # 示例：获取带数字声调且声调在末尾的拼音字符串
    hanzi = "《课文春天来了》 是一篇初中语文课文 通常出现在七年级上册"
    py = hz_2_py(hanzi)
    pt = get_blured_pinyin(py,0.8,0.5,0.8,0.2,0.5)
    pu =removeTone(pt,0.6)
    print(pu)