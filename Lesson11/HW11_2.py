def hide_mail(email):
    a_index = email.find('@')
    a = '***@**'
    return email[:a_index - 3] + a + email[a_index + 4:]


print(hide_mail('somebody_email@gmail.com'))