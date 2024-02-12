import requests
import hashlib
import sys
import bisect

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
    response = request_api_data(head)
    return get_password_leak_count(response, tail)

def binary_search(hashes, hash_to_check):
    hash_values = [hash_tuple[0] for hash_tuple in hashes]
    index = bisect.bisect_left(hash_values, hash_to_check)
    if index < len(hashes) and hashes[index][0] == hash_to_check:
        return hashes[index][1]
    return 0

def get_password_leak_count(hashes, hash_to_check):
    hashes = [line.split(':') for line in hashes.text.splitlines()]
    hashes.sort()
    return binary_search(hashes, hash_to_check)

def main(args):
     for password in args:
         count = pwned_api_check(password)
         if count!=0:
            print(f'{password} was found {count} times, consider another password')
         else:
            print(f'{password} was not found and may be considered safe to use')

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
