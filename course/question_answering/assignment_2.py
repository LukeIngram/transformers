import json
import os

squad_dir = 'data\squad'

with open(os.path.join(squad_dir, 'dev-v2.0.json'), 'rb') as f:
    squad = json.load(f)

new_squad = []


for group in squad['data']:
    for paragraph in group['paragraphs']:
        context = paragraph['context']
        for qa_pair in paragraph['qas']:
            question = qa_pair['question']
            if 'answers' in qa_pair.keys() and len(qa_pair['answers']) > 0:
                answer_list = qa_pair['answers']
            elif 'plausible_answers' in qa_pair.keys() and len(qa_pair['plausible_answers']) > 0:
                answer_list = qa_pair['plausible_answers']
            else:
                answer_list = []
            answer_list = [item['text'] for item in answer_list]
            answer_list = list(set(answer_list))
            for answer in answer_list:
                new_squad.append({
                    'question': question,
                    'answer': answer,
                    'context': context
                })

#Check 
print(new_squad[:3], new_squad[-2:])