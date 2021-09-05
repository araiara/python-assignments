import argparse
import json
from datetime import datetime as dt

def check_date(date): 
    try:
        dt.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date value!")
    return date

def check_age(age):
    try:
        int(age)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid age value!")
    return age

parser = argparse.ArgumentParser()
parser.add_argument("name", help="name")
parser.add_argument("dob", help="date of birth in YYY-MM-DD", type=check_date)
parser.add_argument("age", help="age in integer", type=check_age)
parser.add_argument("hobbies", help="hobbies", nargs='+')

args = parser.parse_args()

user_data = {
    'name': args.name,
    'dob': args.dob,
    'age': args.age,
    'hobbies': args.hobbies
}

root_user_data = {
            "user_details": [
                user_data
            ]
        }

with open('user_data.json', 'r+') as file:  
    try:
        file_data = json.load(file)
        file_data["user_details"].append(user_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    except json.decoder.JSONDecodeError:
        json.dump(root_user_data, file, indent=4)
