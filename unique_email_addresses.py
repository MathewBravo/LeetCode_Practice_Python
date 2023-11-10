from typing import List
def num_unique_emails(emails: List[str])->int:
    uniq_emails = set()
    for email in emails:
        loc, dom = email.split('@')
        loc = loc.split('+')[0]
        loc = loc.replace('.', '')
        uniq_emails.add((loc, dom))
    return len(uniq_emails)

if __name__ == "__main__":
    result = num_unique_emails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(result)