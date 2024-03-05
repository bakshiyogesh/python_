import sqlite3

connection=sqlite3.connect('youtube_manager.db')
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS VIDEOS(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
)
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time)  VALUES(?,?)",(name,time))
    connection.commit()
def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time= ? WHERE id =?",(name,time,video_id))
    connection.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,)) 
    # here we give comma here because it accepts value in tuple and 
    #if you want to make tuple with single element you need to use comma
    connection.commit()
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1.list Videos")
        print("2.Add videos")
        print("3.Update Videos")
        print("4. Delete Videos")
        print("5.Exit app")
        choice=input("Enter a choice:")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name")
            time=input("Enter the video time")
            add_video(name,time)
        elif choice=='3':
            videoId=input("Enter the videoId to update")
            name=input("Enter the video name")
            time=input("Enter the video time")
            add_video(videoId,name,time)
        elif choice=='4':
            videoId=input("Enter the videoId to delete")
            delete_video(videoId)
connection.close()
if __name__=="__main__":
    main()