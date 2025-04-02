#using SHA1 for hashing
import requests #browser without browser
import hashlib
import sys

#Api uses k anonymity which allows others to see the info without knowing the other user info
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # below we get response from the url
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'error fetching : {res.status_code},check the api and try again')
    return res

# #function for reading response
# def read_res(response):
#     print(response.text)
def get_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #put first 5 characters so remove the tail(remaining characters)
    first5_char, tail = sha1password[:5],sha1password[5:]
    # check password if it exist in api response
    response = request_api_data(first5_char)
    return get_leaks_count(response,tail)

#main function
def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

