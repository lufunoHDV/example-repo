# --- OOP Email Simulator --- #

# initialising inbox to access email objects
inbox = []


# Creating email class
class Email:
    # Constructor method
    def __init__(self, email_address, subject_line, email_content):
        """
        initialising the instance variables

        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """
        implementing an instance method to set has_been_read to true
        """
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    """
    this function creates an email object using the example emails
    and extends it into the inbox
    """
    example_emails = [Email("school@gmail.com", "Marks are out", "Goodday Lufuno, your marks are ready for checking"),
                      Email("work@gmail.com", "Work document", "Dear Lufuno, can you please kindly fix the mistakes on this work document"),
                      Email("order@gmail.com", "Package collection", "Good day Lufuno, your takealot order is ready for collection")
                      ]
    inbox.extend(example_emails)


def list_emails():
    """
    this function loops through the inbox and returns the subject line
    for each email
    """
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")


def read_email(index):
    """
    this function gets the email and returns the subject line,
    the email content and the email address of the email
    """
    if 0 <= index < len(inbox):
        print(f"\
        \nfrom: {inbox[index].email_address}\
        \nsubject line: {inbox[index].subject_line}\
        \nContent: {inbox[index].email_content}")
        inbox[index].mark_as_read()


def view_unread_emails():
    """
    this function allows the emails that have not been read
    by excluding the emails that have already been ready
    """
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line}")


populate_inbox()


# --- Email Program --- #
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )
# Control flow allowing user to make a choice
    if user_choice == 1:
        list_emails()
        email_index = int(input("enter email index: "))
        read_email(email_index)

    elif user_choice == 2:
        view_unread_emails()

    elif user_choice == 3:
        print("application is quitting, goodbye")
        break

    else:
        print("Oops - incorrect input.")
