import re

string_content = '{"records":[,{"Id":1, "name":"Taslim", "rec_name": "DRDO[,"}, {"Id":2, "name":"Arif[,", "rec_name": ' \
                 '"Test[],,"}]}'
# pattern = re.compile(r'.')  # Find all characters except \n
# pattern = re.compile(r'^{')  # check whether string starts with provided character and return match object if true
# pattern = re.compile(r'}$')  # check whether string ends with provided character and return match object if true
# pattern = re.compile(r'}/z*')  # Return 0 or more occurrences of specified character
# pattern = re.compile(r'}+')  # Return 1 or more occurrences of specified character
pattern = re.compile(r'(\[,){1}')  # Return specified occurrences of specified character
matches = pattern.finditer(string_content)
# print(matches)
for match in matches:
    print(match)
