# just a quick demo of how we can use "" ,'' & '''.
subject = 'very responsive'
print(subject)

# what to do if we have something like john's laptop is good.
response = "john's laptop is good" # we use "" to avoid errors
print(response)

#what to do if we need to say john said,"my laptop is working fine"
response = 'john said,"my laptop is working fine."'
print(response)

# in an email we need to use tripple quotes to define the message ie. '''
email_message ='''
hi sir,
Please note that all incoming mail's will be forwarded to mail@jfc.com.

Thanks.
kind regards,
nick.
'''
print(email_message)

# getting character of an index we use square brackets
subject = 'very responsive' #starts from 0 or the way while -1 is the last character
print(subject[0:-1])
