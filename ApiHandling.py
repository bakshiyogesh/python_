import requests

def fetch_random_user_data():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    print(data)
    if data['success'] and 'data' in data:
        user_data=data['data']
        user_name=user_data['login']['username']
        user_country=user_data['location']['country']
        return user_name,user_country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        user_name,user_country=fetch_random_user_data()
        print(f"UserName:{user_name} \nCountry:{user_country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()