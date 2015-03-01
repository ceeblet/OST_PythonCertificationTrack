"""
 a function that substitutes X for all but the last four digits of any credit card 
 numbers in a string, returning the updated string as its result
 """
 
import re

def redact_cc(text):
    cc_pattern = r'(\d){4}-(\d){4}-(\d){4}'
    return re.sub(cc_pattern, "XXXX-XXXX-XXXX", text)