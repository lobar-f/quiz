from django.db import models
# from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    time_limit = models.DurationField()
    score = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.category} - Lesson {self.lesson_number} ({self.get_difficulty_display()})"

class Feedback(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    explanation = models.TextField()
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    audio = models.FileField(upload_to='questions/', blank=True, null=True)
    hints = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

class MultipleChoiceOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"
