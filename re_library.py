
'''

I'm gonna work with the re library. It has plenty of methods to work with regular expressions.
I won't use every single method of the library, but the most common ones, like search, split and sub
'''



import re


'''
The match method.
This will return a match object if the beggining of the string matches the regular expresion pattern.
The span you can see in the terminal corresponds to the indexes in the string.
In fact, this method checks for a match only at the beginning of the string.
'''
ejemplo_match1=re.match(r"is","This is an example: I love Python!!") 
print(ejemplo_match1)

ejemplo_match2=re.match(r"T","This is an example: I love Python!!")
print(ejemplo_match2)


'''
The search method.
This one will return a match if the regular expression pattern matches something in the string.
In fact, this method checks for a match anywhere in the string but returns just one match.
'''


ejemplo_search1=re.search(r"is","This is an example: I love Python!!")
print(ejemplo_search1)

'''
However, you may notice the "is" from the demostrative "this" was matched, but the finite verb was not matched.
We need to improve our pattern!
'''
ejemplo_search1=re.search(r"\sis","This is an example: I love Python!!")  #with the "\s" included in the pattern, we are specifing we look for an "is" preceeded by an empty space
print(ejemplo_search1)


ejemplo_search2=re.search(r"Python","This is an example: I love Python!!")
print(ejemplo_search2)

'''
The compile method can compile a regular expression pattern into a regular expession object. We can use it latter
with other methods just like match() or search()
'''

re_obj=re.compile(r"\bis\b")  #We introduce a regular expression pattern as argument
matching=re_obj.search("This is an example: I love Python!!")  #we use our object with the search method
print(matching)

#The fullmatch method will return a match object only if the pattern matches the whole string
re.fullmatch(r"This is an example: I love Python!!","This is an example: I love Python!!")

'''
The findall method is like a better version of the search method because it finds all the occurrences of the pattern
in the string. However, it will return a list containing all of the matches.
'''

findall_ex=re.findall(r"is","This is an example: I love Python!!")
print(findall_ex)

#Let's find all the "i"
findall_ex_2=re.findall(r"i","This is an example: I love Python!!")
print(findall_ex_2)


'''
The sub method replaces the leftmost non-overlapping occurrences of pattern in string by the replacement.
If the pattern isn’t found, string is returned unchanged.
'''

sub_ex=re.sub(r"Python","JavaScript","This is an example: I love Python!!")  #Note that "Javascript" is the repl
print(sub_ex)


#If we use subn instead, we will have a tuple with the newstring and the number of subs made.
re.subn(r"Python","JavaScript","This is an example: I love Python!!")

'''
The split method will split string by the occurrences of pattern and returns a list.
'''

split_list=re.split(r"\s","This is an example: I love Python!!")
print(split_list)

last_ex=re.findall(r"i","This is an example: I love Python!!",flags=re.I)
print(last_ex)
'''
You might have noticed the argument flags was specified previously.
The expression’s behaviour can be modified by specifying a flags value.
In our examples, whe use the re.I attribute to perform case-insensitive matching.
'''
