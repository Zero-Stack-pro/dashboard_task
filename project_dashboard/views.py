from django.shortcuts import render
from django.utils import timezone

from .models import Project, Task


def dashboard_view(request):
    # Получаем список всех проектов
    projects = Project.objects.all().order_by("id")
    project_count = projects.count()
    # Индекс текущего проекта (по кругу)
    current_index = int(request.GET.get("project", 0))
    if current_index < 0 or current_index >= project_count:
        current_index = 0
    current_project = projects[current_index] if project_count > 0 else None

    # Фильтр по статусу задачи
    status_filter = request.GET.get("status", "")
    tasks_qs = (
        Task.objects.select_related("project").filter(project=current_project)
        if current_project
        else Task.objects.none()
    )
    if status_filter:
        tasks_qs = tasks_qs.filter(status=status_filter)
    else:
        tasks_qs = tasks_qs.exclude(status="done")

    # Для цветового выделения
    today = timezone.now().date()
    tasks = []
    for task in tasks_qs:
        if task.deadline < today:
            color = "danger"  # красный
        elif task.deadline == today:
            color = "warning"  # оранжевый
        else:
            color = "success"  # зелёный
        tasks.append(
            {
                "obj": task,
                "color": color,
            }
        )

    # Для аналитики по задачам
    if current_project:
        all_tasks = Task.objects.filter(project=current_project)
        analytics_total = all_tasks.count()
        analytics_done = all_tasks.filter(status="done").count()
        analytics_overdue = (
            all_tasks.filter(deadline__lt=today)
            .exclude(status="done")
            .count()
        )
    else:
        analytics_total = 0
        analytics_done = 0
        analytics_overdue = 0

    context = {
        "projects": projects,
        "current_project": current_project,
        "current_index": current_index,
        "project_count": project_count,
        "tasks": tasks,
        "status_filter": status_filter,
        "status_choices": Task.STATUS_CHOICES,
        "analytics_total": analytics_total,
        "analytics_done": analytics_done,
        "analytics_overdue": analytics_overdue,
    }
    return render(request, "project_dashboard/dashboard.html", context)
