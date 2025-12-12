import random
import string
import turtle

def gen_name():
        
        f_name = ["Aarush", "Anika", "Advait", "Bhavya", "Ishan", "Janhavi", "Kabir", "Latika", "Manav", "Myra", "Neel", "Kavya", "Pranav", "Priya", "Raghav", "Ruhi", "Samar", "Siya", "Tanay", "Tanya", "Vihaan", "Vanshika", "Dhruv", "Diya", "Krish", "Kiara", "Nakul", "Neha", "Om", "Pari", "Reyansh", "Riya", "Rohan", "Sara", "Aryan", "Anvi", "Yash", "Zoya", "Kunal", "Sneha", "Abhay", "Akshara", "Laksh", "Jia", "Jai", "Ira", "Gautam", "Eesha", "Dev", "Aashi", "Aiden", "Sophia", "Liam", "Emma", "Noah", "Olivia", "Lucas", "Ava", "Mason", "Mia", "Ethan", "Harper", "Elijah", "Amelia", "James", "Evelyn", "Benjamin", "Abigail", "Jacob", "Charlotte", "Michael", "Emily", "Daniel", "Elizabeth", "Alexander", "Sofia", "Henry", "Grace", "Sebastian", "Chloe", "Matthew", "Scarlett", "Jackson", "Lily", "Samuel", "Zoey", "David", "Layla", "Carter", "Ella", "Luke", "Hannah", "Wyatt", "Victoria", "Julian", "Penelope", "Isaac", "Ellie", "John", "Nora", "Asher", "Aubrey", "Leo", "Mila"]
        l_name = ["Sharma", "Patel", "Singh", "Gupta", "Shah", "Kumar", "Khan", "Desai", "Jain", "Reddy", "Verma", "Malhotra", "Joshi", "Singh", "Rao", "Mehta", "Bansal", "Bose", "Narayan", "Menon", "Sharma", "Choudhary", "Agarwal", "Kumar", "Kapoor", "Khanna", "Das", "Yadav", "Kulkarni", "Bhatt", "Sharma", "Singh", "Gupta", "Ali", "Chopra", "Desai", "Patel", "Khan", "Reddy", "Kumari", "Singh", "Iyer", "Pillai", "Gupta", "Varma", "Dutta", "Singh", "Nair", "Kumar", "Banerjee", "Smith", "Johnson", "Miller", "Williams", "Brown", "Jones", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Hernandez", "Lopez", "Gonzalez", "Davis", "Perez", "Thomas", "Taylor", "Moore", "Jackson", "White", "Harris", "Scott", "Hall", "Wright", "King", "Clark", "Lee", "Walker", "Young", "Lewis", "Allen", "Green", "Baker", "Hill", "Adams", "Nelson", "Carter", "Mitchell", "Roberts", "Evans", "Phillips", "Turner", "Collins", "Stewart", "Bell", "Foster", "Morgan", "Reed", "Cooper"]
        
        return random.choice(f_name) + " " + random.choice(l_name)

def gen_mail(name):
    
    domain = ["email.com", "outlook.com", "hotmail.com", "yahoo.com"]
    username = name.lower().replace(" ", "") + str(random.randint(10, 9999))
    return f"{username}@{random.choice(domain)}"

def gen_pass(min_len =6, max_len= 20):
    
    length = random.randint(min_len, max_len)
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# def gen_phonenum(max_len = 10):
#     num = random.randint(70000000000,9999999999)
#     return num

def gen_entries(n):
    ent = []
    for _ in range(n):
        name = gen_name()
        e_mail = gen_mail(name) 
        pas = gen_pass()
        # num = gen_phonenum()
        ent.append({"Name":name, "E-Mail":e_mail, "Password":pas})
    return ent


# if __name__ == "__main__":
#     num_ent = int(input("How many entries do you want to generate? "))
#     data = gen_entries(num_ent)   
    
#     for i, entry in enumerate(data, start=1):
#         print(f"\nEntry {i}")
#         print(f"Name: {entry['Name']}")
#         print(f"Email: {entry['E-Mail']}")
#         print(f"Password: {entry['Password']}") 
        
        
    