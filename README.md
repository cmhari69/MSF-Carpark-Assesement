# Car Park Availability Assessment

CarParkSolution is an OutSystems 11 web application for exploring Singapore car park availability using public data from data.gov.sg. The solution separates the public interface, core services, synchronisation, and external integrations.

## Review the application

| Item | Details |
| --- | --- |
| Live application | Add the published `CarPark` URL before submission. |
| OutSystems environment | Add the environment hostname and reviewer access instructions. Send any credentials separately. |
| Solution export | `CarParkSolution` V1. The source Platform Server version recorded in the export is `11.42.1.47790`. [Download the OSP](outsystems/application-export/CarParkSolution-v1.osp) |
| Data source | Singapore Government open data portal. Add the exact dataset title, dataset URL, and consumed REST endpoint from `DataGov_IS`. [data.gov.sg](https://data.gov.sg/) |

To review the live application, open the public screen, find a car park, and check the availability shown for that location and its update time. For a technical review, follow the integration in `DataGov_IS`, the synchronisation logic in `CPA_Sync_CS`, the core services in `CPA_CS`, and the `CarPark` screen.

## Application architecture

| Layer | Packaged CarPark components |
| --- | --- |
| End-user | `CarPark`, in the `CPA Public` application |
| Core | `CPA_CS`, `CPA_Sync_CS` |
| Foundation | `DataGov_IS`, `OneMap_IS`, `CPA_Common_Lib`, in the `CPA Foundation` application |
| Supporting components | `OpenstreetMapPlugin`, `OutSystemsUI`, and additional components listed in the deployment notes |

The layer boundaries make it possible to review the public UI, data synchronisation, and external API handling independently. The architecture notes match the names in the V1 export and explain which boxes in the original design have no separate module in the package. [Architecture notes](docs/architecture.md) · [Original architecture diagram](docs/carpark_three_layer_architecture_clean.png)

## Repository structure

```text
.
├── README.md
├── outsystems/
│   ├── README.md
│   └── application-export/CarParkSolution-v1.osp
├── docs/
│   ├── architecture.md
│   └── carpark_three_layer_architecture_clean.png
├── infrastructure/README.md
├── tests/
│   ├── README.md
│   └── test_osp.py
└── .github/workflows/assessment-checks.yml
```

## Deploy to OutSystems 11

Use Service Center to upload and publish the solution in a compatible environment. Review its packaged dependencies and configure integration settings before the first synchronisation. [Deployment and access instructions](outsystems/README.md)

## Run the automated checks

From the repository root, run the package checks with Python 3.9 or later.

```bash
python -m unittest discover -s tests -v
```

These checks cover archive integrity, the solution manifest, and the presence of the expected V1 modules and map plugin. GitHub Actions runs the same checks on push and pull request. Application-level automated tests and execution evidence are pending. [Test coverage and runtime scenarios](tests/README.md)

## AWS infrastructure

The repository currently contains the AWS scope and deployment notes. Add the actual Infrastructure as Code and record whether it was validated, planned, or applied. Record the hosting location of the live OutSystems demo separately. [AWS infrastructure notes](infrastructure/README.md)

## Before submission

- Replace the access and dataset entries above with the verified values. Check the live application URL as a reviewer and grant the requested OutSystems environment access.
- Commit the AWS IaC and runnable application-level tests. Include the validation commands and actual results.
- Grant the reviewer access to the Git repository and include its URL with the application submission.
