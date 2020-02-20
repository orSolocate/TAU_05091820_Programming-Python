#####################################################
#           DO NOT DELETE THE NEXT 11 LINES         #
import time
from os.path import exists as path_ok
#Application gestures:
backup_succeeded = 'Data was backed up successfully to:\n'
backup_failed = 'Failed to backup you data. Please try again later.\n'
sending_succeeded_msg = 'Message was sent successfully!\n'
removing_succeeded_msg = 'Message was removed successfully!\n'
empty_conversation = 'Conversation either didn\'t start or all messages were removed.\n'
no_permissions_msg = 'Sorry! you are not a member of this conversation.\n'
no_such_msg = 'Message does not exist.\n'
thanks_msg = '\nThank you for using UpWhats! See you soon. Bye.\n'
#####################################################


class Date:
    
    def __init__(self, current_time):
        i=0
        hour=''
        minute=''
        second=''
        while current_time[i]!=',':
            hour+=current_time[i]
            i+=1
        i+=1
        while current_time[i]!=',':
            minute+=current_time[i]
            i+=1
        i+=1
        while i<len(current_time):
            second+=current_time[i]
            i+=1
        self.hour=hour
        self.minute=minute
        self.second=second
        return None        

    def __str__(self):
        return self.hour+":"+self.minute+":"+self.second


class Message:
    
    def __init__(self, sender, content, date, msg_id):
        self.sender=sender
        self.content=content
        self.date=date
        self.msg_id=msg_id
        return None
    
    def __len__(self):
        return len(self.content)
        
    def __str__(self):
        return "("+str(self.msg_id)+") "+str(self.date)+" "+self.sender+": "+self.content
        
    
class Conversation:
    
    def __init__(self, members, size_limit, backup_policy, cloud_account_prefix='./'):
        self.is_valid(members, size_limit, backup_policy, cloud_account_prefix)
        self.members=members
        self.size_limit=size_limit
        self.backup_policy=backup_policy
        cloud_account_prefix+=members[0] #group admin
        cloud_account_prefix+='.txt'
        self.cloud_account=cloud_account_prefix
        self.size=0
        self.total_messages_sent=0
        self.content=[]
        return None
        
    def __len__(self): #how many messages
        return len(self.content)

    def __str__(self):
        for i in range(0,len(self.content)):
            return "("+str(i+1)+")"+str(self.content[i])+"\n"
        
    def is_valid(self, members, size_limit, backup_policy, cloud_account_prefix):
        if (len(members)<2 or size_limit<=10 or backup_policy<1 or not(path_ok(cloud_account_prefix))):
            raise ValueError
        return None

    def is_member(self, username):
        return (username in self.members)
                                                                 
    def enough_space(self, msg): #enough space for this message
        return len(msg)+self.size<=self.size_limit 
                                                                 
    def is_empty(self): #empty-> no messages in the conversation
        return self.content==[]
            
    def time_for_backup(self):
        return (self.total_messages_sent%self.backup_policy==0)
        
    def backup_content(self):
        global backup_succeeded,backup_failed
        try:
            out=open(self.cloud_account,'w')
            out.write(self.get_conversation())
            print backup_succeeded+self.cloud_account
        except IOError:
            print backup_failed
        finally:
            if out is not None:
                out.close()
            return None
                                                                 
    def get_conversation(self):
        global empty_conversation
        if not self.is_empty():
            conversation=""
            for index in range(0,len(self.content)):
                conversation+=str(self.content[index])
                if index!=len(self.content)-1:
                    conversation+="\n"
            return conversation
        else:   return empty_conversation
        
    def send_msg(self, username, msg_content, msg_time):
        global sending_succeeded_msg
        msg_id=self.total_messages_sent+1
        msg=Message(username,msg_content,msg_time,msg_id)
        if not (self.enough_space(msg)): #not enough space for this message
            raise MemoryError
        else:
            self.total_messages_sent+=1
            self.content.append(msg)
            self.size+=len(msg)
            if self.time_for_backup():
                self.backup_content()
            return sending_succeeded_msg        
        
    def find_msg_index(self, msg_id):
        for index in range(0,len(self.content)):
            if self.content[index].msg_id==msg_id:
                           return index
        return -1
        
    def delete_msg(self, msg_id_str):
        global removing_succeeded_msg
        index=self.find_msg_index(int(msg_id_str))
        if index==-1: #id is not in the conversation
            raise ValueError
        else:
            deleted_msg=self.content.pop(index)
            self.size-=len(deleted_msg)
            return removing_succeeded_msg

                           
#####################################################
        
class Application:
    
    def __init__(self):
        '''
        Initializes the app. Think about it as an "installation".
        '''
        conversation_parameters = self.get_conversation_parameters_from_user()
        self.coversation = Conversation(*conversation_parameters)

        
    def get_conversation_parameters_from_user(self):
        '''
        Ask the user for parameters once as part of a conversation initialization.
        '''
        num_of_members = int(raw_input('Please enter the number of members in the group.\n'))
        members = []
        for i in range(num_of_members):
            members.append(raw_input('Please enter member number '+ str(i+1) +':\n'))
        size_limit = int(raw_input('Please enter your storage limit (int):\n'))
        backup_policy = int(raw_input('Please a desired backup policy (int):\n'))
        path = raw_input('Please enter a file path for backing up your data:\n')
        return members, size_limit, backup_policy, path.rstrip('/') + '/'
        
    def show_options(self):
        '''
        Prints the available options to the user. Nothing is returned.
        '''
        print '\n' + '#'*50 + '''\nWelcome to UpWhats! What would you like to do?
        [0] End conversation
        [1] Show full conversation
        [2] Send new message
        [3] Remove existing message\n'''
    
    
    def get_user_choice(self):
        '''
        Gets user's input for the expected operation and returns the choice number 
        if it is valid; -1 otherwise.
        '''    
        illegal_choice_msg = 'Choice is illegal. Please pick a number between 0 and 3'
        user_input = raw_input('Please type your choice and press ENTER\n')
        try:
            choice = int(user_input)
            if (0 <= choice <= 3):
                return choice
        except ValueError:
            print illegal_choice_msg
        return -1
            
    def run(self):
        '''
        Runs an "infinite" dialog loop and executes users requests. Nothing is 
        returned.
        '''
        global no_permissions_msg, no_such_msg, thanks_msg
        while True:
            time.sleep(1.5)
            self.show_options()
            choice = self.get_user_choice()
            if choice == -1:
                continue
            elif choice == 0:
                print thanks_msg
                break
            else:
                username = raw_input('Please enter username (only conversation\'s members are allowed to send/read messages).\n')
                if not self.coversation.is_member(username):
                    print no_permissions_msg
                    continue
                if choice == 1:
                    response = self.coversation.get_conversation()
                    print response
                elif choice == 2:
                    msg_content = raw_input('Please type your message.\n')
                    msg_time = Date(time.strftime('%H,%M,%S'))
                    response = self.coversation.send_msg(username, msg_content, msg_time)
                    print response
                elif choice == 3:
                    msg_id_str = raw_input('Please enter message id.\n')
                    try:
                        response = self.coversation.delete_msg(msg_id_str)
                    except ValueError:
                        response = no_such_msg
                    print response


########################################################
#     Optional: Paste the content of Tests.py below    #

########################################################

''' Main code. Do not change!'''
try:
    app = Application()
    app.run()
except ValueError:
    print '\nOne (or more) of the parameter values is illegal.'
    time.sleep(1)
    print '\nFailed to initialize the app.'
    time.sleep(1)
    print '\nExiting',
    for i in range(3):
        time.sleep(0.5)
        print '.',
    time.sleep(0.5)
    print '\n'

    
        
    
   
        
        
    
    
