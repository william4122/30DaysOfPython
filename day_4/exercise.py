#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty='Thirty'
space=' '
days='Days'
of='Of'
python='Python'
together= thirty + space + days + space + of + space + python
print(together)
#correct, don't do commas, concantenation is string addition so +++++++++++++

#2. Concantenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.
coding='Coding'
space=' '
wfor='For' #cant use for as a var name
all='All'
together_string=coding + space + wfor + space + all
print(together_string)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company='Coding For All'

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
silver_crystal='sailor moon fights crimosn rubeus'
print(silver_crystal.upper())

#7. Change all the characters to lowercase letters using lower() method.
dark_phantom='I AM DEATH PHANTOM RULER OF THE UNIVERSE'
print(dark_phantom.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
coding_for_all='Coding For All'
print(coding_for_all.capitalize())
print(coding_for_all.title())
print(coding_for_all.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
coding_for_all='Coding For All'
sliced=coding_for_all[7:]
print(sliced) 

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding_for_all='Coding For All'
print(coding_for_all.index('For'))

#11. Replace the word coding in the string 'Coding For All' to Python.
coding_string='Coding For All'
python_for_all=coding_string.replace('Coding','Python')
print(python_for_all)

#12.Change Python for Everyone to Python for All using the replace method or other methods.
python_for_everyone='Python For Everyone'
python_for_all=python_for_everyone.replace('Everyone', 'All')
print(python_for_all)

#13. Split the string 'Coding For All' using space as the separator (split()) .
coding_for_all='Coding For All'
split_coding_for_all=coding_for_all.split() #will use the default
print(split_coding_for_all)

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(big_tech.split(','))

#15. What is the character at index 0 in the string Coding For All.
coding_for_all='Coding For All'
index_zero=coding_for_all[0]
print(index_zero)

#16. What is the last index of the string Coding For All.
coding_for_all='Coding For All'
index_last=coding_for_all[-1]
print(index_last)

#17. What character is at index 10 in "Coding For All" string.
coding_for_all='Coding For All'
index_ten=coding_for_all[10]
print(index_ten)

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
##wtf
python_for_everyone='Python For Everyone'
pfo = python_for_everyone[0:3:4]
print(pfo)
#P

#19.Create an acronym or an abbreviation for the name 'Coding For All'.
#is this optimal? if it is this is the answer for 17
coder='Coding For All'
c=coder[0]
f=coder[7]
a=coder[11]
print(c,f,a)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
coding_for_all='coding for all'
index_c=coding_for_all.index('c')
print(index_c)

#21. Use index to determine the position of the first occurrence of F in Coding For All.
coding_for_all='coding for all'
index_f=coding_for_all.index('f')
print(index_f)

#22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
coding_for_all_people='Coding For All People'
last_i=coding_for_all_people.rfind('i')
print(last_i)

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
because_index=sentence.index('because')
print(because_index)
because_find=sentence.find('because')
print(because_find)

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
last_because=sentence.rindex('because')
print(last_because)

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
sliced_with=sentence[0:31]
sliced_end=sentence[55:71]
no_because=sliced_with + sliced_end
print(no_because)


#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
first_because=sentence.find('because')
print(first_because)

#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
