SELECT s.name AS student_name, 
       g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = 1 AND g.subject_id = 1 
AND g.date = (SELECT MAX(date) FROM grades WHERE student_id = s.student_id AND subject_id = 1);  
