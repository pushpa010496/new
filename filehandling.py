
import os

# f = open('demofile3.txt','a')
# # print(f.read())
# f.write('On the other hand, when you add someone to the BCC field, it means that you are sending them a copy of the message without the primary recipient(s) being aware of it. The BCC field is typically used when you want to send a copy of the message to someone without the other recipients knowing about it. This can be useful for keeping someone in the loop without creating unnecessary email threads or for sending a message to a large group of people without revealing everyone email address.')
# f.close()


# f= open('demofile3.txt','rt')
# print(f.readline())

# os.remove('demofile2.txt')
if os.path.exists('demofile2.txt'):
    os.remove('demofile2.txt')
else:
    print('the file dose not exists')


os.rmdir('new')