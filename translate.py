import pandas as pd
import re
from tqdm import tqdm, trange
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tr_tokenizer = AutoTokenizer.from_pretrained("QuoQA-NLP/KE-T5-En2Ko-Base")
tr_model = AutoModelForSeq2SeqLM.from_pretrained("QuoQA-NLP/KE-T5-En2Ko-Base")

def get_translate(sent):
    sent = tr_model.generate(
        **tr_tokenizer(sent, return_tensors="pt", padding=True, max_length=77),
        max_length=77,
        num_beams=5,
        repetition_penalty=1.3,
        no_repeat_ngram_size=3,
        num_return_sequences=1
    )
    sent = tr_tokenizer.decode(sent[0], skip_special_tokens=True)
    return sent
    


if __name__=="__main__":
    with open('D:/SKTAI/Kaggle Fairytale/merged_clean.txt', mode='r', encoding='utf-8') as f:
        text = f.read()

    c_list = [i.replace('\n', ' ') for i in re.split("\n\n", text)]
    c_result_list = []
    
    print(get_translate('''Twas not long till we saw, westwards, a fleet rider advancing towards us, a young maiden of most beautiful appearance, on a slender white steed of swiftest power. We all ceased from the chase on seeing the form of the royal maid; 'twas a surprise to Fionn and the Fianns, they never beheld a woman equal in beauty. A royal crown was on her head, and a brown mantle of precious silk, spangled with stars of red gold, covering her shoes down to the grass. A gold ring was hanging down from each yellow curl of her golden hair; her eyes were blue, clear, and cloudless, like a dewdrop on the top of the grass. Redder were her cheeks than the rose, fairer was her visage than the swan upon the wave, and more sweet was the taste of her balsam lips than honey mingled through red wine. A garment, wide, long, and smooth, covered the white steed; there was a comely saddle of red gold, and her right hand held a bridle with a golden bit. Four shoes, well shaped, were under him, of the yellow gold of the purest quality; a silver wreath was on the back of his head, and there was not in the world a steed better.	'''))
    quit()
    for n, sent in enumerate(tqdm(c_list[35231:35232])):
        result = get_translate(sent)
        c_result_list.append(result)
        print(sent, result, sep='\n')
        
    df = pd.DataFrame(zip(c_list[35231:35232], c_result_list), columns=('en', 'ko'))
    df.to_csv('D:/SKTAI/Kaggle Fairytale/merged_clean_p2_2.tsv', encoding='utf-8', sep='\t')