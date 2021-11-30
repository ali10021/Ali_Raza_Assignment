class customResponse():
    
    def __init__(self):
        self.response = dict()
        self.message = ""
        
    def addKey(self, key, value):
        self.response[key] = value
        
    def getResponse(self):
        return self.response
    
def calculate_average_sales(sales_data):
    total_revenue = 0
    total_number_sales = 0
    
    for item in sales_data:
        total_revenue = total_revenue + item.revenue
        total_number_sales = total_number_sales + item.sales_number
    
    if total_number_sales != 0:
        average_sales = total_revenue/total_number_sales
        return average_sales
    else:
        return "average sales could not be calculated because number of sales is zero"
    
def calculate_average_sales_for_all_users(sales_data):
    total_revenue = 0
    total_number_sales = 0
    
    for item in sales_data:
        total_revenue = total_revenue + item.revenue
        total_number_sales = total_number_sales + item.sales_number
    
    if total_number_sales != 0:
        average_sales_for_all_users = total_revenue/total_number_sales
        return average_sales_for_all_users
    else:
        return "average sales for all users could not be calculated because number of sales is zero"
        
    
    