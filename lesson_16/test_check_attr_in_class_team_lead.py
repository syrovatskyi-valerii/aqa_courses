import pytest
from lesson_16.homework_16_1_1 import TeamLead


@pytest.mark.positive
@pytest.mark.parametrize("name, salary, department, programming_language, team_size", [
    ('Valerii', 999.99, "QA", "Python", 4)
])
def test_team_lead_attributes(name, salary, department, programming_language, team_size):
    result = TeamLead(
        name=name,
        salary=salary,
        department=department,
        programming_language=programming_language,
        team_size=team_size
    )

    assert hasattr(result, "name"), "Відсутній атрибут name"
    assert hasattr(result, "salary"), "Відсутній атрибут salary"
    assert hasattr(result, "department"), "Відсутній атрибут department"
    assert hasattr(result, "programming_language"), "Відсутній атрибут programming_language"
    assert hasattr(result, "team_size"), "Відсутній атрибут team_size"
