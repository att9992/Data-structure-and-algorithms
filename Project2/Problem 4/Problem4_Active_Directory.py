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
        if user in group.get_users():
            return True
        else:
            if len(group.get_groups()) == 0:
                return False
            for gr in group.get_groups():
                boo = is_user_in_group(user,gr)
                if boo:
                    return True
        return False