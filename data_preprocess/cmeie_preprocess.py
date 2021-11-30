import json
import os

import matplotlib.pyplot as plt

def resolve_CMeIE(path):
    res = []
    with open(path, 'r') as load_f:
        for line in load_f.readlines():
            load_dict = json.loads(line)
            res.append(load_dict)
    return res


def process_data(json_list):
    len_stat = {}
    doc_id = 0
    final_res = []
    for line in json_list:
        text = line['text']
        sentences_list = []
        ner_list = []
        re_list = []
        sentences_list.append([w for w in text])
        # ner & re
        for pair_dict in line['spo_list']:
            sub = pair_dict['subject']
            obj = pair_dict['object']['@value']
            sub_start_index = text.find(sub)
            sub_end_index = sub_start_index + len(sub) - 1
            obj_start_index = text.find(obj)
            obj_end_index = obj_start_index + len(obj) - 1
            subject_type = pair_dict['subject_type']
            object_type = pair_dict['object_type']['@value']
            predicate = pair_dict['predicate']

            ner_list.append([sub_start_index, sub_end_index, subject_type])
            ner_list.append([obj_start_index, obj_end_index, object_type])

            re_list.append([sub_start_index, sub_end_index, obj_start_index, obj_end_index, predicate])

            if len(sub) not in len_stat:
                len_stat[len(sub)] = 1
            else:
                len_stat[len(sub)] += 1
            if len(obj) not in len_stat:
                len_stat[len(obj)] = 1
            else:
                len_stat[len(obj)] += 1

        big_ner_list = [ner_list]
        big_re_list = [re_list]
        final_res.append({'doc_key': doc_id, 'sentences': sentences_list, 'ner': big_ner_list, 'relations': big_re_list})
        doc_id += 1

    return final_res, len_stat


if __name__ == '__main__':
    preprocessed_path = './CMeIE/preprocessed'
    path_list = ['./CMeIE/CMeIE_train.json'] #, './CMeIE/CMeIE_dev.json']
    for path in path_list:
        json_list = resolve_CMeIE(path)
        output = process_data(json_list)
        stat_dict = output[1]
        stat_dict = sorted(stat_dict.items(), key=lambda x:x[0])
        # print(stat_dict)
        x, y = [], []
        for d in stat_dict:
            x.append(d[0])
            y.append(d[1])
        plt.bar(x, y, align='center')
        plt.title('CMeIE span length - frequency')
        plt.xlabel('span length')
        plt.ylabel('frequency')
        plt.show()

        # with open(os.path.join(preprocessed_path, path.split('/')[-1]), 'w') as f:
        #     for line in tqdm(output[0]):
        #         json_res = json.dumps(line, ensure_ascii=False)
        #         f.write(json_res)
        #         f.write('\n')

