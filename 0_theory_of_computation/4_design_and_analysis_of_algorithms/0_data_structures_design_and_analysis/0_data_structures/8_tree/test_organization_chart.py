from use_cases.general_tree.organization_chart import OrganizationChartNode
from use_cases.general_tree.organization_chart import Personnel
import pytest

tree_data_sections = ["designation", "name", "both"]


@pytest.mark.parametrize("tree_data", tree_data_sections)
def test_print_organization_chart(tree_data):
    root = OrganizationChartNode(Personnel("CEO", "Nilupul"))

    cto = root.add_child(Personnel("CTO", "Chinmay"))
    hr_head = root.add_child(Personnel("HR Head", "Gels"))

    infra_head = cto.add_child(Personnel("Infrastructure Head", "Vishwa"))
    app_head = cto.add_child(Personnel("Application Head", "Aamir"))

    recruitment_man = hr_head.add_child(Personnel("Recruitment Manager", "Peter"))
    policy_man = hr_head.add_child(Personnel("Policy Manager", "Waqas"))

    cloud_man = infra_head.add_child(Personnel("Cloud Manager", "Dhaval"))
    app_man = infra_head.add_child(Personnel("App Manager", "Abhijit"))

    root.print_tree(tree_data)


if __name__ == "__main__":
    for type in tree_data_sections:
        test_print_organization_chart(type)
        print("\n")
