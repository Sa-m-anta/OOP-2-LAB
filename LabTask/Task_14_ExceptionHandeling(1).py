class InvalidVoterException(Exception):
    """Custom exception for invalid voter age."""
    def init(self, age, message="Age must be 18 or older to vote."):
        self.age = age
        self.message = message
        super().init(self.message)

def check_voter_age(age):
    if age < 18:
        raise InvalidVoterException(age)
    else:
        print("You are eligible to vote.")

try:
    age = int(input("Enter your age: "))
    check_voter_age(age)
except InvalidVoterException as e:
    print(f"InvalidVoterException: {e.message} (Age entered: {e.age})")
except ValueError:
    print("Please enter a valid number for age.")