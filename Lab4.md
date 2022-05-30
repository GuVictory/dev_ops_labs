# 4

## Infrastructure as code

0. You may need VPN for this lab, as terraform is not working properly in Russia.

1. Get familiar with Terraform tool.

> https://www.terraform.io/intro/index.html
> https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html

2. Create a `terraform` folder for your workspaces.
3. Create a workspace for a Virtualbox provider for Terraform.
* Install Virtualbox
* Create a workspace.
* Prepare .tf ﬁles with 3 VMs.
* Use terraform fmt, terraform validate.
* Create a VMs.

4. Use the Github provider for Terraform.
* Create a workspace for your Github project.
* Prepare .tf ﬁles that should include:
    * repository name
    * repository description (Solutions to DevOps labs)
    * visibility
    * default branch
    * branch protection rule for default branch

5. Import your repository to terraform
6. Apply changes from your terraform config to the repository
7. Create a TF.md and provide Terraform related best practices that you found.

### List of requirements

* `terraform` folder with two workspaces is present
* TF.md file is present and contains best practices for terraform
* The workspace with Virtualbox configuration is present
* Screenshot with 3 VMs in TF.md
* The workspace with GitHub repository configuration is present
* Your repository is imported to terraform and configurations are applied
* Screenshots with default branch and branch protection rules from github settings should be provided in TF.md

## Bonus

1. Add several teams to your repository using terraform, provide them different level of access. Apply changes.
2. Add @safinsaf to a team that has admin rights in your repository (by hands), so I am able to see the settings button and check teams in your repository. (You can verify it on your friends the same way).