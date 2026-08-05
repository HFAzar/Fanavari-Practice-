# STR Functions Practice "Total Functions"

'''
Python String Methods;

Method              	Description

-capitalize()	 Converts the first character to upper case
-casefold()	     Converts string into lower case
-center()	     Returns a centered string
-count()	     Returns the number of times a specified value occurs in a string
-encode()	     Returns an encoded version of the string
-endswith()      Returns true if the string ends with the specified value
-expandtabs()    Sets the tab size of the string
-find()	         Searches the string for a specified value and returns the position of where it was found
-format()	     Formats specified values in a string
-format_map()	 Formats specified values from a dictionary in a string
-index()	     Searches the string for a specified value and returns the position of where it was found
-isalnum()	     Returns True if all characters in the string are alphanumeric
-isalpha()	     Returns True if all characters in the string are in the alphabet
-isascii()	     Returns True if all characters in the string are ascii characters
-isdecimal()   	 Returns True if all characters in the string are decimals
-isdigit()	     Returns True if all characters in the string are digits
-isidentifier()	 Returns True if the string is an identifier
-islower()	     Returns True if all characters in the string are lower case
-isnumeric()	 Returns True if all characters in the string are numeric
-isprintable()	 Returns True if all characters in the string are printable
-isspace()	     Returns True if all characters in the string are whitespaces
-istitle()	     Returns True if the string follows the rules of a title
-isupper()	     Returns True if all characters in the string are upper case
-join()	         Converts the elements of an iterable into a string
-ljust()	     Returns a left justified version of the string
-lower()	     Converts a string into lower case
-lstrip()	     Returns a left trim version of the string
-maketrans()	 Returns a translation table to be used in translations
-partition()	 Returns a tuple where the string is parted into three parts
-replace()	     Returns a string where a specified value is replaced with a specified value
-rfind()	     Searches the string for a specified value and returns the last position of where it was found
-rindex()	     Searches the string for a specified value and returns the last position of where it was found
-rjust()	     Returns a right justified version of the string
-rpartition()	 Returns a tuple where the string is parted into three parts
-rsplit()	     Splits the string at the specified separator, and returns a list
-rstrip()	     Returns a right trim version of the string
-split()	     Splits the string at the specified separator, and returns a list
-splitlines() 	 Splits the string at line breaks and returns a list
-startswith()	 Returns true if the string starts with the specified value
-strip()	     Returns a trimmed version of the string
-swapcase()	     Swaps cases, lower case becomes upper case and vice versa
-title()	     Converts the first character of each word to upper case
-translate()	 Returns a translated string
-upper()	     Converts a string into upper case
-zfill()	     Fills the string with a specified number of 0 values at the beginning
      
'''





#capitalize()   Example:
a="hassan fatemi azar"
print(a.capitalize())


#casefold()    Example:
b='HASSAN FATEMI AZAR' 
print(b.casefold()) 
   
#center()    Example:
c="hassan fatemi azar"
print(c.center(33,"$"))


#count()    Example:
d="hassan fatemi azar"
print(d.count("a"))

#encode()    Example:
d="hassan fatemi azar"
print(d.encode())

#endswith()    Example:
e="hassan fatemi azar.text"
print(e.endswith(".text"))  


#expandtabs()    Example:
f="my\t name\t is\t hassan\t fatemi\t azar"
print(f.expandtabs(7))


#find()	    Example:
g="hassan fatemi azar"
print(g.find("azar"))


#format()	    Example:
h="im {}  {}  {}"
print(h.format("hassan","fatemi","azar"))


#format_map()	    Example:
data={"name":"hassan","age":33}
i="my name is {name} & im {age} years old"
print(i.format_map(data))

#index()	    Example:
j="i am a python student"
print(j.index("python"))

#isalnum()	    Example:
k="hassanlxxii72"
print(k.isalnum())


#isalpha()	    Example:
l="hassanlxxii72"
print(l.isalpha())


#isascii()	    Example:
m="حسن fatedmi azar 72 *"
print(m.isascii())


#isdecimal()	    Example:
n="1234567890"
print(n.isdecimal())


#isdigit()	    Example:
o="3372911^13"
print(o.isdigit())


#isidentifier()	    Example:
p="my_name_is_hassan_im_33"
print(p.isidentifier())


#islower()	    Example:
q="hassan fatemi azar"
print(q.islower())


#isnumeric()	    Example:
r="7½"
print(r.isnumeric())


#isprintable()	    Example:
s="hassan Fatemi Azar student of fanavari co.13.33.72."
print(s.isprintable())

#isspace()	    Example:
t="fanavari co."
u="     "
print(t.isspace())
print(u.isspace())


#istitle()	    Example:
v="hassan Fatemi azar"
w="Hassan Fatemi Azar"
print(v.istitle())
print(w.istitle())


#isupper()	    Example:
x="HASSAN FATEMI AZAR"
print(x.isupper())


#join()	    Example:
y=["Hassan","Fatemi","Azar"]
print("_".join(y))


#ljust()	    Example:
z="fanavari"
print(z.ljust(33,"_"))



#lower()	    Example:
aa="hassan FATEMI Azar 2585"
print(aa.lower())


#lstrip()	    Example:
ab="       Hassan Fatemi azar       "
print(ab.lstrip())


#maketrans()	    Example:
ac=str.maketrans("abcdefghi","123456789")
ad="hassan fatemi azar"
print(ad.translate(ac))


#partition()	    Example:
ae="hassan fatemi azar"
print(ae.partition("aril"))
print(ae.partition("azar"))


#replace()	    Example:
af="hassan fatemi azar"
print(af.replace("hassan","iran"))


#rfind()	    Example:
ag="hassan  azar fatemi azar"
print(ag.rfind("azar"))


#rindex()	    Example:
ah="hassan  azar   fatemi   azar"
print(ah.rindex("azar"))



#rjust()	    Example:
ai="hassan fatemi azar"
print(ai.rjust(33,"*"))


#rpartition()	    Example:
aj="hassan fatemi azar"
print(aj.rpartition("azar"))
 


#rsplit()	    Example:
ak="hassan fatemi azar"
print(ak.rsplit(" ",2))



#rstrip()	    Example:
al="       Hassan Fatemi azar       "
print(al.rstrip())



#split()	    Example:
am="hassan,fatemi,azar,tehran,iran"
print(am.split())
print(am.split(","))


#splitlines()	    Example:
an="hassan\n fatemi\n azar\n tehran\n"
print(an.splitlines())


#startswith()	    Example:
ao="hassan fatemi azar"
print(ao.startswith("hassan"))
print(ao.startswith("azar"))



#strip()	    Example:
ap="   Hassan Fatemi Azar   "
print(ap.strip())



#swapcase()	    Example:
aq="Hassan Fatemi Azar"
print(aq.swapcase())



#title()	    Example:
ar="hassan fatemi azar"
print(ar.title())


#translate()	    Example:
as1=str.maketrans("abcdefghi", "123456789")
as2="hassan fatemi azar"
print(as2.translate(as1))



#upper()	    Example:
at="hassan fatemi azar 2585 lxxii"
print(at.upper())


#zfill()	    Example:
au="72" 
print(au.zfill(13))



  
#THE END .... Yours Sincerely .... HFAzar.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

