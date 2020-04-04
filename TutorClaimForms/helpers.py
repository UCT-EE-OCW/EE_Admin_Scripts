from datetime import datetime

pdf_fields = {'student_no': None, 'date_of_birth': None, 'email': None, 'first_names': None, 'surname': None,
              'cell_no': None, 'year': None, 'from': None, 'to': None, 'PhD': "", 'MSc': "", 'UG': "",

              # Column A details
              'course_code_A': None, 'convenor_name_A': None, 'ta_name_A': None, 'total_A': None,
              'day_A_00': None, 'date_A_00': None, 'description_A_00': None, 'time_start_A_00': None, 
              'time_stop_A_00': None, 'duration_A_00': None,
              'day_A_01': None, 'date_A_01': None, 'description_A_01': None, 'time_start_A_01': None, 
              'time_stop_A_01': None, 'duration_A_01': None,
              'day_A_02': None, 'date_A_02': None, 'description_A_02': None, 'time_start_A_02': None, 
              'time_stop_A_02': None, 'duration_A_02': None,
              'day_A_03': None, 'date_A_03': None, 'description_A_03': None, 'time_start_A_03': None, 
              'time_stop_A_03': None, 'duration_A_03': None,
              'day_A_04': None, 'date_A_04': None, 'description_A_04': None, 'time_start_A_04': None, 
              'time_stop_A_04': None, 'duration_A_04': None,
              'day_A_05': None, 'date_A_05': None, 'description_A_05': None, 'time_start_A_05': None, 
              'time_stop_A_05': None, 'duration_A_05': None,
              'day_A_06': None, 'date_A_06': None, 'description_A_06': None, 'time_start_A_06': None, 
              'time_stop_A_06': None, 'duration_A_06': None,
              'day_A_07': None, 'date_A_07': None, 'description_A_07': None, 'time_start_A_07': None, 
              'time_stop_A_07': None, 'duration_A_07': None,
              'day_A_08': None, 'date_A_08': None, 'description_A_08': None, 'time_start_A_08': None, 
              'time_stop_A_08': None, 'duration_A_08': None,
              'day_A_09': None, 'date_A_09': None, 'description_A_09': None, 'time_start_A_09': None, 
              'time_stop_A_09': None, 'duration_A_09': None,
              'day_A_10': None, 'date_A_10': None, 'description_A_10': None, 'time_start_A_10': None, 
              'time_stop_A_10': None, 'duration_A_10': None,
              'day_A_11': None, 'date_A_11': None, 'description_A_11': None, 'time_start_A_11': None, 
              'time_stop_A_11': None, 'duration_A_11': None,
              'day_A_12': None, 'date_A_12': None, 'description_A_12': None, 'time_start_A_12': None, 
              'time_stop_A_12': None, 'duration_A_12': None,
              'day_A_13': None, 'date_A_13': None, 'description_A_13': None, 'time_start_A_13': None, 
              'time_stop_A_13': None, 'duration_A_13': None,
              
              # Column B details
              'course_code_B': None, 'convenor_name_B': None, 'ta_name_B': None, 'total_B': None,
              'day_B_00': None, 'date_B_00': None, 'description_B_00': None, 'time_start_B_00': None,
              'time_stop_B_00': None, 'duration_B_00': None,
              'day_B_01': None, 'date_B_01': None, 'description_B_1': None, 'time_start_B_1': None,
              'time_stop_B_1': None,'duration_B_1': None,
              'day_B_02': None, 'date_B_02': None, 'description_B_02': None, 'time_start_B_02': None,
              'time_stop_B_02': None, 'duration_B_02': None,
              'day_B_03': None, 'date_B_03': None, 'description_B_03': None, 'time_start_B_03': None,
              'time_stop_B_03': None, 'duration_B_03': None,
              'day_B_04': None, 'date_B_04': None, 'description_B_04': None, 'time_start_B_04': None,
              'time_stop_B_04': None, 'duration_B_04': None,
              'day_B_05': None, 'date_B_05': None, 'description_B_05': None, 'time_start_B_05': None,
              'time_stop_B_05': None, 'duration_B_05': None,
              'day_B_06': None, 'date_B_06': None, 'description_B_06': None, 'time_start_B_06': None,
              'time_stop_B_06': None, 'duration_B_06': None,
              'day_B_07': None, 'date_B_07': None, 'description_B_07': None, 'time_start_B_07': None,
              'time_stop_B_07': None, 'duration_B_07': None,
              'day_B_08': None, 'date_B_08': None, 'description_B_08': None, 'time_start_B_08': None,
              'time_stop_B_08': None, 'duration_B_08': None,
              'day_B_09': None, 'date_B_09': None, 'description_B_09': None, 'time_start_B_09': None,
              'time_stop_B_09': None, 'duration_B_09': None,
              'day_B_100': None, 'date_B_10': None, 'description_B_10': None, 'time_start_B_10': None,
              'time_stop_B_10': None,'duration_B_10': None,
              'day_B_11': None, 'date_B_11': None, 'description_B_11': None, 'time_start_B_11': None,
              'time_stop_B_11': None, 'duration_B_11': None,
              'day_B_12': None, 'date_B_12': None, 'description_B_12': None, 'time_start_B_12': None,
              'time_stop_B_12': None, 'duration_B_12': None,
              'day_B_13': None, 'date_B_13': None, 'description_B_13': None, 'time_start_B_13': None,
              'time_stop_B_13': None, 'duration_B_13': None}


def fill(lst, index1, index2):
    try:
        val = lst[index1][index2]
    except IndexError:
        val = ""
    return val


def populate_pdf(tutor, claims):
    # From tutor CSV - "static" content
    filled_dict = pdf_fields.copy()
    filled_dict['student_no'] = tutor["student_no"]
    filled_dict['date_of_birth'] = tutor["date_of_birth"]
    filled_dict['email'] = tutor["email"]
    filled_dict['first_names'] = tutor["first_names"]
    filled_dict['surname'] = tutor["surname"]
    filled_dict['cell_no'] = tutor["cell_no"]
    filled_dict[tutor["current_degree"]] = "Y"
    filled_dict['year'] = tutor["year"]

    # Claims
    for key in filled_dict:
        index = key[-2:]
        if "day_A" in key:
            filled_dict[key] = fill(claims, int(index), 0)
        if "date_A" in key:
            filled_dict[key] = fill(claims, int(index), 1)
        if "description_A" in key:
            filled_dict[key] = fill(claims, int(index), 2)
        if "start_A" in key:
            filled_dict[key] = fill(claims, int(index), 3)
        if "stop_A" in key:
            filled_dict[key] = fill(claims, int(index), 4)
        if "duration_A" in key:
            filled_dict[key] = fill(claims, int(index), 5)

    # Calculated/dynamic
    filled_dict['total_A'] = sum(float(claims[i][5]) for i in range(len(claims)))
    filled_dict['from'] = claims[0][1]
    filled_dict['to'] = claims[len(claims)-1][1]
    filled_dict['sign_date'] = datetime.now().strftime("%d/%m/%Y")
    return filled_dict
