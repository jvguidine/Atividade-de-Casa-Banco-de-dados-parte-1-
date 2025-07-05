# Atividade - Parte 2 (SQL no Supabase)

## Inserção de 2 contatos via SQL

SQL Editor

INSERT INTO app_person (name, age, gender) VALUES
    ('Lucas', 25, 'male'),
    ('Laura', 30, 'female');

## Consulta nomes que contém a letra "L" e que começam com a letra "L".

SELECT * FROM app_person
WHERE name ILIKE '%l%';

ou 

SELECT * FROM app_person
WHERE name ILIKE 'l%';

## Atualização da idade do Lucas

UPDATE app-person
SET age = 26
WHERE id = 4;

## Ranking dos nomes mais frequentes 

SELECT
    SPLIT_PART(name, ' ', 1) AS first_name,
    COUT(*) AS total
FROM app_person
GROUP BY first_name
ORDER BY total DESC;