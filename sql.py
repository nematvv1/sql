CREATE TABLE fan (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    fullname TEXT,
    phone TEXT,
    fan_id INT   -- fan jadvalidagi id
);

CREATE TABLE guruh (
    id SERIAL PRIMARY KEY,
    fan_id INT,       -- fan.id
    teacher_id INT,   -- teacher.id
    dars_jadval TEXT
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    fullname TEXT,
    phone TEXT,
    familyphone TEXT,
    guruh_id INT      -- guruh.id
);


CREATE TABLE homework (
    id SERIAL PRIMARY KEY,
    guruh_id INT,     -- guruh.id
    vazifa TEXT,
    vazifa_date DATE,
    oxirgi_muddat DATE,
    Field TEXT
);

CREATE TABLE homework_answer (
    id SERIAL PRIMARY KEY,
    homework_id INT,  -- homework.id
    student_id INT,   -- student.id
    answer_text TEXT,
    bajargan_vaqti TEXT
);

CREATE TABLE payment (
    id SERIAL PRIMARY KEY,
    student_id INT,   -- student.id
    amount NUMERIC,
    oy TEXT,
    sana DATE,
    status TEXT
);

CREATE TABLE davomat (
    id SERIAL PRIMARY KEY,
    student_id INT,   -- student.id
    guruh_id INT,     -- guruh.id
    sana DATE,
    status TEXT
);

