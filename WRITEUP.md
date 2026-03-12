Write-up Template
Project Overview

This project demonstrates deploying a Flask-based Content Management System (CMS) on Microsoft Azure. The application allows users to create and view articles through a web interface. Articles include a title, author name, body content, and an associated image stored in Azure Blob Storage.

Azure Services Used

The following Azure services were used to deploy and manage the CMS application:

Azure App Service – Hosting the Flask web application

Azure SQL Database – Storing article data

Azure Blob Storage – Storing images associated with articles

Microsoft Entra ID – Providing Microsoft sign-in authentication

GitHub Actions – Continuous Integration and Continuous Deployment (CI/CD)

Section 1 — VM vs App Service Analysis
Virtual Machine (VM) Analysis
Cost

Running the CMS application on a Virtual Machine requires paying for compute resources, storage, and networking. The VM must remain running continuously even when there is little or no traffic, which increases operational costs. Additional resources such as load balancers may also be required for scaling and availability.

Scalability

Scaling a VM-based application requires manual configuration. Administrators must resize the VM or create additional instances and configure load balancing. This process requires more effort and monitoring compared to platform-managed services.

Availability

High availability in a VM environment requires deploying multiple VM instances and configuring load balancing and failover mechanisms. This adds complexity and increases infrastructure management responsibilities.

Workflow

Deploying a CMS application on a VM requires manual server setup. Developers must install Python, configure web servers, manage dependencies, apply security patches, and maintain the operating system. This workflow is more complex and requires continuous maintenance.

Azure App Service Analysis
Cost

Azure App Service offers flexible pricing tiers and includes infrastructure management. For a small application like this CMS project, the Free or Basic tier is sufficient. This significantly reduces infrastructure costs compared to maintaining a full virtual machine.

Scalability

App Service provides built-in scaling capabilities. Applications can scale automatically based on traffic or resource usage without manually provisioning additional servers.

Availability

Azure App Service includes built-in load balancing and high availability features. Microsoft manages the underlying infrastructure to ensure reliability and uptime without requiring manual configuration of redundant servers.

Workflow

The deployment workflow is simplified using Azure App Service. The application can be deployed directly from GitHub using GitHub Actions. This enables automated CI/CD pipelines where application updates are deployed automatically whenever changes are pushed to the repository.

Section 2 — Deployment Decision

Based on the analysis above, Azure App Service was selected as the preferred deployment solution for the CMS application.

Azure App Service simplifies deployment and reduces infrastructure management by handling the underlying servers, scaling, and availability automatically. It also integrates easily with GitHub for continuous deployment, allowing developers to focus on application development instead of infrastructure maintenance.

For a lightweight web application such as this CMS, Azure App Service provides sufficient scalability, reliability, and cost efficiency compared to managing a Virtual Machine.

Section 3 — App Changes That Could Change the Decision

If the CMS application required greater control over the server environment, such as installing custom system software, configuring specialized networking rules, or running multiple background services, deploying the application on a Virtual Machine might become more appropriate.

Additionally, if the application required system-level dependencies or advanced server configurations that are not supported within Azure App Service, a Virtual Machine would provide greater flexibility because it allows full control over the operating system and infrastructure.

Database

The CMS application stores article data in Azure SQL Database.

Example query used to retrieve articles:

SELECT * FROM articles;
Application Features

Create articles with title, author, and body

Store article data in Azure SQL Database

Display images stored in Azure Blob Storage

Authenticate users using Microsoft Entra ID

Automatically deploy updates through GitHub Actions CI/CD

Live Application

https://cms-articles-2026-f2dwc4cng5fja5hq.centralus-01.azurewebsites.net/create

Repository

https://github.com/Jashan122005/the-cms-project/tree/main