'''
     * In The Name Of God *
''' 
#              H
#             /|\
#            / | \
#           /--F--\
#          / \ | / \
#         *--- A ---*
#          \ / Z \ /
#           \  A  /
#            *-R-*
#             \ /
#          ====*=====
#          | HFAZAR |
#          ==========
'''
================================================
  Author         : HFAzar
  Project Title  : User Management System
  Class Session  : 09
  Level          : {level}
  Date           : 1405-07-10
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Task number 02: 

Description: User Management System
File Management · Functions · Strings · Conditions 
Design a user management application that stores data in a file named `users.txt`.

Data Structure:
1,Ali,ali@gmail.com,active
2,Sara,sara@gmail.com,blocked
3,Reza,reza@gmail.com,active

Required Functions:
1.	`add_user()` — Add a new user with an ID, name, email, and status.
2.	`find_user()` — Find a user based on their ID or name.
3.	`delete_user()` — Delete a user based on their ID.
4.	`update_user()` — Modify a user's email or status.
5.	`list_users()` — Display all users.
6.	`generate_report()` — Display the number of active users, blocked users, 
and the total number of users.
Rules: Each user's ID and email must be unique. Deletions or edits must be 
applied to the file itself, not just within the program's memory.
Bonus Challenge: Create an interactive menu using a `while` loop so that the 
program remains active until the user chooses to exit.
''' 
#%%

# ================================================
#   Task 2 — User Management System
# ================================================

# ---------- Helper Functions ----------

def load_users():
    users = []
    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                user = {
                    "id": int(parts[0]),
                    "name": parts[1],
                    "email": parts[2],
                    "status": parts[3],
                }
                users.append(user)
    except FileNotFoundError:
        return []
    return users


def save_users(users):
    with open("users.txt", "w") as f:
        for user in users:
            line = f"{user['id']},{user['name']},{user['email']},{user['status']}\n"
            f.write(line)


def id_exists(users, user_id):
    for u in users:
        if u["id"] == user_id:
            return True
    return False


def email_exists(users, email):
    for u in users:
        if u["email"].lower() == email.lower():
            return True
    return False


# ---------- Add User ----------

def add_user():
    users = load_users()
    
    try:
        user_id = int(input("شناسه (id): "))
    except ValueError:
        print("خطا: شناسه باید عدد باشد.")
        return

    if id_exists(users, user_id):
        print("خطا: این شناسه قبلاً ثبت شده است.")
        return

    name = input("نام: ").strip()
    email = input("ایمیل: ").strip()

    if email_exists(users, email):
        print("خطا: این ایمیل قبلاً ثبت شده است.")
        return

    status = input("وضعیت (active/blocked): ").strip().lower()
    if status not in ["active", "blocked"]:
        print("خطا: وضعیت باید active یا blocked باشد.")
        return

    users.append({
        "id": user_id,
        "name": name,
        "email": email,
        "status": status
    })
    save_users(users)
    print(f"کاربر {name} با موفقیت اضافه شد.")


# ---------- Find User ----------

def find_user():
    users = load_users()
    query = input("شناسه یا نام کاربر را وارد کنید: ").strip()
    
    found = False
    for u in users:
        # بررسی اینکه آیا ورودی با id (عدد) یا نام مطابقت دارد
        if str(u["id"]) == query or u["name"].lower() == query.lower():
            print(f"ID: {u['id']}, Name: {u['name']}, Email: {u['email']}, Status: {u['status']}")
            found = True
            
    if not found:
        print("کاربر پیدا نشد.")


# ---------- Delete User ----------

def delete_user():
    users = load_users()
    try:
        user_id = int(input("شناسه کاربر برای حذف: "))
    except ValueError:
        print("خطا: شناسه باید عدد باشد.")
        return

    new_users = [u for u in users if u["id"] != user_id]
    
    if len(new_users) == len(users):
        print("کاربر پیدا نشد.")
    else:
        save_users(new_users)
        print("کاربر با موفقیت حذف شد.")


# ---------- Update User ----------

def update_user():
    users = load_users()
    try:
        user_id = int(input("شناسه کاربر برای ویرایش: "))
    except ValueError:
        print("خطا: شناسه باید عدد باشد.")
        return

    for u in users:
        if u["id"] == user_id:
            print(f"کاربر پیدا شد: {u['name']}")
            new_email = input("ایمیل جدید (برای عدم تغییر Enter بزنید): ").strip()
            new_status = input("وضعیت جدید active/blocked (برای عدم تغییر Enter بزنید): ").strip().lower()

            if new_email:
                if email_exists(users, new_email) and new_email != u["email"]:
                    print("خطا: این ایمیل قبلاً ثبت شده است.")
                    return
                u["email"] = new_email

            if new_status:
                if new_status not in ["active", "blocked"]:
                    print("خطا: وضعیت نامعتبر است.")
                    return
                u["status"] = new_status

            save_users(users)
            print("اطلاعات کاربر با موفقیت ویرایش شد.")
            return

    print("کاربر پیدا نشد.")


# ---------- List Users ----------

def list_users():
    users = load_users()
    if not users:
        print("لیست کاربران خالی است.")
        return

    print("\n--- لیست کاربران ---")
    print(f"{'ID':<5} | {'Name':<15} | {'Email':<25} | {'Status'}")
    print("-" * 60)
    for u in users:
        print(f"{u['id']:<5} | {u['name']:<15} | {u['email']:<25} | {u['status']}")
    print()


# ---------- Report ----------

def generate_report():
    users = load_users()
    total = len(users)
    active = sum(1 for u in users if u["status"] == "active")
    blocked = sum(1 for u in users if u["status"] == "blocked")

    print("\n--- گزارش کاربران ---")
    print(f"تعداد کل کاربران: {total}")
    print(f"کاربران فعال: {active}")
    print(f"کاربران مسدود: {blocked}")


# ---------- Menu ----------

def main():
    while True:
        print("\n=== سیستم مدیریت کاربران ===")
        print("1. افزودن کاربر جدید")
        print("2. جستجوی کاربر")
        print("3. حذف کاربر")
        print("4. ویرایش کاربر")
        print("5. نمایش همه کاربران")
        print("6. گزارش آماری")
        print("0. خروج")
        
        choice = input("انتخاب کنید: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            find_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            list_users()
        elif choice == "6":
            generate_report()
        elif choice == "0":
            print("خروج از برنامه. خداحافظ!")
            break
        else:
            print("گزینه نامعتبر است. دوباره تلاش کنید.")


# ---------- Main ----------

if __name__ == "__main__":
    main()














