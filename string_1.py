1
def hello_name(name):
    return "Hello " + name + "!"
    
print(hello_name('bob'))

2
def make_abba(a,b):
    return a + b + b + a

print(make_abba('hi', 'bye'))


3
def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'
    
print(make_tags('i', 'Yay'))


4
def make_out_word(out,word):
    return out[:2]+word+out[2:]

print(make_out_word('<<>>', 'Yay'))


5
def extra_end(str):
    return str[-2:]*3

print(extra_end('Hello'))


6
def first_two(str):
    return str[:2] if len(str)>2 else str

print(first_two('Hello'))


7
def first_half(str):
    return str[:int(len(str) / 2)]


print(first_half('WooHoo'))


8
def without_end(str):
    return str[1:-1]
    
print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))


9
def combo_string(a,b):
    long = a if len(a)>len(b) else b
    short = a if len(a)<len(b) else b
    return short + long + short
    
def combo_string(a,b):
    return (a if len(a)<len(b) else b) + (a if len(a)>len(b) else b) + (a if len(a)<len(b) else b)

    
print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print


10
def non_start(a,b):
    return a[1:] + b[1:]
    
print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))


11
def left2(str):
    return str[2:] + str[:2]
    
print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))