value_salary = float(input ("Informe seu salário fixo: "))

value_sales = float(input ("Informe o valor das vendas: "))


if value_sales <= 1500:
   total_salary = (value_sales*5/100)+value_salary
   print(f"O salário total final do vendedor é: {total_salary}")
    
else:
    difer_value_sales = value_sales-1500
    value_sales_basic = value_sales-difer_value_sales
    total_salary = value_salary+(value_sales_basic*5/100)+(difer_value_sales*7/100)
    print(f"O salário total final do vendedor é {total_salary}")

                 