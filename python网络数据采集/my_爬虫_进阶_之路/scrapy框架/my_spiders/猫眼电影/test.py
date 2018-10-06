# coding:utf-8

'''
@author = super_fazai
@File    : test.py
@connect : superonesfazai@gmail.com
'''

from fzutils.common_utils import save_base64_img_2_local
from fontTools.ttLib import TTFont
from pprint import pprint
from xmltodict import parse

'''字体保存到本地'''
a = 'base64,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'
save_path = '/Users/afa/Desktop/x.ttf'
font_xml_save_path = '/Users/afa/Desktop/x.xml'
res = save_base64_img_2_local(save_path=save_path, base64_img_str=a)
print(res)

font = TTFont(save_path)
font.saveXML(font_xml_save_path)

with open(font_xml_save_path, 'r') as f:
    xml_content = f.read()

xml_dict = dict(parse(xml_input=xml_content))
# pprint(xml_dict)
_ = xml_dict['ttFont']['hmtx']['mtx'][1:-1]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_ = [dict(item).get('@name') for item in _]
_ = list(zip(_, a))
pprint(_)