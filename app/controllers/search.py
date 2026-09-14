from app.models.courses import Course

def searchCourse(args):
    query = args.get("query", "").strip()
    page = args.get("page", 1)
    limit = args.get("limit", 10)

    if not query:
        return {
            "success": True,
            "results": [],
            "metadata": {
                "total": 0,
                "total_pages": 0,
                "first_page": 1,
                "last_page": 1,
                "page": page,
                "previous_page": 1,
                "next_page": 1,
                "has_next": False,
                "has_prev": False
            }
        }

    courses_query = Course.query.filter(
        (Course.title.ilike(f"%{query}%")) |
        (Course.org.ilike(f"%{query}%"))
    )
    res = courses_query.paginate(page=page, per_page=limit, error_out=False)

    return {
        "success": True,
        "results": [course.to_dict() for course in res.items],
        "metadata": {
            "total": res.total,
            "total_pages": res.pages,
            "first_page": 1,
            "last_page": res.pages,
            "page": page,
            "previous_page": res.page - 1 if res.has_prev else 1,
            "next_page": res.page + 1 if res.has_next else res.page,
            "has_next": res.has_next,
            "has_prev": res.has_prev
        }
    }