import pyperclip

def split(string):
    return [char for char in string]

if __name__ == '__main__':

    inputstring = input("Enter string to convert: \n").lower()
    charlist = split(inputstring)
    index = 0
    for x in charlist:
        if x.isalpha():
            charlist[index] = ":regional_indicator_"+x+":"+" "
        index = index + 1
    pyperclip.copy(''.join(charlist))
    #print(''.join(charlist))
            
        
