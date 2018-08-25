#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def diagnotic(name_length):
    """日本人の場合英語で入力された名前は3文字以上8文字以下であることが大半になることを利用して、
       名前の長さをresultsのindexに使う"""
    
    results = ["おヌシの精力は「9000000000000」じゃと!? 参った...",
                "おヌシの精力は「-5353535353535353」。赤マムシでも飲んで出直すんじゃな。",
                "おヌシの精力は「530」。ワシといい勝負じゃな。フォッフォッフォ。",
                "おヌシの精力は「3000」じゃ。ま、歳相応といったところかの。精進せい",
                "おヌシの精力は「1111111」じゃ。なかなかのもんじゃが、あんまりヤり過ぎると感度が悪くなるぞ、用心せい。",
                "おヌシの精力は「8181」じゃ。おぬしが男なら巨乳好き、女ならデカマラ中毒かの。やれやれ。",
                "おヌシの精力は...ちょっと診断不可能じゃな。すまん、そんな時もある"]

    if name_length in list(range(3, 9)):
        result = results[name_length-3]

    else:
        result = results[6]

    return result

def detail_diagnostic(name_length):
    """diagnostic同様名前の長さをキーにして詳細な性格分析データをリストから一つ選ぶ"""

    type1 = ["ドSアブノーマル型", 5, 5, 5, 5, 1]  
    type2 = ["淡白にことを済ませたがるタイプ", 1, 1, 3, 4, 2]   
    type3 = ["典型的なドM", 4, 5, 3, 2, 5]     
    type4 = ["普段だけでなく事後も優しいタイプ", 5, 4, 5, 5, 2]     
    type5 = ["普段優しいくせに事後はそっけないクズ", 3, 4, 4, 5, 2]                  
    type6 = ["自己満に走りがちな自称ヤリチン/マン", 2, 1, 5, 4, 2]
    type7 = ["診断不能", 0, 0, 0, 0, 0]

    all_types = [type1, type2, type3, type4, type5, type6, type7]

    if name_length in list(range(3, 9)):
        type = all_types[name_length-3]
    else:
        type = all_types[6]

    type_name = type[0]
    character = type[1:]
    labels = ["アブノーマル度", "Sex時の豹変度", "夜の営みに対する自信", "ベッドイン速度", "Mっ気"]

    return type_name, labels, character
    
       
            


    