import json
import os


def resolve_CMeIE(path):
    res = []
    with open(path, 'r') as load_f:
        for line in load_f.readlines():
            load_dict = json.loads(line)
            res.append(load_dict)
    return res


def process_data(json_list):
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

        final_res.append({'doc_key': doc_id, 'sentences': sentences_list, 'ner': ner_list, 'relations': re_list})
        doc_id += 1

    return final_res


if __name__ == '__main__':
    preprocessed_path = './CMeIE/preprocessed'
    path_list = ['./CMeIE/CMeIE_train.json', './CMeIE/CMeIE_dev.json']
    for path in path_list:
        json_list = resolve_CMeIE(path)
        output = process_data(json_list)
        json_res = json.dumps(output, ensure_ascii=False)

        with open(os.path.join(preprocessed_path, path.split('/')[-1]), 'w') as f:
            f.write(json_res)
