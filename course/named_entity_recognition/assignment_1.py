import spacy


def main(): 
    nlp = spacy.load('en_core_web_sm')

    txt = "Apple reached an all-time high stock price of 143 dollars this January."

    doc = nlp(txt)

    org_list = []

    for entity in doc.ents:
        if entity.label_ == 'ORG':
            org_list.append(entity.text)

    print(org_list)


if __name__ == '__main__': 
    main()