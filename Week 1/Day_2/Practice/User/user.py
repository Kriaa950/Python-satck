class user:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_cards_points = 0 
# function to display info
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Reward memeber: {self.is_rewards_member}")
        print(f"Gold card member: {self.gold_cards_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
        return False
    def spend_points(self, amount):
        if self.gold_cards_points >= amount:
            self.gold_cards_points -= amount# dedcut points
        else:
            print("is not enough point to spend.")
            return True
# create user insatance 
user1 = user("Abdallah", "Kriaa", "abdallahkriaa@gmail.com", 21)
user1.display_info() # display user info 

user1.enroll()
user1.spend_points(50)
user1.display_info()

user2 = user("Yessine", "Kriaa", "yessinekriaa@gmail.com", 21)
user3 = user("Ali", "sassi", "Alisassi@gmail.com", 22)

user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()
user3.display_info()