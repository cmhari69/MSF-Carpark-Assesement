# AWS infrastructure

**AWS infrastructure code and validation results are pending.** Add the Terraform or CloudFormation files used for the assessment here.

For a customer-managed OutSystems 11 deployment on AWS, document the supported Windows/IIS and SQL Server versions for the selected O11 release. The IaC should cover the network, load balancer and TLS, front ends and Deployment Controller placement, supported SQL Server configuration, access controls, outbound API connectivity, and backup and monitoring settings. Record which platform installation and licence steps are handled outside the IaC.

If Terraform is used, add the provider lockfile, example inputs, and prerequisites. From the repository root, validate the configuration once the `.tf` files have been added.

```bash
terraform -chdir=infrastructure fmt -check -recursive
terraform -chdir=infrastructure init -backend=false
terraform -chdir=infrastructure validate
```

Record the deployment model, AWS region, validation and plan results, and whether any resources were applied. Identify the actual live demo environment in the root README.
