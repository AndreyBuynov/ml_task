from deeppavlov import configs, build_model

ner_model = build_model(configs.ner.ner_ontonotes_bert_mult_torch, download=True)

def get_text(text):
    result = ner_model([text])
    stk = []; b = 0; bs = ''; ent_res = '';
    for i, ent in enumerate(result[1][0]):
        if ent[0] == 'B':
            if len(stk) > 0:
                ent_res += bs+':'+' '.join(stk)+'\n';
                b = 0; stk = [];
            stk.append(result[0][0][i])
            b = 1; bs = ent[2:];
        elif ent[0] == 'I':
            if ent[2:] == bs: stk.append(result[0][0][i])
            else:
                if len(stk) > 0:
                    ent_res += ent[2:]+':'+' '.join(stk)+'\n';
                    bs = ent[2:];
        elif ent[0] == 'O':
            if len(stk) > 0:
                ent_res += bs+':'+' '.join(stk)+'\n';
                b = 0; stk = []; bs = '';

    return ent_res # + '==' + ' '.join(result[1][0])
