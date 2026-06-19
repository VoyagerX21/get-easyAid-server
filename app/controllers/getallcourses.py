from app.models.courses import Course

def getallcourses(args):
    page = args.get("page", 1)
    limit = args.get("limit", 10)
    query = Course.query.filter()
    res = query.paginate(page=page, per_page=limit,error_out=False)
    return {
        "data": [i.to_dict() for i in res.items],
        "metadata": {
            "total": res.total,
            "total_pages": res.pages,
            "first_page": 1,
            "last_page": res.pages,
            "page": page,
            "previous_page": res.page-1 if res.has_prev else 1,
            "next_page": res.page+1 if res.has_next else res.page,
            "has_next": res.has_next,
            "has_prev": res.has_prev
        }
    }