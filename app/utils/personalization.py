def personalisedDetails(data):
    def get_value(key):
        value = data.get(key, "")
        if isinstance(value, list):
            return value[0].strip() if value else ""
        return str(value).strip()
    name = get_value("name")
    course = get_value("courseType")
    specialization = get_value("specialization")
    institute = get_value("institute")
    organization = get_value("organization")
    position = get_value("position")
    year = get_value("year")
    courses = data.get("courses", [])
    if isinstance(courses, list):
        courses = ", ".join(courses)
    if specialization and "/" in specialization:
        specialization = specialization.split("/")[-1]
    fields = []
    if name:
        fields.append(f"Name: {name}")
    if institute:
        fields.append(f"Institute: {institute}")
    if year:
        fields.append(f"Academic Year: {year}")
    if organization:
        fields.append(f"Organization: {organization}")
    if position:
        fields.append(f"Position: {position}")
    if courses:
        fields.append(f"Completed Courses: {courses}")
    if specialization:
        fields.append(f"Specialization: {specialization}")
    if course:
        fields.append(f"Course Applying For: {course}")
    structured = "User Details:\n" + "\n".join(fields)
    return structured