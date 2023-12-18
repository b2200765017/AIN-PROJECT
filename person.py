class Person:
    def __init__(self,emp_id, age, attrition, business_travel, department, distance_from_home, education, education_field,
                 employee_count,  gender, job_level,
                 job_role,  marital_status, monthly_income, num_companies_worked, over_18,
                 percent_salary_hike,  standard_hours, stock_option_level,
                 total_working_years, training_times_last_year,  years_at_company,
                 years_since_last_promotion, years_with_curr_manager,environment_satisfaction,job_satisfaction,work_life_balance,
                 job_involvement,performance_rating):
        """
        Initialize a new instance of the Person class with extended features.

        :param age: int, age of the employee.
        :param attrition: str, whether the employee left in the previous year or not.
        :param business_travel: str, how frequently the employees travelled for business purposes.
        :param department: str, department in the company.
        :param distance_from_home: float, distance from home in kilometers.
        :param education: int, education level.
        :param education_field: str, field of education.
        :param employee_count: int, employee count.
        :param employee_number: int, employee number/id.
        :param environment_satisfaction: int, work environment satisfaction level.
        :param gender: str, gender of employee.
        :param job_involvement: int, job involvement level.
        :param job_level: int, job level at company on a scale of 1 to 5.
        :param job_role: str, name of job role in company.
        :param job_satisfaction: int, job satisfaction level.
        :param marital_status: str, marital status of the employee.
        :param monthly_income: int, monthly income in rupees per month.
        :param num_companies_worked: int, total number of companies the employee has worked for.
        :param over_18: str, whether the employee is above 18 years of age or not.
        :param percent_salary_hike: int, percent salary hike for last year.
        :param performance_rating: int, performance rating for last year.
        
        :param standard_hours: int, standard hours of work for the employee.
        :param stock_option_level: int, stock option level of the employee.
        :param total_working_years: int, total number of years the employee has worked so far.
        :param training_times_last_year: int, number of times training was conducted for this employee last year.
        :param work_life_balance: int, work life balance level.
        :param years_at_company: int, total number of years spent at the company by the employee.
        :param years_since_last_promotion: int, number of years since last promotion.
        :param years_with_curr_manager: int, number of years under current manager.
        """
        self.emp_id = emp_id
        self.age = age
        self.attrition = attrition
        self.business_travel = business_travel
        self.department = department
        self.distance_from_home = distance_from_home
        self.education = education
        self.education_field = education_field
        self.employee_count = employee_count
      
        self.gender = gender
        self.job_level = job_level
        self.job_role = job_role
       
        self.marital_status = marital_status
        self.monthly_income = monthly_income
        self.num_companies_worked = num_companies_worked
        self.over_18 = over_18
        self.percent_salary_hike = percent_salary_hike
     
        self.standard_hours = standard_hours
        self.stock_option_level = stock_option_level
        self.total_working_years = total_working_years
        self.training_times_last_year = training_times_last_year
        self.years_at_company = years_at_company
        self.years_since_last_promotion = years_since_last_promotion
        self.years_with_curr_manager = years_with_curr_manager
        self.environment_satisfaction = environment_satisfaction
        self.job_satisfaction = job_satisfaction
        self.work_life_balance = work_life_balance
        self.job_involvement = job_involvement
        self.performance_rating = performance_rating





    def __str__(self):
        """
        String representation of the Person object with extended features.
        :return: str, description of the Person.
        """
        return (f"Person(age={self.age}, attrition='{self.attrition}', "
                f"business_travel='{self.business_travel}', department='{self.department}', "
                f"distance_from_home={self.distance_from_home}, education={self.education}, "
                f"education_field='{self.education_field}', employee_count={self.employee_count}, "
                f"employee_number={self.employee_number}, environment_satisfaction={self.environment_satisfaction}, "
                f"gender='{self.gender}', job_involvement={self.job_involvement}, job_level={self.job_level}, "
                f"job_role='{self.job_role}', job_satisfaction={self.job_satisfaction}, "
                f"marital_status='{self.marital_status}', monthly_income={self.monthly_income}, "
                f"num_companies_worked={self.num_companies_worked}, over_18='{self.over_18}', "
                f"percent_salary_hike={self.percent_salary_hike}, performance_rating={self.performance_rating}, "
                f"relationship_satisfaction={self.relationship_satisfaction}, standard_hours={self.standard_hours}, "
                f"stock_option_level={self.stock_option_level}, total_working_years={self.total_working_years}, "
                f"training_times_last_year={self.training_times_last_year}, work_life_balance={self.work_life_balance}, "
                f"years_at_company={self.years_at_company}, years_since_last_promotion={self.years_since_last_promotion}, "
                f"years_with_curr_manager={self.years_with_curr_manager})")
    



