sentence = raw_input("Sentence:")

screen_width=80
text_width=len(sentence)
box_width =text_width+6
left_magrin=(screen_width-box_width)//2

print
print ' '*left_magrin+'+' +'-'*(box_width-2)+'+'
print ' '*left_magrin+'!' +' '*(box_width-2)+'!'
print ' '*left_magrin+'! ' +        sentence+' '*3+'!'
print ' '*left_magrin+'!' +' '*(box_width-2)+'!'
print ' '*left_magrin+'+' +'-'*(box_width-2)+'+'
