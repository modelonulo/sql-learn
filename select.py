# METODO read_sql_table

    # load tabela inteira com o engine
    df = pd.read_sql_table('employees',engine)

    # load algumas colunas 
    df = pd.read_sql_table('employees', engine, columns=["first_name","last_name"])

# METODO read_sql_query

    # seleciona todos e cria df
    df = pd.read_sql_query("select * from employees",engine)

    # liga varias tabelas
    query = '''
    SELECT  emp.first_name,
            emp.last_name,
            emp.gender,
            depar.dept_name as departament_name,
            dept.from_date,
            dept.to_date
    FROM employees emp
    INNER JOIN dept_emp dept
    ON emp.emp_no = dept.emp_no
    INNER JOIN departments depar
    ON dept.dept_no = depar.dept_no;
    '''

    df = pd.read_sql_query(query,engine)
    df.head()

        
    #SELECT ----------------
        
        query = '''
        SELECT name from employees;
        '''

        #seleciona a coluna nome da tabela pessoa 
        
        # SELECT and FROM sao keywords e nao sao case-sensitives 
        query = '''
        SELECT name FROM people;
        '''
        
        #seleciona mais de uma coluna
        # seleciona title and release year from films
        query = '''
        SELECT title, release_year
        FROM films;
        '''
        
        query = '''
        SELECT title, release_year, country
        FROM films;
        '''
        #seleciona todas linhas
        query = '''
        SELECT * FROM films;
        '''
    
        #seleciona valores valores unicos (apenas uma vez cada valor) de uma coluna
        # DISTINCT        
        query = ''' 
        SELECT DISTINCT country from films;
        '''

        #COUNT number of 
        #traz quantas colunas tem 
        
        #COUNT todos registros (*) de reviews
        query = ''' 
        SELECT COUNT(*) FROM reviews;
        '''
        
        #COUNT numero de registros/LINHAS em uma coluna, chamamos a coluna
        
        #contar numero de registros presentes de birthdates na planilha peolple
        query = '''
        SELECT COUNT(birthdate) FROM people;
        '''
        
        #contar numero de valores UNICOS de uma coluna em uma planilha 
        # COUNT + DISTINCT
        
        #quantidade de datas unicas
        query = '''
        SELECT COUNT(DISTINCT birthdate)
        FROM people;
        '''
        #SELECT FILTERING WHERE----------------
        #filter numeric and text, However, so far you've only been able 
        #to filter by specifying the exact text you're interested in
        
        # FROM + WHERE (sempre usado apos FROM )
        
        # seleciona todos filmes com ano de lancamento 2016
        query = '''
        SELECT * FROM films WHERE release_year = 2016;
        '''
        
        #numero total de filmes lancados antes de 2000
        query = '''
        SELECT COUNT(*) FROM films WHERE release_year < 2000;
        ''''
        
        #Get all details for all films released in 2016.
        query = '''
        SELECT * FROM films WHERE release_year = 2016;
        '''
        
        #Get the number of films released before 2000.
        query = '''
        SELECT COUNT(*) FROM films WHERE release_year < 2000;
        '''
        
        #Get the title and release year of films released after 2000.
        query = '''
        SELECT title, release_year FROM films WHERE release_year > 2000;
        '''
        
        #Get all details for all French language films.
        query = '''
        SELECT * FROM films WHERE language = 'French';
        '''
        
        #Get the name and birth date of the person born on November 11th, 1974. Remember to use ISO date format ('1974-11-11')!
        query = '''
        SELECT name, birthdate FROM people WHERE birthdate = '1974-11-11';
        '''

        #Get the number of Hindi language films.
        query = '''
        SELECT COUNT(*) FROM films WHERE language = 'Hindi';
        '''
        
        #SELECT FILTERING WHERE AND ----------------
        #Get the title and release year for all Spanish language films released before 2000.
        query = '''
        SELECT title, release_year FROM films WHERE language = 'Spanish' AND release_year < 2000;
        '''
        
        # Get all details for Spanish language films released after 2000.
        query = '''
        SELECT * FROM films WHERE language = 'Spanish' and release_year > 2000;
        '''
 
        #Get all details for Spanish language films released after 2000, but before 2010.
        query = '''
        SELECT * FROM films 
        WHERE language = 'Spanish' AND release_year > 2000 AND release_year < 2010;
        '''
        
        #SELECT FILTERING WHERE AND OR ----------------
        
        # OR Display only rows that meet at least one of the specified conditions.
        
        #returns all films released in either 1994 or 2000:
        query = '''
        SELECT title
        FROM films
        WHERE release_year = 1994
        OR release_year = 2000;
        ''''

        #seleciona filmes que fora lancados em 1994 OU 1995 E tem a certificacao PG OU R 
        
        query = '''
        SELECT title
        FROM films
        WHERE (release_year = 1994 OR release_year = 1995)
        AND (certification = 'PG' OR certification = 'R');
        '''
        
        #Get the title and release year for films released in the 90s.
        query = ''' 
        SELECT title, release_year
        FROM films 
        WHERE release_year >= 1990 AND release_year < 2000;
        ''''
        
        #Now, build on your query to filter the records to only include French or Spanish language films.
        query = '''
        SELECT title, release_year
        FROM films
        WHERE (release_year >= 1990 AND release_year < 2000)
        AND (language = 'French' OR language = 'Spanish');
        '''
        
        #Finally, restrict the query to only return films that took in more than $2M gross.
        query = '''         
        SELECT title, release_year
        FROM films
        WHERE (release_year >= 1990 AND release_year < 2000)
        AND (language = 'French' OR language = 'Spanish')
        AND gross > 2000000;
        ''''

        #SELECT FILTERING BETWEEM ----------------

        # Get the title and release year of all films released between 1990 and 2000 (inclusive).
        query = '''
        SELECT title, release_year FROM films  * where release_year BETWEEN 1990 AND 2000;
        '''
        
        
        #SELECT WHERE IN 
        
        #para quando precisamos especificar determinados valores. 
        
        #titulo e linguagem de filmes em ingles, espanhol ou frances
        
        query = '''
        SELECT title, language
        FROM films
        WHERE language IN ('English', 'Spanish', 'French');
        '''
        
        #Get the title and certification of all films with an NC-17 or R certification.
        query = '''
        SELECT title, certification
        FROM films
        WHERE certification IN ('NC-17', 'R');
        '''
        
        #Get the names of people who are still alive, i.e. whose death date is missing.
        query = '''
        Get the names of people who are still alive, i.e. whose death date is missing.
        '''
        
        #Get the number of films which don't have a language associated with them.
        query = '''
        SELECT COUNT(*)
        FROM films
        WHERE language IS NULL;
        '''

        #WHERE + LIKE // NOT LIKE
        #LIKE operator can be used in a WHERE clause to search for a pattern in a column
        #para isto, wildcard as a placeholder for some other values. 
        #There are two wildcards you can use with LIKE
        
        #% match zero, one, or many characters in text. Vai retornar:'Data', 'DataC' 'DataCamp', 'DataMind'
        query = '''
        SELECT name FROM companies WHERE name LIKE 'Data%';
        '''

        #_ retorna single charactere. vai retornar 'DataCamp', 'DataComp'
        query = '''
        SELECT name FROM companies WHERE name LIKE 'DataC_mp'
        '''

        #NOT LIKE retorna os resultados que nao match.

        #Get the names of all people whose names begin with 'B'.
        query = '''
        SELECT name
        FROM people
        WHERE name LIKE 'B%'
        '''

        #Get the names of people whose names have 'r' as the second letter
        query = '''
        SELECT name
        FROM people
        WHERE name LIKE '_r%';
        '''

        #Get the names of people whose names don't start with A
        query = '''
        SELECT name
        FROM people
        name NOT LIKE 'A%'
        '''

    #FUNCOES DE AGREGACAO = AGGREGATE FUNCTIONS
    #funcoes para calcular soma, media, maximo ex

        #Get the average value from the budget column of the films - media
        query = '''
        SELECT AVG(budget)
        FROM films;
        '''

        #Get the MAX value from the budget column of the films - maximo
        query = '''
        SELECT MAX(budget)
        FROM films;
        '''

        #Use the SUM() function to get the total duration of all films. - soma
        query = '''
        SELECT SUM(duration)
        FROM films;
        '''

        #Selecione a duracao do filme mais curto
        query = '''
        SELECT MIN(duration)
        FROM films;
        ''' 

#Combinando funcoes de agregacao com o WHERE. 

        #get the total budget of movies made in the year 2010 or later:
        query = '''
        SELECT SUM(budget) 
        FROM Films
        WHERE release_year >= 2010;
        '''

        #Get the average amount grossed by all films whose titles start with the letter 'A'
        que = '''
        SELECT AVG(gross)
        FROM Films
        where title LIKE 'A%'
        '''
        
        #Get the amount grossed by the worst performing film in 1994.
        query = '''
        SELECT MIN(gross)
        FROM films 
        WHERE release_year = 1994;
        '''

        #Get the amount grossed by the best performing film between 2000 and 2012, inclusive
        query = '''
        SELECT MAX(gross)
        FROM films
        WHERE release_year BETWEEN 2000 AND 2012;
        '''

#Operacoes matematicas

        #SQL assume que se vc divide um inteiro por um inteiro, vc deseja um inteiro como resultado. 
        #se precisa de precisao, adicionar casas decimais nos numeros. ex:

        query = '''
        SELECT (4 / 3);
        ''' #resulta em 1

        query = '''
        SELECT (4.0 / 3.0)
        ''' #resulta em 1.333



        







        









        
        



        




    