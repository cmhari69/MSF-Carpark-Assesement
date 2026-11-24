# OutSystems deployment and access

| Export details | Value |
| --- | --- |
| Solution | `CarParkSolution` |
| Export version | `V1` |
| Source Platform Server | `11.42.1.47790`, as recorded in the manifest |
| Public application and module | `CPA Public` / `CarPark` |

The OSP is a solution export. It carries the CarPark modules, `OpenstreetMapPlugin`, `Sleep`, `OutSystemsUI`, `RichWidgets`, `Users`, and several system extensions. The uploaded file was renamed for the repository with its content preserved. [Download the OSP](application-export/CarParkSolution-v1.osp)

## Publish to a reviewer environment

1. Use a compatible OutSystems 11 environment and an account authorised to publish solutions. Compare platform and dependency versions with the target before publishing, especially in a shared environment.
2. In Service Center, open **Factory → Solutions** and use **Upload & Publish a Solution** to upload the OSP. Review dependency or compatibility issues reported by Service Center and confirm the final publish result there.
3. Review consumed REST API configuration and any environment-specific properties in the target. Use environment configuration for any credentials required by the deployed integrations.
4. Run or verify the first data synchronisation using the mechanism configured by the solution. If it uses a Timer, check the Timer run and recent integration errors in Service Center.
5. Open the published `CarPark` application and exercise a known car park lookup. Verify availability, source freshness, and the map if it is enabled.

## Reviewer access

Add the published application URL and environment hostname to the root README. If platform access requires sign-in, use a named reviewer account with the access needed for the review. Share credentials separately and record the scope provided. [Root README](../README.md#review-the-application)
