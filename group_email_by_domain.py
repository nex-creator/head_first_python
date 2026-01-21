def group_email_by_domain(emails):
    grouped_by_domain ={}
    for email in emails:
        user_name, domain_name = email.split('@')
        if domain_name in grouped_by_domain:
            grouped_by_domain[domain_name]["count"] += 1
            grouped_by_domain[domain_name]["users"].append(user_name)
        else:
                grouped_by_domain[domain_name] = {
                    "count": 1,
                    "users": [user_name]
                }
                    

    return grouped_by_domain

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
    "dave@hotmail.com",
    "eve@yahoo.com"
]
print(group_email_by_domain(emails))