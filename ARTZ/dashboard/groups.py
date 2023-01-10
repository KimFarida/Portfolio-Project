from django.contrib.auth.models import User, Group
from .models import CustomGroup

# Get the group
mygroup = Group.objects.get(name='Custom Group')

# Get all users in the group
users = User.objects.filter(groups__name='Custom Group')

# Print the username of each user
for user in users:
    print(user.username)
