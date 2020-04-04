pdf_fields = {'student_no': None, 'date_of_birth': None, 'email': None, 'first_names': None, 'surname': None,
              'cell_no': None, 'year': None, 'from': None, 'to': None,

              # Column A details
              'course_code_a': None, 'convenor_name_A': None, 'ta_name_A': None,
              'day_A': None, 'date_A': None, 'description_A': None, 'time_start_A': None, 'time_stop_A': None,
              'duration_A': None,
              'day_A_1': None, 'date_A_1': None, 'description_A_1': None, 'time_start_A_1': None, 'time_stop_A_1': None,
              'duration_A_1': None,
              'day_A_2': None, 'date_A_2': None, 'description_A_2': None, 'time_start_A_2': None, 'time_stop_A_2': None,
              'duration_A_2': None,
              'day_A_3': None, 'date_A_3': None, 'description_A_3': None, 'time_start_A_3': None, 'time_stop_A_3': None,
              'duration_A_3': None,
              'day_A_4': None, 'date_A_4': None, 'description_A_4': None, 'time_start_A_4': None, 'time_stop_A_4': None,
              'duration_A_4': None,
              'day_A_5': None, 'date_A_5': None, 'description_A_5': None, 'time_start_A_5': None, 'time_stop_A_5': None,
              'duration_A_5': None,
              'day_A_6': None, 'date_A_6': None, 'description_A_6': None, 'time_start_A_6': None, 'time_stop_A_6': None,
              'duration_A_6': None,
              'day_A_7': None, 'date_A_7': None, 'description_A_7': None, 'time_start_A_7': None, 'time_stop_A_7': None,
              'duration_A_7': None,
              'day_A_8': None, 'date_A_8': None, 'description_A_8': None, 'time_start_A_8': None, 'time_stop_A_8': None,
              'duration_A_8': None,
              'day_A_9': None, 'date_A_9': None, 'description_A_9': None, 'time_start_A_9': None, 'time_stop_A_9': None,
              'duration_A_9': None,
              'day_A_100': None, 'date_A_10': None, 'description_A_10': None, 'time_start_A_10': None, 'time_stop_A_10': None,
              'duration_A_10': None,
              'day_A_11': None, 'date_A_11': None, 'description_A_11': None, 'time_start_A_11': None, 'time_stop_A_11': None,
              'duration_A_11': None,
              'day_A_12': None, 'date_A_12': None, 'description_A_12': None, 'time_start_A_12': None, 'time_stop_A_12': None,
              'duration_A_12': None,
              'day_A_13': None, 'date_A_13': None, 'description_A_13': None, 'time_start_A_13': None, 'time_stop_A_13': None,
              'duration_A_13': None,
              
              # Column B details
              'course_code_b': None, 'convenor_name_B': None, 'ta_name_B': None,
              'day_B': None, 'date_B': None, 'description_B': None, 'time_start_B': None, 'time_stop_B': None,
              'duration_B': None,
              'day_B_1': None, 'date_B_1': None, 'description_B_1': None, 'time_start_B_1': None, 'time_stop_B_1': None,
              'duration_B_1': None,
              'day_B_2': None, 'date_B_2': None, 'description_B_2': None, 'time_start_B_2': None, 'time_stop_B_2': None,
              'duration_B_2': None,
              'day_B_3': None, 'date_B_3': None, 'description_B_3': None, 'time_start_B_3': None, 'time_stop_B_3': None,
              'duration_B_3': None,
              'day_B_4': None, 'date_B_4': None, 'description_B_4': None, 'time_start_B_4': None, 'time_stop_B_4': None,
              'duration_B_4': None,
              'day_B_5': None, 'date_B_5': None, 'description_B_5': None, 'time_start_B_5': None, 'time_stop_B_5': None,
              'duration_B_5': None,
              'day_B_6': None, 'date_B_6': None, 'description_B_6': None, 'time_start_B_6': None, 'time_stop_B_6': None,
              'duration_B_6': None,
              'day_B_7': None, 'date_B_7': None, 'description_B_7': None, 'time_start_B_7': None, 'time_stop_B_7': None,
              'duration_B_7': None,
              'day_B_8': None, 'date_B_8': None, 'description_B_8': None, 'time_start_B_8': None, 'time_stop_B_8': None,
              'duration_B_8': None,
              'day_B_9': None, 'date_B_9': None, 'description_B_9': None, 'time_start_B_9': None, 'time_stop_B_9': None,
              'duration_B_9': None,
              'day_B_100': None, 'date_B_10': None, 'description_B_10': None, 'time_start_B_10': None, 'time_stop_B_10': None,
              'duration_B_10': None,
              'day_B_11': None, 'date_B_11': None, 'description_B_11': None, 'time_start_B_11': None, 'time_stop_B_11': None,
              'duration_B_11': None,
              'day_B_12': None, 'date_B_12': None, 'description_B_12': None, 'time_start_B_12': None, 'time_stop_B_12': None,
              'duration_B_12': None,
              'day_B_13': None, 'date_B_13': None, 'description_B_13': None, 'time_start_B_13': None, 'time_stop_B_13': None,
              'duration_B_13': None,
              
              }

def populate_pdf_dict(tutor, claims):
    # From tutor CSV
    filled_dict = pdf_fields.copy()
    filled_dict['student_no'] = tutor["student_no"]
    filled_dict['date_of_birth'] = tutor["date_of_birth"]
    filled_dict['email'] = tutor["email"]
    filled_dict['first_names'] = tutor["first_names"]
    filled_dict['surname'] = tutor["surname"]
    filled_dict['cell_no'] = tutor["cell_no"]
    filled_dict['year'] = tutor["year"]

    # A tasks
    filled_dict['course_code_a'] = "EEE4120F"
    filled_dict['convenor_name_A'] = "Simon Winberg"
    filled_dict['ta_name_A'] = "Keegan Crankshaw"

    filled_dict['day_A'] = claims[0][0]
    filled_dict['date_A'] = claims[0][1]
    filled_dict['description_A'] = claims[0][2]
    filled_dict['time_start_A'] = claims[0][3]
    filled_dict['time_stop_A'] = claims[0][4]
    filled_dict['duration_A'] = claims[0][5]

    filled_dict['day_A_1'] = claims[0][0]
    filled_dict['date_A_1'] = claims[0][1]
    filled_dict['description_A_1'] = claims[0][2]
    filled_dict['time_start_A_1'] = claims[0][3]
    filled_dict['time_stop_A_1'] = claims[0][4]
    filled_dict['duration_A_1'] = claims[0][5]
    
    filled_dict['day_A_2'] = claims[1][0]
    filled_dict['date_A_2'] = claims[1][1]
    filled_dict['description_A_2'] = claims[1][2]
    filled_dict['time_start_A_2'] = claims[1][3]
    filled_dict['time_stop_A_2'] = claims[1][4]
    filled_dict['duration_A_2'] = claims[1][5]

    # Repeat to 13

    # Calculated/dynamic
    filled_dict['from'] = tutor["date_of_birth"]
    filled_dict['to'] = tutor["date_of_birth"]
    filled_dict['sign_date'] = "4/4/2020"
    return filled_dict


def Populate_rev2(tutor, claims):
    filled_dict = pdf_fields.copy()
    # fill claims
    for key in filled_dict:
        if "day" in key:
            print("found day!")
            print(key)
            index = str(key)[-2:]
            print(index, "0")

    return filled_dict