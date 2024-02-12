import requests
import hashlib
import sys

# 'CBFDA'
def request_api_data(query_param):
    url = 'https://api.pwnedpasswords.com/range/' + query_param
    res = requests.get(url)
    code = res.status_code
    if code != 200:
        raise RuntimeError(f'error fetching resonse: {code}, check your request')
    else: 
        return res

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1password[:5], sha1password[5:]
    print(sha1password)
    response = request_api_data(head)
    return get_password_leak_count(response, tail)

def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def main(args):
     for password in args:
         count = pwned_api_check(password)
         if count!=0:
            print(f'{password} was found {count} times... you should probably change your password!')
         else:
            print(f'{password} was NOT found. Carry on!')

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
