class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "Pikachu")
user_2 = User("002", "Greninja")

print(f"User 1 Following: {user_1.following}")
print(f"User 1 Followers: {user_1.followers}")

user_1.follow(user_2)
print(f"User 1 Following: {user_1.following}")
print(f"User 1 Followers: {user_1.followers}")
print(f"User 2 Following: {user_2.following}")
print(f"User 2 Followers: {user_2.followers}")
