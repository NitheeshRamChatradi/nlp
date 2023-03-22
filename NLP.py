import spacy

def convert_to_full_month_name(text):
    doc = nlp(text)
    new_text = []
    for token in doc:
        if token.text in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
            if token.text == "Jan":
                new_text.append("January")
            elif token.text == "Feb":
                new_text.append("February")
            elif token.text == "Mar":
                new_text.append("March")
            elif token.text == "Apr":
                new_text.append("April")
            elif token.text == "May":
                new_text.append("May")
            elif token.text == "Jun":
                new_text.append("June")
            elif token.text == "Jul":
                new_text.append("July")
            elif token.text == "Aug":
                new_text.append("August")
            elif token.text == "Sep":
                new_text.append("September")
            elif token.text == "Oct":
                new_text.append("October")
            elif token.text == "Nov":
                new_text.append("November")
            elif token.text == "Dec":
                new_text.append("December")
        else:
            new_text.append(token.text)
    return " ".join(new_text)


def insert_spaces(s):
    result = []
    for i in range(len(s)):
        if s[i].isdigit() and (i == 0 or (not s[i-1].isdigit() and s[i-1] != ':')):
            result.append(" ")
        elif s[i].isalpha() and (i == 0 or s[i-1].isdigit()):
            result.append(" ")
        result.append(s[i])
    return "".join(result)

nlp = spacy.load("en_core_web_sm")
input_string = input("enter the string : ")#data in the excel which has to be seperated into diff colms is the input here
text1 = insert_spaces(input_string)
text = convert_to_full_month_name(text1)
print(text)
doc = nlp(text)
date = time = ""
for ent in doc.ents:
    # print(ent)
     if ent.label_ == "DATE":
        date = date + " " + ent.text
        if ent.label_ == "TIME":
            time = time + " " + ent.text
            #print(ent.label_)
print(f"Date: {date}")#should place this date in date column
print(f"Time: {time}")#place this in time column
