"""
zip method takes 2 or more same type of arguments and zip them together. It will zip such a way that ,
for each zip it will pick first elements from each and combine them to make a tuple, then 2nd element
from all and so on.
"""

name_list = ["Scott", "Peter", "Tony", "Steve"]
character_list = ["Ant man", "Spider man", "Iron man", "Captain America"]
movies = [2016, 2011, 2007, 2006]
final_result = list(zip(name_list, character_list, movies))
print(final_result)
