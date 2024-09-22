SELECT g.group_name, 
       AVG(gr.grade) AS average_grade
FROM groups g
JOIN students s ON g.group_id = s.group_id
JOIN grades gr ON s.student_id = gr.student_id
WHERE gr.subject_id = 1
GROUP BY g.group_id;
