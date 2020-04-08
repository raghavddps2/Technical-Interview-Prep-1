class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #check the group's immediate visible users

    users = group.get_users()
    if user in users:
        return True
    
    else:
        groups = group.get_groups()
        for group in groups:
            return is_user_in_group(user,group)
    return False


print("Test case 1")
empty_grp = Group("empty")
user = "user"
print(empty_grp.get_name(), "group has user?", is_user_in_group(user, empty_grp))

print("Test case 2")
grp = Group("test_grp")
user1 = "user1"
user2 = "user2"
user3 = "user3"
user4 = "user4"
grp.add_user(user1)
grp.add_user(user2)
grp.add_user(user3)
print(grp.get_name(), "group have user1?", is_user_in_group(user1, grp))
print(grp.get_name(), "group have user2?", is_user_in_group(user2, grp))
print(grp.get_name(), "group have user3?", is_user_in_group(user3, grp))
print(grp.get_name(), "group have user4?", is_user_in_group(user4, grp))

print("Test case 3")       
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user_a = "sub_child_user_a"
child.add_group(sub_child)
parent.add_group(child)
print(parent.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, parent))
print(child.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, child))
print(sub_child.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, sub_child))
print(parent.get_name(),"group has sub_child_user_a?",is_user_in_group(sub_child_user_a, parent))


'''
Test case 1
empty group has user? False
Test case 2
test_grp group have user1? True
test_grp group have user2? True
test_grp group have user3? True
test_grp group have user4? False
Test case 3
parent group has sub_child_user? True
child group has sub_child_user? True
subchild group has sub_child_user? True
parent group has sub_child_user_a? False

'''


