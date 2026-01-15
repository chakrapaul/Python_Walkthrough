import random
import string

def encode_the_text(text_code):
    mod_code = ""
    if len(text_code)>=3:
        add_at_end = text_code[0]
        text_code+=add_at_end
        mod_code = text_code[1:]
    else:
        mod_code = text_code[::-1]
    
    random_char = string.ascii_letters+string.digits
    start_chars = ''.join(random.choices(random_char,k=3))
    end_chars = ''.join(random.choices(random_char,k=3))
    
    complete_modified_code = start_chars+mod_code+end_chars
    return complete_modified_code

def decode_code(code_to_decode):
    if len(code_to_decode)<3:
        return code_to_decode[::-1]
    else:
        dec_to_org = code_to_decode[3:-3]
        add_to_start = dec_to_org[-1]
        # print(add_to_start)
        original_string = add_to_start+dec_to_org
        return original_string[:-1]
        # return dec_to_org


text_code = input("Enter your text:")
code_to_decode = encode_the_text(text_code)
print("Code encoded is as follows:",code_to_decode)
original_code=decode_code(code_to_decode)
print("Your decoded code is:",original_code)

