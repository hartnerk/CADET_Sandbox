from django.db import models
from django.utils import timezone

# This file will organize the data retrieved from the data layer after it has 
# been analyzed. Based off of the Data layer team's spec D88, it is 
# expected that A topic model dictionary and a list of comment objects will 
# be retrieved. The following code below will take this information and model 
# it in to a JSON that the charts in distribution_chart/views.py can read.
class Instructor(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

class Course(models.Model):
	name = models.CharField(max_length=50)
	year = models.PositiveSmallIntegerField(default=1)
	SEMESTERS = (
		('1', 'Spring'),
		('2', 'Summer'),
		('3', 'Fall'),
	)
	semester = models.CharField(max_length=1, choices=SEMESTERS)

#class Results_Topic(models.Model):
#	topic_label = models.ForeignKey(
#		Topic.topic_id,
#		on_delete=models.CASCADE)
#	comment_sentiment = models.ForeignKey(
#		Comment.tone,
#		on_delete=models.CASCADE)

#class Results_Instructor(models.Model):
#	name = models.ForeignKey(
#		Instructor.first_name + " " + Instructor.last_name,
#		on_delete=models.CASCADE)
#	comment_count = # of comments

class Comment(models.Model):
	# Topic of Instructor comment?
	TYPES = (
		('0', 'instructor'),
		('1', 'topic')
	)
	type_of_comm = models.CharField(max_length=1, choices=TYPES)
	# many comments belong to one instructor
	instructor = models.ForeignKey(
		Instructor,
		on_delete=models.CASCADE)
	# many comments belong to one course
	course = models.ForeignKey(
		Course,
		on_delete=models.CASCADE)
	# what the comment says
	text = models.TextField()
	# what is the sentiment?
	TONES = (
		('pos', 'positive'),
		('neu', 'neutral'),
		('neg', 'negative')
	)
	tone = models.CharField(max_length=3, choices=TONES)
	# Topic ID
	topic_id = models.IntegerField()

class Topic(models.Model):
	topic_id = models.IntegerField()
	# many topics belong to one comment
	comment = models.ForeignKey(
		Comment,
		on_delete=models.CASCADE)
	text = models.TextField()
