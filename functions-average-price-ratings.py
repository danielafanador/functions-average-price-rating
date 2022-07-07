
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(float(value))
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += element
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return column

#AVERAGE PRICE
price_column = extract (apps_data, 4)
avg_price = sum(price_column) / len(price_column)
print ('Average price:')
print (avg_price)
print (sum(price_column))
print (len(price_column))
print ('')

#AVERAGE RATING
rating_column = mean(apps_data, 7)
avg_rating = sum(rating_column) / len(rating_column) 
print ('Average rating:')
print (avg_rating)
print (sum(rating_column))
print (len(rating_column))
print ('')
print ('')