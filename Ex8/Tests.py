'''
The next code block executes several tests of common scenarios for your aid. 
You are more than welcome to add tests of your own, but it's not mandatory.
'''
#Assert statement throws an error if the expression after it evaluates to False
d = Date('h,m,s')
assert d.hour=='h'
assert d.minute=='m'
assert d.second=='s'
assert str(d)=='h:m:s'
members = ('a', 'b', 'c')
m=Message(members[0], 'bla', d, 17)
assert len(m)==3
assert str(m)=='(17) ' + str(d) + ' a: bla' 
c=Conversation(members, 20, 3)
assert c.enough_space('$'*c.size_limit)    
assert not c.enough_space('$'*(c.size_limit+1))    
assert not c.is_member('non-existing member')
assert c.is_member('a')
assert c.is_member('c')
assert c.is_empty()
try:
    c.delete_msg(170)
    assert False
except ValueError:
    pass
assert c.get_conversation() == empty_conversation
try:
    c.send_msg(members[0], '$'*(c.size_limit+1), d)
    assert False
except MemoryError:
    pass
assert c.send_msg(members[0], '$'*(c.size_limit-1), d) == sending_succeeded_msg
assert c.find_msg_index(1) == 0
assert not c.is_empty()

assert sum([len(x) for x in c.content]) == c.size_limit-1
try:
    c.send_msg(members[0], '$$', d)
    assert False
except MemoryError:
    pass
assert sum([len(x) for x in c.content]) == c.size_limit-1

try:
    c.delete_msg(0)
    assert False
except ValueError:
    pass

tmp = c.total_messages_sent
assert c.delete_msg(tmp) == removing_succeeded_msg
try:
    c.delete_msg(1)
    assert False
except ValueError:
    pass

assert c.total_messages_sent == tmp
assert c.find_msg_index(0) == -1

assert c.is_empty()
assert sum([len(x) for x in c.content]) == 0
assert c.send_msg(members[0], 'Hi', d) == sending_succeeded_msg
assert c.send_msg(members[1], 'Bye', d) == sending_succeeded_msg
assert c.get_conversation() == '(2) h:m:s a: Hi\n(3) h:m:s b: Bye'
f = open('./'+members[0]+'.txt')
assert f.read() == '(2) h:m:s a: Hi\n(3) h:m:s b: Bye'
f.close()
assert c.size == 5
print '\nCongrats!!! All preliminary tests passed!\n'