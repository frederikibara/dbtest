SELECT AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.teacher_id = 1;  
