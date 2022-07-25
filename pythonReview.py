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

def add_comments(video,username,comment_text):
	if 'comment' in video:
		comment['username']:'comment_text'
