def simple_types(event, context):
    print(event)
    return event

def list_types(event, context):
    print(event)
    student_scores = {"John": 100, "Bob": 90, "Suresh": 93}
    scores = []
    for name in event:
        scores.append(student_scores[name])
    return scores



