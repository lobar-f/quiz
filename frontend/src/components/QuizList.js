import React from 'react';
import axios from 'axios';
import { List, ListItem, Button } from '@material-ui/core';

function QuizList() {
  const [quizzes, setQuizzes] = React.useState([]);

  React.useEffect(() => {
    axios.get('http://localhost:8000/api/quizzes')
      .then(response => setQuizzes(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <List>
      {quizzes.map(quiz => (
        <ListItem key={quiz.id}>
          <Button href={`/quiz/${quiz.id}`}>{quiz.title}</Button>
        </ListItem>
      ))}
    </List>
  );
}

export default QuizList;
