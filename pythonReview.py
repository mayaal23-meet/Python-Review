def create_youtube_video(title,description):

	video = {"title":title , 'description':description, 'like':0 , 'dislike':0 , 'comment':{}}

def like(video):
	if 'like' in video:
		video['like'] +=1
	return video

def dislike(video):
	if 'dislike' in video:
		video['dislike'] +=1
	return video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo['comments'] = {username, comment_text}
	return youtubevideo


def main():
	new_youtube_dict = create_youtube_video("Summer Y2", "MEET's Summer")
	like(new_youtube_dict)
	dislike(new_youtube_dict)
	add_comment(new_youtube_dict, "Noa", "I love it")
	print("Title: ", new_youtube_dict['title'])
	print("Description: ", new_youtube_dict['description'])
	print(new_youtube_dict['likes'], " people liked that :)")
	print(new_youtube_dict['dislikes'], " people disliked that :(")
	print("Comments: \n==========")
	print(new_youtube_dict['comments'])

if __name__ == '__main__':
	main()