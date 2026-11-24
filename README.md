# Car Park Availability Assessment

CarParkSolution is an OutSystems 11 web application for exploring Singapore car park availability using public data from data.gov.sg. The solution separates the public interface, core services, synchronisation, and external integrations.

## Review the application

| Item | Details |
| --- | --- |
| Live application | Add the published `CarPark` URL before submission. |
| OutSystems environment | Environment URL: https://hariharan-chandrasekaran.outsystemscloud.com/CarPark/  |
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

### Scalability for the next phase
The diagram shows the MVP modules (solid) and the planned modules (dashed). The layering
lets the future modules be added without changing the MVP modules:
- **CPA_Admin** can be added in the end-user layer. It consumes existing Core services
  (CPA_CS, CPA_Sync_CS, Audits_CS) and needs no changes to CPA_Public.
- **CPA_Widgets** can take UI blocks out of CPA_Public so Public and Admin share them.
- **Security_Lib, Logger_Lib and Identity_IS** can be added in the foundation layer.
  Core and end-user modules adopt them when required, with no rework of the integrations.
- A new data source (for example a motorcycle or private carpark feed) is a new
  `*_IS` module plus a new sync in CPA_Sync_CS. The CPA_Public screens keep reading from CPA_CS.
- Each layer can be deployed and scaled independently through LifeTime, and Core
  services can be exposed as REST APIs for other channels such as a mobile app.
