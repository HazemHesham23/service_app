import frappe

def get_permission_query_conditions_for_service_project(user):
    user_roles = frappe.get_roles(user)

    # السماح الكامل للمديرين
    if "System Manager" in user_roles or "Projects Manager" in user_roles:
        return ""

    # تطبيع الأدوار حسب القيم الموجودة في assigned_role
    role_normalization_map = {
        "Accounts Manager": "Account Manager",
        "Analytics": "Analyst",
    }

    normalized_roles = set()
    for role in user_roles:
        normalized_roles.add(role_normalization_map.get(role, role))

    # الحصول على اسم الشركة من الـ Employee المرتبط بالمستخدم
    employee_company = frappe.db.get_value("Employee", {"user_id": user}, "company")
    if not employee_company:
        return "1=0"  # لا يوجد موظف مرتبط، لا يسمح برؤية أي مشروع

    roles_list = "', '".join(normalized_roles)

    conditions = f"""
        organization = '{employee_company}' AND
        assigned_role IN ('{roles_list}')
    """
    return conditions


def get_permission_query_conditions_for_service_task(user):
    user_roles = frappe.get_roles(user)

    # السماح الكامل للمديرين
    if "System Manager" in user_roles or "Projects Manager" in user_roles:
        return ""

    # تطبيع الأدوار حسب القيم الموجودة في assigned_role
    role_normalization_map = {
        "Accounts Manager": "Account Manager",
        "Analytics": "Analyst",
    }

    normalized_roles = set()
    for role in user_roles:
        normalized_roles.add(role_normalization_map.get(role, role))

    employee_company = frappe.db.get_value("Employee", {"user_id": user}, "company")
    if not employee_company:
        return "1=0"  # لا يوجد موظف مرتبط، لا يسمح برؤية أي مهمة

    roles_list = "', '".join(normalized_roles)

    # في Service Task ما فيش organization، فقط شرط الدور
    conditions = f"""
        assigned_role IN ('{roles_list}')
    """
    return conditions
