import json
import numpy as np


test_keys = ['test', 'Test']
keys = ['assert', 'Assert']

assert_num = 0
max_assert_num = 0
total_test_num = 0
total_method_num = 0
focal_method_lengths = []
retrvied_method_lengths = []
test_lengths = []
with open('/Users/yangchen/Desktop/CodeLlama-7b-Instruct-hf_comment_extend_full.jsonl', 'r') as fr:
    for line in fr:
        content = json.loads(line)
        is_public = content['is_public']
        tests = content['few_shot_test'].split('\n\n')
        retrvied_methods = content['few_shot_method']
        
        focal_method = content['focal_method']
        
        if is_public == "0":
            continue
        
        flag = False
            
        for t in tests:
            single_ass = 0
            if any(k in t.split('\n')[0] for k in test_keys):
                total_test_num += 1
                flag = True
                lines_in_test = t.split('\n')
                for l in lines_in_test:
                    if any(k in l for k in keys): 
                        assert_num += 1
                        single_ass += 1
                if single_ass>max_assert_num:
                    max_assert_num =  single_ass
                test_lengths.append(len(t.split('\n')))
        if flag:
            total_method_num += 1
            focal_method_lengths.append(len(focal_method.split('\n')))
            retrvied_method_lengths.append(len(retrvied_methods.split('\n')))

print("Total test number: ", total_test_num)
print("Total method number: ", total_method_num)
print("Average assert number per test: ", assert_num/total_test_num)
print("Average test number per method: ", total_test_num/total_method_num)
print('Max ', max_assert_num)

print('Average length of focal ', np.mean(focal_method_lengths))

print('Average length of example ', np.mean(retrvied_method_lengths))
print('Average retrived test length', np.mean(test_lengths))
