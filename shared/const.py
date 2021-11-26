task_ner_labels = {
    'ace04': ['FAC', 'WEA', 'LOC', 'VEH', 'GPE', 'ORG', 'PER'],
    'ace05': ['FAC', 'WEA', 'LOC', 'VEH', 'GPE', 'ORG', 'PER'],
    'scierc': ['Method', 'OtherScientificTerm', 'Task', 'Generic', 'Material', 'Metric'],
    'emr': ['DISEASE', 'POSITION', 'DRUG', 'DELIVER_METHOD', 'EFFICACY', 'INDICATION', 'SURGERY', 'SYMPTOM', 'RIS',
            'LIS', 'LIS_ITEMS', 'ITEM_VALUE', 'ITEM_UNIT', 'REMARK', 'THERAPY', 'GENERAL_STATUS',
            'GENERAL_STATUS_RESULT',
            'VITAL_SIGN', 'VALUE', 'PE_ITEMS', 'PE_RESULT'],
    'cmeie': ['疾病', '其他', '其他治疗', '检查', '手术治疗', '其他治疗', '流行病学', '症状', '社会学', '药物', '部位', '预后']
}

task_rel_labels = {
    'ace04': ['PER-SOC', 'OTHER-AFF', 'ART', 'GPE-AFF', 'EMP-ORG', 'PHYS'],
    'ace05': ['ART', 'ORG-AFF', 'GEN-AFF', 'PHYS', 'PER-SOC', 'PART-WHOLE'],
    'scierc': ['PART-OF', 'USED-FOR', 'FEATURE-OF', 'CONJUNCTION', 'EVALUATE-FOR', 'HYPONYM-OF', 'COMPARE'],
    'emr': ['DIS-POS', 'DRU-DE', 'DRU-EFF', 'DRU-INDI', 'SUR-POS', 'SUR-DIS', 'SYM-POS', 'RIS-POS', 'LI-LIS', 'LI-VAL',
            'LI-UNIT', 'LI-RMK', 'GS-RES', 'VS-VAL', 'VS-UNIT', 'PE-RES', 'PE-POS']
    'cmeie': ['预防', '阶段', '就诊科室', '辅助治疗', '化疗', '放射治疗', '手术治疗', '实验室检查', '影像学检查', '辅助检查', '组织学检查',
              '内窥镜检查', '筛查', '多发群体', '发病率', '发病年龄', '多发地区', '发病性别倾向', '死亡率', '传播途径', '多发季节',
              '并发症', '病理分型', '相关（导致）', '鉴别诊断', '相关（转化）', '相关（症状）', '临床表现', '治疗后症状', '侵及周围组织转移的症状',
              '病因', '高危因素', '风险评估因素', '病史', '遗传因素', '发病机制', '病理生理', '药物治疗', '发病部位', '转移部位',
              '外侵部位', '预后状况', '预后生存率', '同义词']
}


def get_labelmap(label_list):
    label2id = {}
    id2label = {}
    for i, label in enumerate(label_list):
        label2id[label] = i + 1
        id2label[i + 1] = label
    return label2id, id2label
