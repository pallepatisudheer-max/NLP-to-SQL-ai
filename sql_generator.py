def generate_sql(question):

    question = question.lower()

    if "all employees" in question:
        return "SELECT * FROM employees"

    elif "salary greater than" in question:
        return """
        SELECT *
        FROM employees
        WHERE salary > 50000
        """

    elif "department" in question:
        return """
        SELECT *
        FROM employees
        WHERE department='IT'
        """

    return "SELECT * FROM employees"