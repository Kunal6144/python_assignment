gender = input('Enter your Gender: ').lower()
hemoglobin = float(input('Enter your Heamoglobin Value (g/l): ').lower())

if (gender == 'male' or gender == 'm') and (134 <= hemoglobin <= 167):
    print('Your Hemoglobin valus is normal for males')
elif (gender == 'male' or gender == 'm') and (134 >= hemoglobin >= 167):
    print('Your Hemoglobin valus is not normal for males')
elif (gender == 'female' or gender == 'f') and (117 >= hemoglobin >= 155):
    print('Your Hemoglobin valus is not normal for females')
elif (gender == 'female' or gender == 'f') and (117 <= hemoglobin <= 155):
    print('Your Hemoglobin valus is normal for females')
