import React from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { List, ListItem, Button } from '@material-ui/core';

function Quiz() {
  const [quiz, setQuiz] = React.useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = React.useState(0);
  const [score, setScore] = React.useState(0);

  const { id } = useParams();

  React.useEffect(() => {
    axios.get(`http://localhost:8000/api/quizzes/${id}`)
      .then(response => setQuiz(response.data))
      .catch(error => console.error(error));
  }, [id]);

  if (!quiz) {
    return null;
  }

  const currentQuestion = quiz.questions[currentQuestionIndex];

  const handleSubmitAnswer = choice => {
    if (choice.is_correct) {
      setScore(score => score + 1);
    }

    if (currentQuestionIndex + 1 < quiz.questions.length) {
      setCurrentQuestionIndex(index => index + 1);
    } else {
      // TODO: Redirect to results page
    }
  };

  return (
    <>
      <h2>{currentQuestion.text}</h2>
      <List>
        {currentQuestion.choices.map(choice => (
          <ListItem key={choice.id}>
            <Button onClick={() => handleSubmitAnswer(choice)}>
              {choice.text}
            </Button>
          </ListItem>
        ))}
      </List>
    </>
  );
}

export default Quiz;
