from use_cases.general.organization_chart import OrganizationChartNode
from use_cases.general.organization_chart import Personnel

import pytest

tree_data_sections = ["designation", "name", "both"]

@pytest.mark.parametrize("tree_data", tree_data_sections)
def test_print_organization_chart(tree_data):
    root = OrganizationChartNode(Personnel("CEO", "Nilupul"))
    cto = OrganizationChartNode(Personnel("CTO", "Chinmay"))
    hr_head = OrganizationChartNode(Personnel("HR Head", "Gels"))
    infra_head = OrganizationChartNode(Personnel("Infrastructure Head", "Vishwa"))
    cloud_man = OrganizationChartNode(Personnel("Cloud Manager", "Dhaval"))
    app_man = OrganizationChartNode(Personnel("App Manager", "Abhijit"))
    app_head = OrganizationChartNode(Personnel("Application Head", "Aamir"))
    recruitment_man = OrganizationChartNode(Personnel("Recruitment Manager", "Peter"))
    policy_man = OrganizationChartNode(Personnel("Policy Manager", "Waqas"))

    root.add_child(cto)
    root.add_child(hr_head)

    cto.add_child(infra_head)
    cto.add_child(app_head)

    hr_head.add_child(recruitment_man)
    hr_head.add_child(policy_man)

    infra_head.add_child(cloud_man)
    infra_head.add_child(app_man)

    root.print_tree(tree_data)


if __name__ == "__main__":
    for type in tree_data_sections:
        test_print_organization_chart(type)
        print("\n")
