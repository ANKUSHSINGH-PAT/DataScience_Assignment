import pandas as pd

Data = pd.read_csv("Input/Salaries.csv")
sal = pd.DataFrame(Data)
# print(sal.head())
# print(sal.info())
sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
print(sal.columns)
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
max_pay = sal['TotalPay'].max()
print(max_pay)
print(sal[sal['TotalPay'] == sal['TotalPay'].max()]['EmployeeName'])

emp_name_max_benefit = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
print(emp_name_max_benefit)

emp_name_min_benefit = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
listemp = list(emp_name_max_benefit)
print(listemp[0])
# print(emp_name_min_benefit)
# print(emp_name_max_benefit[1])
emp_details = sal[sal['EmployeeName'] == listemp[0]]
print(emp_details)

# Convert 'Year' column to datetime format
sal['Year'] = pd.to_datetime(sal['Year'])
print(sal['Year'])

# Filter data for the years 2011 to 2014
base_pay = pd.to_numeric(sal['BasePay'], errors='coerce')
print(base_pay)

print(sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head(5))

# print(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

print(sal.groupby('Year').mean()['BasePay'])

print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))


def count(s):
    if 'chef' in s.lower():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x: count(x))))


