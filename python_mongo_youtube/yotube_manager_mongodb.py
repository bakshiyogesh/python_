from pymongo import MongoClient
from bson import ObjectId
client = MongoClient(
    "mongodb+srv://CHAI:CHAI@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificates=True)
# tlsAllowInvalidCertificate=TRue not a good way to handle ssl
db = client['ytmanager']
video_collection = db['videos']
print(video_collection)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_videos():
    for video in video_collection.find():
        print(
            f"ID:{video['_id']},Name :{video['name']} and Time:{video['time']}")


def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, {"$set": {"name": name, "time": time}})


def delete_video(video_id):
    video_collection.delete_one({
        '_id': video_id
    })


def main():
    while True:
        print("\nYoutube Videos")
        print("1. List all video")
        print("2. Add a new Video")
        print("3 Update a video")
        print("4 Delete a video")
        print("5 Exit the app")
        choice = input("Enter your choice:")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            add_video(name, time)
        elif choice == '3':
            name = input("Enter the updated name:")
            time = input("Enter the updated time:")
            video_id = input("Enter video id to update")
            update_video(name, time, video_id)
        elif choice == '4':
            video_id = input("Enter video id to delete")
            delete_video(video_id)
        elif choice == '5':
            break


if __name__ == '__main__':
    main()
